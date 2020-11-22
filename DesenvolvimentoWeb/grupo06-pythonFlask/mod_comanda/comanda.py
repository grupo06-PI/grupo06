from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session

from mod_comanda.comandaBD import Comandas

from mod_login.login import validaSessao

import datetime

bp_comanda = Blueprint('comanda', __name__, template_folder='templates', url_prefix='/comandas')


@bp_comanda.route("/AbrirComanda", methods=['GET','POST'])
@validaSessao
def AbrirComanda():
    
    comanda=Comandas()
    return render_template("formComanda.html", comanda=comanda, content_type='application/json')


@bp_comanda.route("/ListaComandas", methods=['GET','POST'])
@validaSessao
def ListaComandas():
    comanda=Comandas()
    res = comanda.selectALL()
    return render_template("formListaComandas.html", result=res, content_type='application/json')
    


@bp_comanda.route("/abrirComanda", methods=['GET','POST'])
@validaSessao
def abrirComanda():
    _msg = ""

    try:
        comanda=Comandas()

        comanda.id_comanda = request.form['id_comanda']
        comanda.numero_comanda = request.form['numero_comanda']
        comanda.data_hora = datetime.datetime.now()
        comanda.status_comanda = request.form['status_comanda']
        comanda.status_pagamento = request.form['status_pagamento']
        comanda.funcionario_id = session['id_funcionario']

        _msg = comanda.insert()
        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_excpetion = e.args
        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_excpetion)


@bp_comanda.route('/deleteComanda', methods=['POST'])
@validaSessao
def deleteComanda():
    _msg = ""
    try:
        comanda = Comandas()
        comanda.id_comanda = request.form['id_comanda']

        _msg = comanda.delete()

        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_exception = e.args
        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)
    
