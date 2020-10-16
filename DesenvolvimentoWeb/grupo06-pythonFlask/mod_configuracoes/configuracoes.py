from flask import Blueprint, render_template

bp_configuracoes = Blueprint('configuracoes', __name__, template_folder='templates')

@bp_configuracoes.route("/Configuracoes", methods=['GET'])
def formConfiguracoes():
    return render_template("formConfiguracoes.html")