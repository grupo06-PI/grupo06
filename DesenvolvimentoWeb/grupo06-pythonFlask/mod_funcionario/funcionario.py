from flask import Blueprint, render_template

bp_funcionario = Blueprint('funcionario', __name__, template_folder='templates')

@bp_funcionario.route("/funcionario", methods=['GET'])
def formFuncionario():
    return render_template("formFuncionario.html")