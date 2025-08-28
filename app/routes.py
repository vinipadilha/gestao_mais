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

@app.route("/fornecedores")
def fornecedores():
    return render_template("fornecedores.html")

@app.route("/categorias")
def categorias():
    return render_template("categorias.html")

@app.route("/formaspagamento")
def formaspagamento():
    return render_template("formaspagamento.html")

@app.route("/vendas")
def vendas():
    return render_template("vendas.html")
    
@app.route("/caixa")
def caixa():
    return render_template("caixa.html")

