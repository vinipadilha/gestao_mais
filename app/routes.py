from main import app
from flask import render_template

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/estoque")
def estoque():
    return render_template("estoque.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

@app.route("/clientes")
def clientes():
    return render_template("clientes.html")

@app.route("/cadastros/fornecedores")
def fornecedores():
    return render_template("/cadastros/fornecedores.html")

@app.route("/cadastros/categorias")
def categorias():
    return render_template("/cadastros/categorias.html")

@app.route("/cadastros/formaspagamento")
def formaspagamento():
    return render_template("/cadastros/formaspagamento.html")

@app.route("/vendas")
def vendas():
    return render_template("vendas.html")
    
@app.route("/caixa")
def caixa():
    return render_template("caixa.html")

@app.route("/alertas")
def alertas():
    return render_template("alertas.html")

