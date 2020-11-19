from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session

from mod_comanda.comandaBD import Comandas
from mod_comanda.comandaBD import ComandaAddProd
from mod_produto.produtoBD import Produtos

from mod_login.login import validaSessao

bp_dashboard = Blueprint('dashboard', __name__, template_folder='templates', url_prefix="/dashboard")

@bp_dashboard.route("/ComandasAbertas", methods=['GET'])
@validaSessao
def ComandasAbertas():
    comanda=Comandas()
    res = comanda.selectALL()
    return render_template("formComandasAbertas.html", result=res, content_type='application/json')

@bp_dashboard.route("/RegistroFiados", methods=['GET'])
@validaSessao
def RegistroFiados():
    return render_template("formRegistroFiados.html")


@bp_dashboard.route("/AdicionarProdutos", methods=['GET','POST'])
@validaSessao
def AdicionarProdutos():
    comandaAdd = ComandaAddProd()
    return render_template("formAddProdutos.html", comandaAdd=comandaAdd, content_type='application/json')


@bp_dashboard.route('/formEditComanda', methods=['POST'])
@validaSessao
def formEditComanda():
    comanda=Comandas()
    comanda.id_comanda = request.form['id_comanda']
    comanda.selectONE()
    return render_template('formAddProdutos.html', comanda=comanda, content_type='application/json')


@bp_dashboard.route('/addProdutoComanda', methods=['POST'])
@validaSessao
def addProdutoComanda():
    _msg = ""
    
    try:
        
        comandaAdd = ComandaAddProd()
        comanda = Comandas()
        comandaAdd.quantidade = request.form['quantidade']
        comandaAdd.valor_unitario = request.form['valor_unitario']
        comandaAdd.comanda_id = request.form['comanda_id']
        comandaAdd.produto_id = request.form['produto_id']
        comandaAdd.funcionario_id = session['id_funcionario']

        _msg = comandaAdd.insert()
        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_excpetion = e.args
        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_excpetion)

@bp_dashboard.route('/listaProdutos', methods = ['POST'])
@validaSessao
def listaProdutos():
    produto=Produtos()
    produto.nome = request.form['nome']
    produto.valor_unitario = request.form['valor_unitario']

    try:
        result = produto.listaProdutos()
        return jsonify(produto_existe=True)

    except Exception as e:
        return jsonify(erro = True, mensagem_exception = str(e))