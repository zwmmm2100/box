import urllib.request
from bs4 import BeautifulSoup
import base64
import re
url = 'http://jandan.net/ooxx/page-39#comments'
res = urllib.request.urlopen(url)
soup = BeautifulSoup(res,'lxml')
sss = soup.find_all(class_="tucao-like-container")
for i in sss:
		
	if int(i.span.text) > 100:
		hash_url = i.parent.parent.find(class_="text").find(class_="img-hash").text
		imgurl = base64.b64decode(hash_url).decode('utf-8')
		real_imgurl = 'http:' + imgurl
		gan_weizhi = real_imgurl.index('/',22)
		real_large_imgurl = real_imgurl[:22] + 'large' + real_imgurl[gan_weizhi:]

		print(real_large_imgurl)
