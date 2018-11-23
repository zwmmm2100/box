import requests
from bs4 import BeautifulSoup
import codecs
global headers
import time
headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Connection':'keep-alive'}
xurl = 'https://sspai.com/api/v1/articles?offset=0&limit=2&type=recommend_to_home&sort=recommend_to_home_at&include_total=false'

#根据链接收集所有的id加到列表里面
def num_lists(url):
	driver = requests.get(url)
	tesss = driver.json()
	lists = tesss["list"]
	urls = []
	for i in lists:
		
		urls.append(i['id'])
		print(i['id'])
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
	title_files = {}
	for i in lists:
		res = requests.get(i)
		url_text = res.text
		soup = BeautifulSoup(url_text,'lxml')
		ssss= soup.find(class_="article-margin")
		try:
			title = soup.find(class_="article-margin").find(class_="title").text
		except AttributeError as reason:
			print("qusetion is: " + str(reason))
			continue

		html_name = 'C:/Users/Administrator/Desktop/html/' + str(lists.index(i)) + '.html'
		s = codecs.open(html_name,'w',encoding='utf-8')
		s.write(url_text)
		s.close()

		title_url = 'file:///C:/Users/Administrator/Desktop/html/' + str(lists.index(i)) + '.html'
		title_files[title] = title_url
		print('[' + str(lists.index(i)+1) + '/200]' + title + ' is ok.')
		time.sleep(10)
	return title_files



s = num_lists(xurl)
lists = url_lists(s)
oo = down_html(lists)
print(oo)

doc = '<head><meta charset="UTF-8"><style>a{text-decoration:none}</style></head>'
for key in oo:
	doc = doc + "<a href=%s><p>%s</p></a>" %(oo[key],key) + '\n'
list_name = 'C:/Users/Administrator/Desktop/html/' + 'MULU.html'
s = codecs.open(list_name,'w',encoding='utf-8')
s.write(doc)
s.close()
