import os
from PyPDF2 import PdfFileReader, PdfFileWriter
 
 # Input the path of the file, start and end page of pdf

def pdf_splitter(path,start,end):
    fname = os.path.splitext(os.path.basename(path))[0]
 
    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()
    if start == end:
        pdf_writer.addPage(pdf.getPage(start-1))
    else:
        for i in range(start-1,end):
            pdf_writer.addPage(pdf.getPage(i))
 
    output_filename = '{}_page_{}.pdf'.format(
            fname, start)
 
    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)
 
    print('Created: {}'.format(output_filename))
    
    if __name__ == '__main__':
    path = '/Users/tianma/Desktop/Li Haoran/pdf scan/scan.pdf'
    pdf_splitter(path,11,11)