import requests 
from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
import re


all_data = []

driver = webdriver.Chrome()  # 根据实际情况设置Chrome驱动程序的路径


for page in range(1,9):
    driver.get(f"https://zidian.qianp.com/duoyinzi_{page}.html")
    wait = WebDriverWait(driver, 10)
    timeout = 30 # 超时秒数

    prev_count = 0
    while True:
        curr_count = driver.execute_script("return window.performance.getEntries().length;")
        
        if curr_count > prev_count:
            # 请求数增加,页面还在加载
            prev_count = curr_count
        else:
            # 请求数不再增加,页面加载完毕
            break
        time.sleep(1)
        
        timeout -= 1
        if timeout == 0:
            raise TimeoutException
    # 获取页面源码
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    open('../html/duoyinzi.html', 'w').write(html)
    duoyinzi_list = soup.find('ul', class_='txt w3 f18')
    for item in duoyinzi_list.find_all('li'):
        word = item.a.text[0]
        title = item.a['title'] 
        pinyins = re.split('、', title)
            
        data = {
            'word': word, 
            'pinyins': pinyins
        }
        all_data.append(data)
        
df = pd.DataFrame(all_data)
df.to_excel('../excel/duoyinzi.xlsx', index=False)