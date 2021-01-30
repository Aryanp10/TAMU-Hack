from flask import Flask
from flask import render_template, request, url_for, redirect, g, session, flash
import PyPDF2



# def fileReader():
#     pdfName = "old/file.pdf"

#     pdfRead = PyPDF2.PdfFileReader(pdfName)

#     for i in range(pdfRead.getNumPages()):
#         page = pdfRead.getPage(i)
#         print("Page No: " + str(1 + pdfRead.getPageNumber(page)))
#         pageContent = page.extractText()
#         print(pageContent)


app = Flask(__name__)
app.secret_key = "123"

@app.route("/", methods=["POST", "GET"])
def index():

    return render_template("index.html")

if __name__ == "__main__":
    fileReader()
    app.run(debug=True)