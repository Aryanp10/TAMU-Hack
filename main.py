from flask import Flask
from flask import render_template, request, url_for, redirect, g, session, flash

app = Flask(__name__)
app.secret_key = "123"

@app.route("/", methods=["POST", "GET"])
def index():

    return render_template("index.html")