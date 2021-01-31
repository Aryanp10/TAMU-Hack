from PyPDF2 import PdfFileReader, PdfFileWriter

# Read all the text from a pdf file and save teh content on 
def fileReader2(pagelist):
    pdfName = open("extraction/file.pdf", 'rb')
    try:
        pdfRead = PdfFileReader(pdfName)
        for i in range(pdfRead.getNumPages()):
            page = pdfRead.getPage(i)
            pagelist.append(page.extractText().replace('\n', ''))
    except Exception as e:
        print("Error {}".format(e))


# Extract Important information ("Course info", "Meeting time", etc.)
def extractInfo(pagelist):
    print("Hello")

if __name__ == "__main__":
    pagelist = []
    fileReader2(pagelist)
    print(pagelist)
