import requests
from bs4 import BeautifulSoup
headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive'}
url = 'https://zhuanlan.zhihu.com/books'
res = requests.get(url,headers=headers)
url_text = res.text
soup = BeautifulSoup(url_text,'lxml')
ssss= soup.find(class_="article-margin")
print(soup)