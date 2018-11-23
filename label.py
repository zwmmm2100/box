from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter

pdf_one = PdfFileMerger()
pdf_one.append(open('01.pdf','w')
pdf_one.merge(0,'11.pdf')
pdf_one.addBookmark('shuqiano',1)
pdf_one.write('222.pdf')