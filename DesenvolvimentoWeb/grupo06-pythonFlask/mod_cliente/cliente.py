from flask import Blueprint, render_template

bp_cliente = Blueprint('cliente', __name__, template_folder='templates')

@bp_cliente.route("/cliente", methods=['GET'])
def formCliente():
    return render_template("formCliente.html")