from flask import Blueprint, render_template

bp_produto = Blueprint('produto', __name__, template_folder='templates', url_prefix='/produtos')

@bp_produto.route("/cadProduto", methods=['GET'])
def CadProduto():
    return render_template("formProduto.html")


@bp_produto.route("/listaProdutos", methods=['GET'])
def ListaProdutos():
    return render_template("formListaProdutos.html")