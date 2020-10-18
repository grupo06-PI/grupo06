from flask import Blueprint, render_template

bp_dashboard = Blueprint('dashboard', __name__, template_folder='templates', url_prefix="/dashboard")

@bp_dashboard.route("/ComandasAbertas", methods=['GET'])
def ComandasAbertas():
    return render_template("formComandasAbertas.html")

@bp_dashboard.route("/RegistroFiados", methods=['GET'])
def RegistroFiados():
    return render_template("formRegistroFiados.html")