from flask import Flask, render_template, request
import this, operacoes

this.cpf = ""
this.nome = ""
this.telefone = ""
this.endereco = ""
this.data = ""
this.dados = ""
this.dado = ""
this.nDado = ""
this.campo = ""
app = Flask(__name__)  #Representando uma variável do tipo flask

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('/index.html', titulo='Página Inicial')

@app.route('/cadastroCliente.html', methods=['GET', 'POST'])
def cadastrarCliente():
    if request.method == 'POST':
        this.cpf     = request.form['tCPF']
        this.nome    = request.form['tNome']
        this.senha   = request.form['tSenha']
        this.telefone= request.form['tTelefone']
        this.endereco= request.form['tEndereco']
        this.data    = request.form['tData']
        this.dados   = operacoes.cadastrar(this.cpf,this.nome,this.senha,this.telefone,this.endereco,this.data)
    return render_template('/cadastroCliente.html', titulo='Página de Cadastro', resultado=this.dados)

@app.route('/consultarCliente.html', methods=['GET', 'POST'])
def consultar():
    if request.method == 'POST':
        this.CPF = request.form['tCPF']
        this.mensagem = operacoes.consultar(this.CPF)
    else:
        this.mensagem = ""
    return render_template('consultarCliente.html', titulo="Consulta por código", dados=this.mensagem)

@app.route('/sobre.html', methods=['GET', 'POST'])
def sobre():
    return render_template('sobre.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/atualizar.html', methods=['GET','POST'])
def atualizarDados():
    if request.method == 'POST':
        this.CPF = request.form['tCPF']
        this.campo  = request.form['tCampo']
        this.nDado  = request.form['tNovoDado']
        this.dado = operacoes.atualizar(this.CPF, this.campo, this.nDado)
    return render_template('atualizar.html', titulo='Atualizar', resultado=this.dado)

@app.route('/excluir.html', methods=['GET', 'POST'])
def excluir():
    if request.method == 'POST':
        this.CPF = request.form['tCPF']
        this.dado   = operacoes.excluir(this.CPF)
    return render_template('excluir.html', titulo='Excluir', resultado=this.dado)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
