import requests
from bs4 import BeautifulSoup
import pandas as pd
# 创建保存表
# school_list = workbook['Sheet1']
# driver = webdriver.Edge('../msedgedriver.exe')  # 根据实际情况设置Chrome驱动程序的路径

# 获取网页内容
# url列表
# 使用BeautifulSoup解析HTML
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-cw.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-hke.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-i.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-sou.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-wch.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-kc.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-kt.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-sk.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-ssp.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-wts.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-ytm.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-n.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-st.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-tp.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-kwt.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-tw.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-tm.html'
# url = 'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-yl.html'

urls = [
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-cw.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-hke.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-i.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-sou.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-wch.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-kc.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-kt.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-sk.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-ssp.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-wts.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-ytm.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-n.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-st.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-tp.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-kwt.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-tw.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-tm.html',
    'https://www.edb.gov.hk/en/student-parents/sch-info/sch-search/schlist-by-district/school-list-yl.html'
]
schools = []

for url in urls:

    response = requests.get(url)
    response.encoding = 'utf-8'  # 明确指定编码方式
    soup = BeautifulSoup(response.text, 'html.parser')

    # 保存soup到文件,追加

    # with open('../html/school.html', 'w', encoding='utf-8') as f:
    #     f.write(str(soup))

    # 找到所有表格 A
    tables = soup.findAll('table', {'class': 'tablestyleA'})

    # with open('../html/tables.html', 'w', encoding='utf-8') as f:
    #     f.write(str(tables))

    # 遍历每个表格A

        # 获取表格的第二个tr 
            # 第一个td中的第二个br 是区域 area
            # 第二个td中的第二个br 是类型 type 
        # 获取表格中的第三个tr
            # 获取上面的tr中的表格table 
            # 遍历这个table 
                # 从第二个tr 开始，第二个tr是学校信息，第三个tr是学校网址，第四个是下一所学校的信息，第五个是下一所学校的网址，依次类推
                # 上面学校信息tr中，第二个td
                    # td的第一个tr是 学校英文名 name_en
                    # td的第二个tr是 学校英文地址 addr_en
                    # td的第三个tr是 中文名 name
                    # td的第四个tr是 学校地址 addr
                    # td的第5个tr是 学校no no
                # 第三个td 获取里面的table
                    # 第一个tr 第一个td电话 phone
                    # 第二个tr 里面第一个td 内容是 fax
                
                # 第四个td 获取里面的table
                    # 第一个tr 里面第一个td是 supervisor
                    # 第二个tr 里面的第一个td 是 headmaster
                # 学校网址tr   获取里面的a链接地址 是 website
                # 保存 area no name type name_en addr phone fax website 到excel 表的一行

    # 初始化一个空的列表来保存所有学校的信息

    for table_a in tables:
        # with open('../html/table.html', 'w', encoding='utf-8') as f:
        #     f.write(str(table_a))
        # print(table_a)
        area = table_a.find_all('tr')[1].find_all('td')[0].text
        type = table_a.find_all('tr')[1].find_all('td')[1].text

        list = table_a.find_all('tr')[2].find_all('table', {'border':'1'})[0].find_all('tr', recursive=False)[1:]
        for school_info in list:
            # print(school_info)
            with open('../html/school_info.html', 'w', encoding='utf-8') as f:
                f.write(str(school_info))
            school = {}
        
            if school_info.find_all('td')[1].text in "Website 網址":
                continue
            school['area'] = area
            school['type'] = type
            name_en = school_info.find_all('td')[1].find_all('tr')[0].text
            print(name_en)   
            school['name_en'] = name_en
        
            addr_en = school_info.find_all('td')[1].find_all('tr')[1].text
            school['addr_en'] = addr_en
            print(addr_en)    
            name = school_info.find_all('td')[1].find_all('tr')[2].text
            school['name'] = name
            print(name)
            addr = school_info.find_all('td')[1].find_all('tr')[3].text
            school['addr'] = addr
            print(addr)
            no = school_info.find_all('td')[1].find_all('tr')[4].text
            school['no'] = no
            print(no)
            tel_tag = school_info.find(lambda tag: "Tel. 電話:" in tag.get_text())
            if tel_tag is None:
                print("Tel. 電話: tag not found")
            else:
                connect_text = [line for line in tel_tag.get_text().split("\n") if line.strip()]
                tel_line = connect_text[0]
                fax_line = connect_text[1]
                print(connect_text)

                phone = tel_line.split(":")[1].strip()  # 分割文本并获取电话号码
                fax = fax_line.split(":")[1].strip()
                school['phone'] = phone
                school['fax'] = fax
                print(phone)
                print(fax)
                
                # 联系人
                tel_table = tel_tag
                print(tel_table)
                # 找到下一个兄弟节点，这应该是包含校监和校长信息的<table>标签
                next_table = tel_table.find_next_sibling('td')
                # 获取所有的<tr>标签
                trs = next_table.find_all('tr')

                # 第一个<tr>标签应该包含校监信息
                supervisor = trs[0].get_text().strip()

                # 第二个<tr>标签应该包含校长信息
                headmaster = trs[1].get_text().strip()
                print(supervisor)
                school['supervisor'] = supervisor
                school['headmaster'] = headmaster
                print(headmaster)
            web_tag = school_info.find_next_sibling('tr')
            if web_tag == None:
                website = ""
            else: 
                if web_tag.find('a') == None:
                    website = ""
                else:
                    website = web_tag.find('a')['href']    
            school['website'] = website
            print(website)
            schools.append(school)
print(schools)
# 将学校信息保存到Excel文件
df = pd.DataFrame(schools)
df.to_excel('schools.xlsx', index=False)
