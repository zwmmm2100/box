import requests
from bs4 import BeautifulSoup
import codecs
global headers
import time
strs = 'file:///C:/Users/Administrator/Desktop/html/' + '1.html'
x = "<a href=%s>111</a>" %strs + '\n'
list_name = 'C:/Users/Administrator/Desktop/html/' + 'mulu.html'
s = codecs.open(list_name,'w',encoding='utf-8')
s.write(x)
s.close()


res = requests.get('https://sspai.com/post/50253?article_id=50253')
url_text = res.text
soup = BeautifulSoup(url_text,'lxml')
ssss= soup.find(class_="article-margin").find(class_="title").text
lianjie = 'C:/Users/Administrator/Desktop/html/' + ssss + '.html'
s = codecs.open(lianjie,'w',encoding='utf-8')
s.write(x)
s.close()
print(ssss)
