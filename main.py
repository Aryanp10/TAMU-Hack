from flask import Flask
from flask import render_template, request, url_for, redirect, g, session, flash
import PyPDF2
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import random, string
from decimal import Decimal

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
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# db=SQLAlchemy(app)

# class user_info(db.Model):
#     id=db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(200), nullable = False)
#     school= db.Column(db.String(200), nullable = False)
#     email = db.Column(db.String(100), nullable = False)
#     password = db.Column(db.String(200), nullable = False)

#     def __repr__(self):
#         return '<Task %r>' % self.id


def genID(length):
    id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(length)])
    return id



@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # command = "DROP TABLE user_info"
        # cursor.execute(command)
        # command = "CREATE TABLE user_info (id varchar(5), name varchar(30), school varchar(100), email varchar(40), password varchar(100) )"
        # cursor.execute(command)

        cursor.execute("SELECT * FROM user_info")       
        result = cursor.fetchall()
        for row in result:
            print(row)

        session['id'] = genID(5)
        session['name'] = request.form['name']
        session['school'] = request.form['school']
        session['email'] = request.form['email']
        session['password'] = request.form['password']
 
        command = f"INSERT INTO user_info VALUES ('{session['id']}', '{session['name']}', '{session['school']}', '{session['email']}', '{session['password']}')"
        cursor.execute(command)

        cursor.execute("SELECT * FROM user_info")       
        result = cursor.fetchall()
        for row in result:
            print(row)

        conn.commit()
        return redirect(url_for("signin"))
    else:
        return render_template("index.html")

@app.route("/signin", methods=["POST", "GET"])
def signin():


    # session['signin_email'] = request.form['signin_email']
    # session['signin_password'] = request.form['signin_password']

    # command=f"SELECT COUNT(*) FROM user_info WHERE email LIKE '%{session}%'"

    return render_template("signin.html")

if __name__ == "__main__":
    app.run(debug=True)