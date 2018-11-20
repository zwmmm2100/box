import io
from PIL import Image
import urllib.request
import ssl
import codecs

ssl._create_default_https_context = ssl._create_unverified_context
res = urllib.request.urlopen('https://mhpic.cnmanhua.com/comic/J%2F%E7%BB%9D%E4%B8%96%E5%94%90%E9%97%A8%2F148%E8%AF%9DGQ%2F1.jpg-mht.middle.webp').read()
byte_stream = io.BytesIO(res)
roiimg = Image.open(byte_stream)
imgbytearr = io.BytesIO()
roiimg.save(imgbytearr,format='PDF')
imgbytearr = imgbytearr.getvalue()
with open("1ss.pdf",'wb') as f:
	f.write(imgbytearr)
print(byte_stream)