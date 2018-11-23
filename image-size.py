from PIL import Image
ss = Image.open('1.png')
ss = ss.resize((300,300),Image.ANTIALIAS)
ss.save("000.png")
print(ss.size[0])

