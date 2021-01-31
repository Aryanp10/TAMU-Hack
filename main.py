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
    if request.method == "POST":
        session['name'] = request.form['name']
        session['school'] = request.form['school']
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        print(session)
        return redirect(url_for("signin"))
    else: 
        return render_template("index.html")

@app.route("/signin", methods=["POST", "GET"])
def signin():
    return render_template("signin.html")

if __name__ == "__main__":
    app.run(debug=True)