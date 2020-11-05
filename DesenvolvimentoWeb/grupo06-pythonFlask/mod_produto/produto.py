from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
import base64

from mod_produto.produtoBD import Produtos

from mod_login.login import validaSessao

bp_produto = Blueprint('produto', __name__, template_folder='templates', url_prefix='/produtos')

@bp_produto.route("/cadProduto", methods=['GET','POST'])
@validaSessao
def CadProduto():
    produto = Produtos()
    return render_template('formProduto.html', produto=produto, content_type='application/json')


@bp_produto.route("/listaProdutos", methods=['GET','POST'])
@validaSessao
def ListaProdutos():
    produto = Produtos()
    res = produto.selectALL()
    return render_template('formListaProdutos.html', result=res, content_type='application/json')

@bp_produto.route('/formEditProduto', methods=['POST'])
@validaSessao
def formEditProduto():
    produto = Produtos()
    produto.id_produto = request.form['id_produto']
    produto.selectONE()
    return render_template('formProduto.html', produto=produto, content_type='application/json')

@bp_produto.route('/addProduto', methods=['POST'])
@validaSessao
def addProduto():
    _msg = ""
    try:
        produto = Produtos()
        produto.id_produto = request.form['id_produto']
        produto.nome = request.form['nome']
        produto.descricao = request.form['descricao']
        produto.valor_unitario = request.form['valor_unitario']
        produto.foto = "data:" + request.files['foto'].content_type + ";base64," +str(base64.b64encode(request.files['foto'].read()), "utf-8")

        _msg = produto.insert()
        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_exception = e.args
        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)

@bp_produto.route('/editProduto', methods=['POST'])
@validaSessao
def editProduto():
    _msg = ""
    try:

        produto = Produtos()
        produto.id_produto = request.form['id_produto']
        produto.nome = request.form['nome']
        produto.descricao = request.form['descricao']
        produto.valor_unitario = request.form['valor_unitario']
        produto.foto = "data:" + request.files['foto'].content_type + ";base64," +str(base64.b64encode(request.files['foto'].read()), "utf-8")

        _msg = produto.update()
        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_exception = e.args
        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)

@bp_produto.route('/deleteProduto', methods=['POST'])
@validaSessao
def deleteProduto():
    _msg = ""
    try:

        produto = Produtos()
        produto.id_produto = request.form['id_produto']

        _msg = produto.delete()

        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_exception = e.args
        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)