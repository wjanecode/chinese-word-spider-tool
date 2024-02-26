# 爬取香港成语
from bs4 import BeautifulSoup
import pandas as pd

# 读取本地 HTML 文件
with open('../html/hkdict.idioms.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# 使用 BeautifulSoup 解析 HTML 内容
soup = BeautifulSoup(html_content, 'html.parser')

# 找到所有的成语
# 找到所有的<a>标签
a_tags = soup.find_all('a')
idiom_list = []
for tag in a_tags:
    d_tags = tag.find_all('d')
    if not d_tags:
        text = tag.get_text(separator='', strip=True)
        if text:
            idiom_list.append(text)

# 创建 DataFrame 对象
df = pd.DataFrame({'成语': idiom_list})
# 打印前 5 个成语
print(idiom_list[:65])

# 创建 DataFrame 对象
df = pd.DataFrame({'成语': idiom_list})

# 保存到 Excel 文件
df.to_excel('../excel/idioms.xlsx', index=False)
print('保存成功')