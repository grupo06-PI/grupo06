from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from mod_funcionario.funcionarioBD import Funcionarios
from mod_login.login import validaSessao
from funcoes import Funcoes
from GeraPdf import PDF
from flask import send_file


bp_funcionario = Blueprint('funcionario', __name__, template_folder='templates', url_prefix="/funcionarios")


@bp_funcionario.route("/cadFuncionario", methods=['GET', 'POST'])
@validaSessao
def CadFuncionario():
    funcionario = Funcionarios()
    return render_template("formFuncionario.html", funcionario=funcionario, content_type='application/json')


@bp_funcionario.route("/listaFuncionarios", methods=['GET', 'POST'])
@validaSessao
def ListaFuncionarios():
    funcionario = Funcionarios()
    res = funcionario.selectALL() 
    return render_template("formListaFuncionarios.html", funcionario=funcionario, result=res, content_type='application/json')


@bp_funcionario.route("/formEditFuncionario", methods=['POST'])
@validaSessao
def formEditFuncionario():

    funcionario = Funcionarios()
    funcionario.id_funcionario = request.form['id_funcionario']
    funcionario.selectONE()
    return render_template('formFuncionario.html', funcionario=funcionario, content_type='application/json')




@bp_funcionario.route("/addFuncionario", methods=['GET','POST'])
@validaSessao
def addFuncionario():
    funcoes = Funcoes()
    _msg = ""

    try:
        funcionario=Funcionarios()

        funcionario.id_funcionario = request.form['id_funcionario']
        funcionario.nome = request.form['nome']
        funcionario.matricula = request.form['matricula']
        funcionario.cpf = request.form['cpf']
        funcionario.telefone = request.form['telefone']
        funcionario.grupo = request.form['grupo']
        funcionario.senha = funcoes.encrypt(request.form['senha'])  
        _msg = funcionario.insert()
        
        #log
        log = _msg  +"|Matricula:"+ request.form['matricula'] +"|Usuário:" + session['usuario'] + "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_excpetion = e.args

        #log
        log = _msg  +"|Usuário:" + session['usuario'] + "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_excpetion)

@bp_funcionario.route("/editFuncionario", methods=['POST'])
@validaSessao
def editFuncionario():
        _msg = ""
        funcoes = Funcoes()
        try:
            funcionario=Funcionarios()

            funcionario.id_funcionario = request.form['id_funcionario']
            funcionario.nome = request.form['nome']
            funcionario.matricula = request.form['matricula']
            funcionario.cpf = request.form['cpf']
            funcionario.telefone = request.form['telefone']
            funcionario.grupo = request.form['grupo']
            funcionario.senha = funcoes.encrypt(request.form['senha'])

            _msg = funcionario.update()

            #log
            log = _msg  +"|ID:"+ request.form['id_funcionario'] +"|Usuário:" + session['usuario'] + "|"
            funcoes.logInfo(log)

            return jsonify(erro=False, mensagem=_msg)

        except Exception as e:
            _msg, _msg_excpetion = e.args

            #log
            log = _msg  +"|Usuário:" + session['usuario'] + "|"
            funcoes.logError(log)

            return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_excpetion)


@bp_funcionario.route("/deleteFuncionario", methods=['POST'])
@validaSessao
def deleteFuncionario():
    _msg = ""
    funcoes = Funcoes()
    try:

        funcionario = Funcionarios()
        funcionario.id_funcionario = request.form['id_funcionario']

        _msg = funcionario.delete()

        #log
        log = _msg  +"|ID:"+ request.form['id_funcionario'] +"|Usuário:" + session['usuario'] + "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = _msg  +"|Usuário:" + session['usuario'] + "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)

@bp_funcionario.route('/pdfFuncionario', methods=['POST'])
@validaSessao
def pdfFuncionarios():
    geraPdf = PDF()
    geraPdf.pdfFuncionarios()
    return send_file('pdfFuncionarios.pdf', attachment_filename='pdfFuncionarios.pdf')
