from flask import Flask, render_template, request, redirect, url_for

lista_produtos = [
    { "nome": "Coca-cola", "descricao": "veneno", "preco": 12.02, "imagem": "" },
    { "nome": "Doritos", "descricao": "suja mão", "preco": 12.02, "imagem": "" },
    { "nome": "Água", "descricao": "mata sede", "preco": 12.02, "imagem": "" },
]

app = Flask("minha app")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"


@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)
    

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto['nome'] == nome:
            return render_template("produto.html", produto=produto)

    return "Produto não existe!"

# GET
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro-produto.html")

# POST
@app.route("/produtos", methods=["POST"])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = request.form['preco']
    imagem = request.form['imagem']
    produto = { "nome": nome, "descricao": descricao, "preco": preco, "imagem": imagem }
    lista_produtos.append(produto)
    
    return redirect(url_for("produtos"))



app.run(port=5001)