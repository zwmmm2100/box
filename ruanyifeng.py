import urllib.request
from bs4 import BeautifulSoup
import codecs
import pdfkit

html = urllib.request.urlopen("http://www.ruanyifeng.com/blog/archives.html")
#要抓取的链接总目录
textt = BeautifulSoup(html,'lxml')
lists = textt.find_all(class_="module-list-item")
for i in range(1):
    bb = lists[i].a['href']
    #提取链接
    txt_name = str(i) + '.txt'
    #每篇文章放入一个文件夹中
    html = urllib.request.urlopen(bb)
    #解析网页
    bsObj = BeautifulSoup(html,'lxml')
    list = bsObj.find_all(class_="asset-content entry-content")
    file_con = list[0].get_text()
    textqqqqq = '<head><meta charset="UTF-8"></head>' + str(list[0])
    #头部加入标示，避免出现乱码
    pdf_file_name = str(i) + '1.pdf'
    pdfkit.from_string(textqqqqq,pdf_file_name)
    #提取文章
    f = codecs.open(txt_name,'w',encoding='utf-8')
    #由于是中文内容，需要转换编码方式
    f.write(file_con)
    #写入
    f.close()

    html_name = str(i) + '.html'
    s = codecs.open(html_name,'w',encoding='utf-8')
    s.write(textqqqqq)
    s.close()
