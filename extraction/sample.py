import PyPDF2
from tabula import read_pdf
from tabulate import tabulate


def fileReader():
    pdfName = open(
        'C:/Users/ammar/Desktop/tamuHack/TAMU-Hack/extraction/file.pdf', 'rb')
    try:
        pdfRead = PyPDF2.PdfFileReader(pdfNam)

        for i in range(pdfRead.getNumPages()):
            page = pdfRead.getPage(i)
            if i > 0:
                print(
                    '==================================================================================')
            pageContent = page.extractText()
            print(pageContent)
    except Exception as e:
        print("Error {}".format(e))


if __name__ == "__main__":
    fileReader()
