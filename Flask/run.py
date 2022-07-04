# coding=utf-8
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    items = ["Apfel", "Birne", "Banane"]
    
    return render_template("start.html, name="Max Mustermann", items=items)

@app.route("/test")
def test():
    return render_template("test.html", name="Max Mustermann")