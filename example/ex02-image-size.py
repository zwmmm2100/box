#用image打开图片，并对图片的大小进行更改

from PIL import Image
ss = Image.open('1.png')
ss = ss.resize((300,300),Image.ANTIALIAS)
ss.save("000.png")
print(ss.size[0])