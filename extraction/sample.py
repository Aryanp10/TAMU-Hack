import PyPDF2
from tabula import read_pdf
from tabulate import tabulate


def fileReader():
    pdfName = open('file2.pdf', 'rb')

    pdfRead = PyPDF2.PdfFileReader(pdfName)

    for i in range(pdfRead.getNumPages()):
        page = pdfRead.getPage(i)
        if i > 0:
            print(
                "======================================================================")
        pageContent = page.extractText()
        print(pageContent)

# str(1 + pdfRead.getPageNumber(page)) <--------------- for page number

# def student_dictionary():


if __name__ == "__main__":
    fileReader()
