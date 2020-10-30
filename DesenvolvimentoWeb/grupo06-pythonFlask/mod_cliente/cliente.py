from flask import Blueprint, render_template, request, redirect, url_for, flash

from mod_cliente.clienteBD import Clientes

bp_cliente = Blueprint('cliente', __name__, template_folder='templates', url_prefix='/clientes')

@bp_cliente.route("/cadCliente", methods=['GET','POST'])
def CadCliente():

    cliente=Clientes()
    return render_template("formCliente.html", cliente=cliente, content_type='application/json')


@bp_cliente.route("/listaClientes", methods=['GET','POST'])
def ListaClientes():

    cliente=Clientes()
    res = cliente.selectALL()
    return render_template("formListaClientes.html", result=res, content_type='application/json')


@bp_cliente.route("/formEditCliente", methods=['POST'])
def formEditCliente():

    cliente=Clientes()
    cliente.id_cliente = request.form['id_cliente']
    cliente.selectONE()
    return render_template('formCliente.html', cliente=cliente, content_type='application/json')


@bp_cliente.route('/addCliente', methods=['GET','POST'])
def addCliente():

    cliente=Clientes()

    cliente.id_cliente = request.form['id_cliente']
    cliente.nome = request.form['nome']
    cliente.cpf = request.form['cpf']
    cliente.telefone = request.form['telefone']
    cliente.compra_fiado = request.form['compra_fiado']
    cliente.dia_fiado = request.form['dia_fiado']
    cliente.senha = request.form['senha']   

    cliente.insert()

    return redirect(url_for('cliente.ListaClientes'))

@bp_cliente.route('/editCliente', methods=['POST'])
def editCliente():

    cliente=Clientes()

    cliente.id_cliente = request.form['id_cliente']
    cliente.nome = request.form['nome']
    cliente.cpf = request.form['cpf']
    cliente.telefone = request.form['telefone']
    cliente.compra_fiado = request.form['compra_fiado']
    cliente.dia_fiado = request.form['dia_fiado']
    cliente.senha = request.form['senha']   
    

    if 'salvaEditaUsuarioDB' in request.form:
        cliente.update()

    elif 'salvaExcluiUsuarioDB' in request.form:
        cliente.delete()

    return redirect(url_for('cliente.ListaClientes'))