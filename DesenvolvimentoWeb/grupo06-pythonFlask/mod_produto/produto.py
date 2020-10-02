from flask import Blueprint, render_template

bp_produto = Blueprint('produto', __name__, template_folder='templates')

@bp_produto.route("/produto", methods=['GET'])
def formProduto():
    return render_template("formProduto.html")