from flask import Blueprint, render_template

bp_dashboard = Blueprint('dashboard', __name__, template_folder='templates', url_prefix="/dashboard")

@bp_dashboard.route("/ComandasAbertas", methods=['GET'])
def formComandasAbertas():
    return render_template("formComandasAbertas.html")

@bp_dashboard.route("/RegistroFiados", methods=['GET'])
def formRegistroFiados():
    return render_template("formRegistroFiados.html")