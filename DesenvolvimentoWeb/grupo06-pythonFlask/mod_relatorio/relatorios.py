from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session, json
from mod_login.login import validaSessao

bp_relatorios = Blueprint('relatorios', __name__, template_folder='templates', url_prefix="/relatorios")

@bp_relatorios.route("/relatorios", methods=['GET'])
@validaSessao
def Relatorios():
    return render_template("relatorios.html", content_type='application/json')