from PyPDF2 import PdfFileReader, PdfFileWriter


def fileReader2():
    pdfName = open("extraction/file.pdf", 'rb')
    try:
        pdfRead = PdfFileReader(pdfName)
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
    fileReader2()
    print("Hello")
