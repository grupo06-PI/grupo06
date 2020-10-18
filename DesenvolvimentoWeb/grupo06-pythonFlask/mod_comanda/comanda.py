from flask import Blueprint, render_template

bp_comanda = Blueprint('comanda', __name__, template_folder='templates', url_prefix='/comandas')

@bp_comanda.route("/AbrirComanda", methods=['GET'])
def AbrirComanda():
    return render_template("formComanda.html")