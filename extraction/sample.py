import PyPDF2
import tabula as tb
from tabulate import tabulate


def fileReader():
    pdfName = open('extraction/file.pdf', 'rb')

    try:
        pdfRead = PyPDF2.PdfFileReader(pdfName)

        for i in range(pdfRead.getNumPages()):
            page = pdfRead.getPage(i)
            if i > 0:
                print(
                    '==================================================================================')
            pageContent = page.extractText()
            print(pageContent)
    except Exception as e:
        print("Error {}".format(e))


def tableReader():
    pdfName = "extraction/file3.pdf"

    try:
        dfs = tb.read_pdf(pdfName, pages='all')
        print(dfs)
    except Exception as e:
        print("Error {}".format(e))


'''
    try:
        df = tb(pdfName)
        print(df)
    except Exception as e:
        print("Error {}".format(e))
'''

if __name__ == "__main__":
    tableReader()
