import pdfkit

sss = []
#把所有html文件地址加到sss列表
for i in range(19):
	file_name = str(i) + '.html'
	sss.append(file_name)

#用pdfkit把sss列表中的文件合并为一个pdf文件
pdfkit.from_file(sss,'list.pdf')