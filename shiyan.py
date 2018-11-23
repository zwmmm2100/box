import io
from PIL import Image
import urllib.request
import ssl
import codecs
import PyPDF2

ssl._create_default_https_context = ssl._create_unverified_context
def url_txt(meau,num):
	return 'https://mhpic.cnmanhua.com/comic/J%2F%E7%BB%9D%E4%B8%96%E5%94%90%E9%97%A8%2F' + str(meau) + '%E8%AF%9DGQ%2F' + str(num) + '.jpg-mht.middle.webp'
for j in range(1,160):
	new_pdf = str(j) + 'p.pdf'
	image_list = []
	ss = PyPDF2.PdfFileMerger()
	for i in range(1,25):
		ssl._create_default_https_context = ssl._create_unverified_context
		try:
		    res= urllib.request.urlopen(url_txt(j,i)).read()
		except urllib.error.HTTPError:
		    break
		byte_stream = io.BytesIO(res)
		roiimg = Image.open(byte_stream)
		imgbytearr = io.BytesIO()
		roiimg.save(imgbytearr,format='PDF')
		imgbytearr = imgbytearr.getvalue()
		image_num = str(i) + '.pdf'
		image_list.append(image_num)
		with open(image_num,'wb') as f:
			f.write(imgbytearr)
		for i in image_list:
			ss.append(i)
		ss.write(new_pdf)

