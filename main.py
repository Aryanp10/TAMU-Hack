from flask import Flask
from flask import render_template, request, url_for, redirect, g, session, flash
import PyPDF2
from flask_sqlalchemy import SQLAlchemy


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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db=SQLAlchemy(app)

class Info(db.Model):
    id=db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    school= db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(200), nullable = False)

    def __repr__(self):
        return '<Task %r>' % self.id


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