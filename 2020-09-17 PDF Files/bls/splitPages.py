#This scripts splits the pdf files into one page documents.
from PyPDF2 import PdfFileReader, PdfFileWriter

def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter() #PdfFileReader object
        pdf_writer.addPage(pdf.getPage(page)) #addPage method

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

if __name__ == '__main__':
    path = 'rfrotated.pdf'
    split(path, 'SplitPdf/rfpage')