from flask import Blueprint, render_template

bp_comanda = Blueprint('comanda', __name__, template_folder='templates')

@bp_comanda.route("/comanda", methods=['GET'])
def formComanda():
    return render_template("formComanda.html")