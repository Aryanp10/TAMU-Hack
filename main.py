from flask import Flask
from flask import render_template, request, url_for, redirect, g, session, flash
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
        # command = "CREATE TABLE user_info (id varchar(5), name varchar(30), school varchar(100), email varchar(40), password varchar(100), PRIMARY KEY(email) )"
        # cursor.execute(command)

        # cursor.execute("SELECT * FROM user_info")       
        # result = cursor.fetchall()
        # for row in result:
        #     print(row)

        session['id'] = genID(5)
        session['name'] = request.form['name']
        session['school'] = request.form['school']
        session['email'] = request.form['email']
        session['password'] = request.form['password']
 
        command = f"INSERT INTO user_info VALUES ('{session['id']}', '{session['name']}', '{session['school']}', '{session['email']}', '{session['password']}')"
        try:
            cursor.execute(command)
            conn.commit()
            cursor.execute("SELECT * FROM user_info")       
            result = cursor.fetchall()
            for row in result:
                print(row)
            return redirect(url_for("signin"))
        except:
            return render_template("emailerror.html")
    else:
        return render_template("index.html")


@app.route("/emailerror", methods=["POST", "GET"])
def emailerror():
    if request.method == "POST":
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        session['id'] = genID(5)
        session['name'] = request.form['name']
        session['school'] = request.form['school']
        session['email'] = request.form['email']
        session['password'] = request.form['password']
 
        command = f"INSERT INTO user_info VALUES ('{session['id']}', '{session['name']}', '{session['school']}', '{session['email']}', '{session['password']}')"
        try:
            cursor.execute(command)
            conn.commit()
            cursor.execute("SELECT * FROM user_info")       
            result = cursor.fetchall()
            for row in result:
                print(row)
            return redirect(url_for("signin"))
        except:
            return render_template("emailerror.html")
    else:
        return render_template("emailerror.html")

@app.route("/signin", methods=["POST", "GET"])
def signin():
    if request.method == "POST":
        session['signin_email'] = request.form['signin_email']
        session['signin_password'] = request.form['signin_password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        # cursor.execute("SELECT * FROM user_info")       
        # result = cursor.fetchall()
        # for row in result:
        #     print(row)

        command=f"SELECT COUNT(*) FROM user_info WHERE email LIKE '%{session['signin_email']}%' AND password LIKE '%{session['signin_password']}%'"
        cursor.execute(command)
        if cursor.fetchall()[0][0] == 1:
            session['accountemail'] = session['signin_email']
            return redirect(url_for("index"))
        else:

            flash('Email or password does not match.')
    return render_template("signin.html")


if __name__ == "__main__":
    app.run(debug=True)