from flask import Flask, render_template, request, redirect, url_for

lista_produtos = [
    { "nome": "Coca-cola", "descricao": "veneno", "preco": 10.00, "imagem": https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcR5ULXi2OR1z-cpaVdnMbSm-VNbc5sHy5EOJzD6CD8QO42w_MHQN4eGeT4E2zHEmxkI}
    { "nome": "Doritos", "descricao": "suja mão", "preco": 7.50, "imagem": https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlQATu8RC7xxlru61gmTjNhu8l8JM-_cm4qA&s}
    { "nome": "Água", "descricao": "mata sede", "preco": 10.00, "imagem": https://aguamineralhydrate.com.br/wp-content/uploads/2016/02/Garrafa-Agua-Mineral-1-5-litro-entrega.jpg}
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


@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro-produto.html")

#POST
@app.route("/produtos", methods=['POST'])
def salvar_produto():
    nome= request.form['nome']
    descricao = request.form['descricao']
    preco = request.form['preco']
    produto = {"nome": nome, "descricao": descricao, "preco": preco}
    lista_produtos.append(produto)

    return redirect(url_for("produtos"))

app.run(port=5001)