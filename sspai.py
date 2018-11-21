import requests
from bs4 import BeautifulSoup

url = 'https://sspai.com/'
res = requests.get(url)
url_con = res.text
print(url_con)