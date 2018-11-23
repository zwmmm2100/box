import ssl
import urllib.request
from bs4 import BeautifulSoup
import pdfkit
import codecs

ssl._create_default_https_context = ssl._create_unverified_context

html = urllib.request.urlopen("https://python3-cookbook.readthedocs.io/zh_CN/latest/").read()

soup = BeautifulSoup(html,'lxml')
lists = soup.find_all(class_="toctree-l2")
for n,i in enumerate(lists):
	
	list_url = "https://python3-cookbook.readthedocs.io/zh_CN/latest/" + i.a.get('href')
	html2 = urllib.request.urlopen(list_url).read()
	soup2 = BeautifulSoup(html2,'lxml')
	doc_txt = soup2.find_all(class_="section")
	doc_txt_new = '<head><meta charset="UTF-8"></head>' + str(doc_txt)

	html_name = str(n) + 'a.html'
	f = codecs.open(html_name,'w',encoding='utf-8')
	f.write(doc_txt_new)
	f.close()
	print(html_name + " is ok.")
