from PIL import Image
import PyPDF2

ss = PyPDF2.PdfFileMerger()
file_path_list = []
file_path_list.append('1.png')
file_path_list.append('2.png')
print(file_path_list)
for i in file_path_list:
	ss.append(i)
print(ss)
ss.write('444.pdf')

#合并两张图片为pdf