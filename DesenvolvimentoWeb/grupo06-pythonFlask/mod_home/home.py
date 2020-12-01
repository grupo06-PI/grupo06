from flask import Blueprint, render_template

from mod_login.login import validaSessao

bp_home = Blueprint('home', __name__, template_folder='templates')

@bp_home.route("/home", methods=['GET'])
@validaSessao
def formHome():
    return render_template("formHome.html")

@bp_home.route("/homeCliente", methods=['GET'])
@validaSessao
def formHomeCliente():
    return render_template("formHomeCliente.html")