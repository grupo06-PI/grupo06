from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from mod_cliente.clienteBD import Clientes
from mod_comanda.comandaBD import ComandaRecebimento
from mod_comanda.comandaBD import Comandas
from mod_produto.produtoBD import ProdutosComandas
from mod_login.login import validaSessao
from funcoes import Funcoes
from GeraPdf import PDF
from flask import send_file

bp_cliente = Blueprint('cliente', __name__, template_folder='templates', url_prefix='/clientes')

@bp_cliente.route("/cadCliente", methods=['GET','POST'])
@validaSessao
def CadCliente():

    cliente=Clientes()
    return render_template("formCliente.html", cliente=cliente, content_type='application/json')


@bp_cliente.route("/listaClientes", methods=['GET','POST'])
@validaSessao
def ListaClientes():

    cliente=Clientes()
    res = cliente.selectALL()
    return render_template("formListaClientes.html", result=res, content_type='application/json')


@bp_cliente.route("/formEditCliente", methods=['POST'])
@validaSessao
def formEditCliente():

    cliente=Clientes()
    cliente.id_cliente = request.form['id_cliente']
    cliente.selectONE()
    return render_template('formCliente.html', cliente=cliente, content_type='application/json')


@bp_cliente.route('/addCliente', methods=['GET','POST'])
@validaSessao
def addCliente():
    _msg = ""
    funcoes = Funcoes()
    try:
        cliente=Clientes()

        cliente.id_cliente = request.form['id_cliente']
        cliente.nome = request.form['nome']
        cliente.cpf = request.form['cpf'].replace('.','').replace('-','')
        cliente.telefone = request.form['telefone'].replace('(','').replace(')','').replace(' ','').replace('-','')
        cliente.compra_fiado = request.form['compra_fiado']
        cliente.dia_fiado = request.form['dia_fiado'].replace('/','')
        cliente.senha = funcoes.encrypt(request.form['senha']) 

        _msg = cliente.insert()

        #log
        log = _msg  +"|CPF:"+ request.form['cpf'] +"|Usuário:" + session['usuario'] + "|"
        funcoes.logInfo(log)
        
        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_excpetion = e.args

        #log
        log = _msg  +"|Usuário:" + session['usuario'] + "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_excpetion)
    

@bp_cliente.route('/editCliente', methods=['POST'])
@validaSessao
def editCliente():
    _msg = ""
    funcoes = Funcoes()
    try:

        cliente=Clientes()

        cliente.id_cliente = request.form['id_cliente']
        cliente.nome = request.form['nome']
        cliente.cpf = request.form['cpf'].replace('.','').replace('-','')
        cliente.telefone = request.form['telefone'].replace('(','').replace(')','').replace(' ','').replace('-','')
        cliente.compra_fiado = request.form['compra_fiado']
        cliente.dia_fiado = request.form['dia_fiado'].replace('/','')
        cliente.senha = funcoes.encrypt(request.form['senha'])   

        _msg = cliente.update()

        #log
        log = _msg  +"|ID:"+ request.form['id_cliente'] + session['usuario'] + "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = _msg  +"|Usuário:" + session['usuario'] + "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)

@bp_cliente.route('/deleteCliente', methods=['POST'])
@validaSessao
def deleteCliente():
    _msg = ""
    funcoes = Funcoes()
    try:

        cliente = Clientes()
        cliente.id_cliente = request.form['id_cliente']

        _msg = cliente.delete()

        #log
        log = _msg  +"|ID:"+ request.form['id_cliente'] + session['usuario'] + "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = _msg  +"|Usuário:" + session['usuario'] + "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)

@bp_cliente.route('/pdfCliente', methods=['POST'])
@validaSessao
def pdfCliente():
    geraPdf = PDF()
    geraPdf.pdfClientes()
    return send_file('pdfClientes.pdf', attachment_filename='pdfClientes.pdf')


@bp_cliente.route('/listaProdComanda', methods = ['POST'])
@validaSessao
def listaProdComanda():
    comandaRecebimento = ComandaRecebimento()
    comanda=Comandas()
    produtosComandas = ProdutosComandas()
    comanda.comanda_id = request.values['comanda_id']
    comanda.cliente_id = int(session['id_cliente'])
    listaProdComandas = comanda.selectALLCliente()
    subTotalComandas = produtosComandas.selectALLSubTotal()
    return render_template("formListaProdComandaCliente.html", comanda=comanda, listaProdComandas=listaProdComandas, subTotalComandas=subTotalComandas, content_type='application/json')