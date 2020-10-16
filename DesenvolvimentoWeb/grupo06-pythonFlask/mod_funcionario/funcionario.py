from flask import Blueprint, render_template

bp_funcionario = Blueprint('funcionario', __name__, template_folder='templates', url_prefix="/funcionarios")

@bp_funcionario.route("/cadFuncionario", methods=['GET'])
def CadFuncionario():
    return render_template("formFuncionario.html")


@bp_funcionario.route("/listaFuncionarios", methods=['GET'])
def ListaFuncionarios():
    return render_template("formListaFuncionarios.html")
