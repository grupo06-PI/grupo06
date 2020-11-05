from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

from mod_cliente.clienteBD import Clientes

from mod_login.login import validaSessao

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

    try:
        cliente=Clientes()

        cliente.id_cliente = request.form['id_cliente']
        cliente.nome = request.form['nome']
        cliente.cpf = request.form['cpf']
        cliente.telefone = request.form['telefone']
        cliente.compra_fiado = request.form['compra_fiado']
        cliente.dia_fiado = request.form['dia_fiado']
        cliente.senha = request.form['senha']   

        _msg = cliente.insert()
        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_excpetion = e.args
        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_excpetion)
    

@bp_cliente.route('/editCliente', methods=['POST'])
@validaSessao
def editCliente():
    _msg = ""

    try:

        cliente=Clientes()

        cliente.id_cliente = request.form['id_cliente']
        cliente.nome = request.form['nome']
        cliente.cpf = request.form['cpf']
        cliente.telefone = request.form['telefone']
        cliente.compra_fiado = request.form['compra_fiado']
        cliente.dia_fiado = request.form['dia_fiado']
        cliente.senha = request.form['senha']   

        _msg = cliente.update()
        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_exception = e.args
        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)

@bp_cliente.route('/deleteCliente', methods=['POST'])
@validaSessao
def deleteCliente():
    _msg = ""
    try:

        cliente = Clientes()
        cliente.id_cliente = request.form['id_cliente']

        _msg = cliente.delete()

        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_exception = e.args
        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)
    