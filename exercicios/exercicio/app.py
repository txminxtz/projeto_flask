from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ
import random

app = Flask("Validador CPF e CNPJ")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/gerar_cpf")
def gerar_cpf():
    cpf = CPF()
    novo_cpf = cpf.generate()
    return render_template('gerar_cpf.html', cpf=novo_cpf)

@app.route('/gerar_cnpj')
def gerar_cnpj():
    cnpj = CNPJ()
    novo_cnpj = cnpj.generate()
    return render_template('gerar_cnpj.html', cnpj=novo_cnpj)


@app.route('/validar_cpf', methods=['GET', 'POST'])
def validar_cpf():
    if request.method == 'POST':
        cpf_input = request.form['cpf']
        cpf = CPF()
        if cpf.validate(cpf_input):
            return render_template('validar_cpf.html', cpf=cpf_input, mensagem="CPF válido!")
        else:
            return render_template('validar_cpf.html', cpf=cpf_input, mensagem="CPF inválido!")
    return render_template('validar_cpf.html')

@app.route('/validar_cnpj', methods=['GET', 'POST'])
def validar_cnpj():
    if request.method == 'POST':
        cnpj_input = request.form['cnpj']
        cnpj = CNPJ()
        if cnpj.validate(cnpj_input):
            return render_template('validar_cnpj.html', cnpj=cnpj_input, mensagem="CNPJ válido!")
        else:
            return render_template('validar_cnpj.html', cnpj=cnpj_input, mensagem="CNPJ inválido!")
    return render_template('validar_cnpj.html')

if __name__ == '__main__':
    app.run(debug=True)
    