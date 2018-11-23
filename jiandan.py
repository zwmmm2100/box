import urllib.request
import requests
import base64
from bs4 import BeautifulSoup
old_url = 'http://jandan.net/ooxx/page-%d#comments'
imgurl_lists = []
for x in range(1,41):
	url = old_url %x 
	res = urllib.request.urlopen(url)
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}

	soup = BeautifulSoup(res,'lxml')
	sss = soup.find_all(class_="tucao-like-container")

	for i in sss:
		
		if int(i.span.text) > 100:
			hash_url = i.parent.parent.find(class_="text").find(class_="img-hash").text
			imgurl = base64.b64decode(hash_url).decode('utf-8')
			real_imgurl = 'http:' + imgurl
			real_large_imgurl = real_imgurl.replace('mw600','large')
			print(real_large_imgurl)
			imgurl_lists.append(real_large_imgurl)

			'''
	print(imgurl_lists)
for url in imgurl_lists:
	s = requests.get(url)
	with open(str(imgurl_lists.index(url)) + '.jpg', 'wb') as f:
		f.write(s.content)
'''


