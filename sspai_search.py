import requests
from bs4 import BeautifulSoup
search_text = 'workflow'
url = 'https://sspai.com/api/v1/search?offset=0&limit=10&type=article&keyword=%s' %search_text
res = requests.get(url)
url_text = res.text
soup = BeautifulSoup(url_text,'lxml')
ssss= soup.find(class_="article-margin")
print(soup)
#解析网页
#保存成文本形式
#生成目录
#带目录的pdf格式
