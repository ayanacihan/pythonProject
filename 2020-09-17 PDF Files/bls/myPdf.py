#first we created virtual environment via the Terminal
'''cihanayana@repeaterhost bls % python3 -m venv myenv
cihanayana@repeaterhost bls % cd myenv
cihanayana@repeaterhost myenv % cd bin
cihanayana@repeaterhost bin % source activate
(myenv) cihanayana@repeaterhost bin % '''

from PyPDF2 import PdfFileReader

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f: #r is for read, b is for binary
        pdf = PdfFileReader(f) #creating the object
        information = pdf.getDocumentInfo() #return an instance of doc info
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """ #string formatting ends here

    print(txt)
    return information

if __name__ == '__main__':
    path = 'bls/myenv/mypdffile.pdf' #the file location is important
    extract_information(path)

'''OUTPUT
Information about bls/myenv/mypdffile.pdf

Author: Victor M. Alvarez
Creator: LaTeX with hyperref package
Producer: pdfTeX-1.40.18
Subject: 
Title: yara Documentation
Number of pages: 115'''