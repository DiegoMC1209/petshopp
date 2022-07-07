from flask import Flask, render_template, request
import this, conexao

db_connection = conexao.conexao()
con = db_connection.cursor()

App = Flask(__name__)  #Representando uma variável do tipo flask

def cadastrar(cpf,nome,senha,telefone,endereco,dataDeNascimento):
    try:
        sql = "insert into cliente(cpf,nome,senha,telefone,endereco,dataDeNascimento) values('{}', '{}','{}', '{}', '{}', '{}')".format(cpf,nome,senha,telefone,endereco,dataDeNascimento)
        con.execute(sql)
        db_connection.commit()
        return  "Cadastrado Com Sucesso"
    except Exception as erro:
        return erro 
        
def consultar(CPF):
    try:
        sql = "select * from cliente where CPF = '{}'".format(CPF)
        con.execute(sql)

        this.msg = ""
        this.msg = "Nenhum dado Encontrado!"
        for(CPF, nome, senha, telefone, endereco, dataDeNascimento) in con:
            if int(CPF) == int(CPF):
                this.msg = "CPF: {} Nome: {}, Senha: {}, Telefone: {}, Endereço: {}, Data de Nascimento: {}".format(CPF,nome, senha, telefone, endereco, dataDeNascimento)
                return this.msg
        return this.msg
    except Exception as erro:
        this.msg = ""
        return erro
def atualizar(CPF, campo, novoDado):
    try:
        sql = "update cliente set {} = '{}' where CPF = '{}'".format(campo, novoDado, CPF)
        con.execute(sql)
        db_connection.commit()
        return "Atualizado com Sucesso!".format(con.rowcount)
    except Exception as erro:
        return erro
def excluir(CPF):
    try:
        sql = "delete from cliente where CPF = '{}'".format(CPF)
        con.execute(sql)
        db_connection.commit()
        return "Deletado com Sucesso!".format(con.rowcount)
    except Exception as erro:
        return erro
def Login():
    try:
        sql = "select senha from cliente where cpf = '{}';".format(this.cpf)
        con.execute(sql)  # prepara o comando para ser executado

        for (senha) in con:
            print(senha[0])
            if this.senha == senha[0]:
                print("Login Efetuado com sucesso")
    except Exception as erro:
        print(erro)
