from main import app
from flask import render_template

@app.route("/")
def homepage():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/estoque")
def estoque():
    return render_template("estoque.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

