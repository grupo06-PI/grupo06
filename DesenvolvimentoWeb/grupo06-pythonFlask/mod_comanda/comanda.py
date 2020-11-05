from flask import Blueprint, render_template

from mod_login.login import validaSessao

bp_comanda = Blueprint('comanda', __name__, template_folder='templates', url_prefix='/comandas')

@bp_comanda.route("/AbrirComanda", methods=['GET'])
@validaSessao
def AbrirComanda():
    return render_template("formComanda.html")