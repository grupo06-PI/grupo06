from flask import Blueprint, render_template

bp_comanda = Blueprint('comanda', __name__, template_folder='templates', url_prefix='/comandas')

@bp_comanda.route("/cadComanda", methods=['GET'])
def formComanda():
    return render_template("formComanda.html")