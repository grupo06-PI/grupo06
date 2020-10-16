from flask import Blueprint, render_template

bp_cliente = Blueprint('cliente', __name__, template_folder='templates', url_prefix='/clientes')

@bp_cliente.route("/cadCliente", methods=['GET'])
def CadCliente():
    return render_template("formCliente.html")


@bp_cliente.route("/listaClientes", methods=['GET'])
def ListaClientes():
    return render_template("formListaClientes.html")
   