import PyPDF2
from tabula import read_pdf
from tabulate import tabulate


def fileReader():
    pdfName = open(
        'C:/Users/ammar/Desktop/tamuHack/TAMU-Hack/extraction/file.pdf', 'rb')

    pdfRead = PyPDF2.PdfFileReader(pdfName)

    for i in range(pdfRead.getNumPages()):
        page = pdfRead.getPage(i)
        if i > 0:
            print(
                '==================================================================================')
        pageContent = page.extractText()
        print(pageContent)


if __name__ == "__main__":
    fileReader()
