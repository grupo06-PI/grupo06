from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session, json

from mod_comanda.comandaBD import Comandas
from mod_comanda.comandaBD import ComandaAddProd
from mod_comanda.comandaBD import ComandaAddCliente
from mod_produto.produtoBD import Produtos
from mod_produto.produtoBD import ProdutosComandas
from mod_cliente.clienteBD import Clientes

from funcoes import Funcoes


from mod_login.login import validaSessao

bp_dashboard = Blueprint('dashboard', __name__, template_folder='templates', url_prefix="/dashboard")

@bp_dashboard.route("/ComandasAbertas", methods=['GET'])
@validaSessao
def ComandasAbertas():
    comanda=Comandas()
    res = comanda.selectALLDashboard()
    return render_template("formComandasAbertas.html", result=res, content_type='application/json')

@bp_dashboard.route("/ComandasAtrasadas", methods=['GET'])
@validaSessao
def ComandasAtrasadas():
    comanda=Comandas()
    res = comanda.selectALLComandasAtrasadas()
    return render_template("formComandasFiadoAtrasadas.html", result=res, content_type='application/json')

@bp_dashboard.route("/RegistroFiados", methods=['GET'])
@validaSessao
def RegistroFiados():
    return render_template("formRegistroFiados.html")


@bp_dashboard.route("/AdicionarProdutos", methods=['GET','POST'])
@validaSessao
def AdicionarProdutos():
    produto=Produtos()
    listaProd = produto.selectALL()
    comandaAddProd=ComandaAddProd()   
    comandaAddProd.comanda_id = request.form['comanda_id']
    comandaAddProd.selectONE()
    return render_template("formAddProdutos.html", listaProd=listaProd, comandaAddProd=comandaAddProd, content_type='application/json')

@bp_dashboard.route('/addProdutoComanda', methods=['POST'])
@validaSessao
def addProdutoComanda():
    _msg = ""
    funcoes = Funcoes()
    
    try:
        
        comandaAddProd = ComandaAddProd()
        comandaAddProd.quantidade = request.form['quantidade']
        comandaAddProd.valor_unitario = request.form['valor_unitario']
        comandaAddProd.comanda_id = request.form['comanda_id']
        comandaAddProd.produto_id = request.form['id_produto']
        comandaAddProd.funcionario_id = session['id_funcionario']

        _msg = comandaAddProd.insert()
        
        #log
        log = _msg  +"|ID Produto:"+ request.form['id_produto'] +"|Usuário:" + session['usuario'] + "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_excpetion = e.args

        #log
        log = _msg  +"|Usuário:" + session['usuario'] + "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_excpetion)


@bp_dashboard.route('/buscaProduto', methods = ['POST'])
@validaSessao
def buscaProduto():

    try:
        produto=Produtos()
        produto.id_produto = request.form['id_produto']
        produto.selectONE()

        produtoJson = produto.toJSON()
        return jsonify(error=False, produto=produtoJson)

    except Exception as e:
        return jsonify(erro=True, mensagem_exception = str(e))

@bp_dashboard.route('/listaProdComanda', methods = ['POST'])
@validaSessao
def listaProdComanda():
    produtosComandas=ProdutosComandas()
    produtosComandas.comanda_id = request.values['comanda_id']
    listaProdComandas = produtosComandas.selectALL()
    return render_template("formListaProdComanda.html", produtosComandas=ProdutosComandas, listaProdComandas=listaProdComandas, content_type='application/json')

@bp_dashboard.route('/deleteProdComanda', methods=['POST'])
@validaSessao
def deleteProdComanda():
    _msg = ""
    funcoes = Funcoes
    try:

        produtosComandas=ProdutosComandas()
        produtosComandas.id_comanda_produto = request.form['id_comanda_produto']

        _msg = produtosComandas.deleteProdComanda()

        #log
        log = _msg  +"|id_comanda_produto:"+ request.form['id_comanda_produto'] +"|Usuário:" + session['usuario'] + "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = _msg  +"|Usuário:" + session['usuario'] + "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)


@bp_dashboard.route("/AdicionarCliente", methods=['GET','POST'])
@validaSessao
def AdicionarCliente():
    clientes=Clientes()
    comandaAddCliente=ComandaAddCliente()
    comandaAddCliente.id_comanda = request.form['id_comanda']
    listaClientes = clientes.selectALLClientes()
    return render_template("formAddCliente.html", comandaAddCliente=comandaAddCliente, listaClientes=listaClientes, content_type='application/json')


@bp_dashboard.route('/addClienteComanda', methods=['GET','POST'])
@validaSessao
def addClienteComanda():
    _msg = ""
    funcoes = Funcoes()
    try:   
        comandaAddCliente = ComandaAddCliente()
        comandaAddCliente.cliente_id = request.form['id_cliente']
        comandaAddCliente.id_comanda = request.form['id_comanda']

        _msg = comandaAddCliente.update()

        #log
        log = _msg  +"|ID Comanda:"+ request.form['id_comanda']+"|ID Cliente:"+ request.form['id_cliente']+"|Usuário:" + session['usuario'] + "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_excpetion = e.args

        #log
        log = _msg  +"|Usuário:" + session['usuario'] + "|"
        funcoes.logError(log)
        
        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_excpetion)


@bp_dashboard.route("/Dashboard", methods=['GET'])
@validaSessao
def Dashboard():
    return render_template("formDashboard.html", content_type='application/json')