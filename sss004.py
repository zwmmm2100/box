import requests
from bs4 import BeautifulSoup

url = 'https://sspai.com/api/v1/search?offset=0&limit=10&type=article&keyword=work'
res = requests.get(url)
url_text = res.text
soup = BeautifulSoup(url_text,'lxml')
ssss= soup.find(class_="article-margin")
print(soup)