import requests
from bs4 import BeautifulSoup
import codecs
global headers
headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive'}
url = 'https://sspai.com/api/v1/articles?offset=0&limit=1&type=recommend_to_home&sort=recommend_to_home_at&include_total=false'

#根据链接收集所有的id加到列表里面
def num_lists(url):
	driver = requests.get(url)
	tesss = driver.json()
	lists = tesss["list"]
	urls = []
	for i in lists:
		
		urls.append(i['id'])
	return urls
#根据id列表拼凑real链接地址
def url_lists(url_l):
	real_url_lists = []
	for i in url_l:
		real_url = 'https://sspai.com/post/%d?article_id=%d' %(i,i)
		real_url_lists.append(real_url)
	return real_url_lists
#下载html
def down_html(lists):
	for i in lists:
		res = requests.get(i)
		url_text = res.text
		soup = BeautifulSoup(url_text,'lxml')
		ssss= soup.find(class_="article-margin")
		html_name = str(lists.index(i)) + '.html'
		s = codecs.open(html_name,'w',encoding='utf-8')
		s.write(str(url_text))
		s.close()

s = num_lists(url)
lists = url_lists(s)
down_html(lists)




