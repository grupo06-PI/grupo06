from flask import Blueprint, render_template, redirect, request, url_for, flash, jsonify, session

from mod_configuracoes.configuracoesBD import Configuracoes

from mod_login.login import validaSessao

from funcoes import Funcoes

bp_configuracoes = Blueprint('configuracoes', __name__, template_folder='templates')

@bp_configuracoes.route("/Configuracoes", methods=['GET','POST'])
@validaSessao
def formConfiguracoes():
    configuracoes = Configuracoes()
    return render_template("formConfiguracoes.html", configuracoes=configuracoes, content_type='application/json')


@bp_configuracoes.route("/listaConfiguracoes", methods=['GET','POST'])
@validaSessao
def ListaConfiguracoes():
    configuracoes = Configuracoes()
    res = configuracoes.SelectALL()
    return render_template("formListaConfiguracoes.html", result=res, content_type='application/json')

@bp_configuracoes.route('/formEditConfiguracoes', methods=['POST'])
@validaSessao
def formEditConfiguracoes():
    configuracoes=Configuracoes()
    configuracoes.selectONE()
    return render_template('formConfiguracoes.html', configuracoes=configuracoes, content_type='application/json')


@bp_configuracoes.route('/editConfiguracoes', methods=['POST'])
@validaSessao
def editConfiguracoes():
    _msg = ""
    funcoes = Funcoes()
    try:

        configuracoes = Configuracoes()
        configuracoes.taxa_juro_diario = request.form['taxa_juro_diario']
        configuracoes.multa_atraso = request.form['multa_atraso']
      
        _msg = configuracoes.update()

        #log
        log = _msg  + "|Usuário:" + session['usuario'] + "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = _msg  +"|Usuário:" + session['usuario'] + "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)