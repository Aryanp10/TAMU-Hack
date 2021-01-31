import tabula as tb
import camelot
import pandas as pd
import numpy as np
import re
from PyPDF2 import PdfFileReader, PdfFileWriter

# Read all the text from a pdf file and save teh content on


def fileReader2(pagelist):
    pdfName = open("extraction/file.pdf", 'rb')
    try:
        pdfRead = PdfFileReader(pdfName)
        for i in range(pdfRead.getNumPages()):
            page = pdfRead.getPage(i)
            pagelist.append(page.extractText())
            # page.extractText()
    except Exception as e:
        print("Error {}".format(e))

# Extract Important information ("Course info", "Meeting time", etc.)


# def extractInfo(pagelist):
#     print("Hello")


# def camReader():
#     tables = camelot.read_pdf("extraction/file2.pdf")
#     print(tables)


# def tabReader():
#     tb.io.read_pdf_with_template(
#         input_path="extraction/file2.pdf", stream=True)


# def tableReader():
#     pdfName = "extraction/file3.pdf"

#     try:

#         dfs = tb.read_pdf(pdfName, pages='all', multiple_tables=True)
#         print(dfs[0][0][0])
#     except Exception as e:
#         print("Error {}".format(e))


if __name__ == "__main__":
    pagelist = []
    fileReader2(pagelist)
    print(pagelist[0])
    # counter = 0
    for i in pagelist:
        for f in i:
            if f == ' ' or f == '\n':
                pass

        print(i)
    #     for f in i:
    #         if f ==
    #         print(counter)
    #         counter = counter + 1
    # print(counter)
    # counter = counter + 1
