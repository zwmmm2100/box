import pdfkit

sss = []
for i in range(19):
	file_name = str(i) + '.html'
	sss.append(file_name)


pdfkit.from_file(sss,'list.pdf')