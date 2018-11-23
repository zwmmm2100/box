import pdfkit
with open('1.html','w',encoding='utf-8') as f:
    f.write("<p>sdfsdf</p><p>的身份框架</p>")

pdfkit.from_file('1.html','1.pdf')