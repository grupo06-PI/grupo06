from flask import Blueprint, render_template

from mod_login.login import validaSessao

bp_dashboard = Blueprint('dashboard', __name__, template_folder='templates', url_prefix="/dashboard")

@bp_dashboard.route("/ComandasAbertas", methods=['GET'])
@validaSessao
def ComandasAbertas():
    return render_template("formComandasAbertas.html")

@bp_dashboard.route("/RegistroFiados", methods=['GET'])
@validaSessao
def RegistroFiados():
    return render_template("formRegistroFiados.html")