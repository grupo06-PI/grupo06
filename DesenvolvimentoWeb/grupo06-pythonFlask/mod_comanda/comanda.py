from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from mod_comanda.comandaBD import Comandas
from mod_comanda.comandaBD import ComandaRecebimento
from mod_produto.produtoBD import ProdutosComandas
from mod_cliente.clienteBD import Clientes
from GeraPdf import PDF
from flask import send_file
from mod_login.login import validaSessao
from funcoes import Funcoes
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
    funcoes = Funcoes()
    try:
        comanda=Comandas()

        comanda.id_comanda = request.form['id_comanda']
        comanda.numero_comanda = request.form['numero_comanda']
        comanda.data_hora = datetime.datetime.now()
        comanda.status_comanda = 0
        comanda.status_pagamento = 0
        comanda.funcionario_id = session['id_funcionario']
        comanda.cliente_id = 1

        _msg = comanda.insert()
        
        #log
        log = _msg  +"|Comanda:"+ request.form['numero_comanda'] +"|Usuário:" + session['usuario'] + "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_excpetion = e.args

        #log
        log = _msg +"|Usuário:" + session['usuario'] + "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_excpetion)


@bp_comanda.route('/deleteComanda', methods=['POST'])
@validaSessao
def deleteComanda():
    _msg = ""
    funcoes = Funcoes()
    try:
        comanda = Comandas()
        comanda.id_comanda = request.form['id_comanda']

        _msg = comanda.delete()

        #log
        log = _msg  +"|ID Comanda:"+ request.form['id_comanda'] +"|Usuário:" + session['usuario'] + "|"
        funcoes.logInfo(log)

        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_exception = e.args

        #log
        log = _msg +"|Usuário:" + session['usuario'] + "|"
        funcoes.logError(log)

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_exception)


@bp_comanda.route("/Recebimento", methods=['GET','POST'])
@validaSessao
def Recebimento():

    produtosComandas=ProdutosComandas()
    comanda=Comandas()
    comanda.id_comanda = request.form['id_comanda']
    comanda.selectONE()
    produtosComandas.comanda_id = request.values['id_comanda']
    comandaRecebimento = ComandaRecebimento()
    
    subTotalComandas = produtosComandas.selectALLSubTotal()
    return render_template("formRecebimentoAVista.html", comanda=comanda, comandaRecebimento=comandaRecebimento, subTotalComandas=subTotalComandas, content_type='application/json')


@bp_comanda.route("/finalizarRecebimento", methods=['GET','POST'])
@validaSessao
def finalizarRecebimento():
    _msg = ""
    funcoes = Funcoes()
    try:
        if request.form['tipo_recebimento'] == "1":
            
            #inserindo na TB_RECEBIMENTO
            comandaRecebimento = ComandaRecebimento()
            comandaRecebimento.data_hora = datetime.datetime.now()
            comandaRecebimento.tipo = 1 #a vista 1
            comandaRecebimento.valor_acrescimo = request.form['valor_acrescimo']
            comandaRecebimento.valor_desconto = request.form['valor_desconto']
            comandaRecebimento.valor_total  = request.form['subtotal']
            comandaRecebimento.funcionario_id = session['id_funcionario']
            comandaRecebimento.insert()

            ultimoId = comandaRecebimento.pegarLastrowid()

             #insert tb_comanda recebimento
            comandaRecebimento.id_comanda = request.form['id_comanda']
            comandaRecebimento.recebimento_id = ultimoId
            comandaRecebimento.insertTbComandaRecebimento()

            #update status comanda e pagamento tb_comanda
            comandaRecebimento.id_comanda = request.form['id_comanda']
            _msg = comandaRecebimento.updateTbComandaAVista()
        
        else:
            comandaRecebimento = ComandaRecebimento()
            cliente=Clientes()

            cliente.cpf = request.form['cpf']
            cliente.senha = request.form['senha']

            cliente.selectLogin()

            if cliente.id_cliente > 0:
                #update status comanda e pagamento tb_comanda
                comandaRecebimento.id_comanda = request.form['id_comanda']
                _msg = comandaRecebimento.updateTbComandaFiado()
            
            else:
                _msg = "Dados do Cliente Incorretos"
                return jsonify(erro=True, mensagem=_msg)

        
        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_excpetion = e.args

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_excpetion)


@bp_comanda.route("/RecebimentoFiadosAVista", methods=['GET','POST'])
@validaSessao
def RecebimentoFiadosAVista():

    produtosComandas=ProdutosComandas()
    comanda=Comandas()
    comanda.id_comanda = request.form['id_comanda']
    comanda.selectONE()
    produtosComandas.comanda_id = request.values['id_comanda']
    comandaRecebimento = ComandaRecebimento()
    
    subTotalComandas = produtosComandas.selectALLSubTotal()
    return render_template("formRecebimentosFiadosAVista.html", comanda=comanda, comandaRecebimento=comandaRecebimento, subTotalComandas=subTotalComandas, content_type='application/json')

@bp_comanda.route("/finalizarRecebimentoFiado", methods=['GET','POST'])
@validaSessao
def finalizarRecebimentoFiado():
    _msg = ""
    funcoes = Funcoes()
    try:

        
        #inserindo na TB_RECEBIMENTO
        comandaRecebimento = ComandaRecebimento()
        comandaRecebimento.data_hora = datetime.datetime.now()
        comandaRecebimento.tipo = 2 #fiado
        comandaRecebimento.valor_acrescimo = request.form['valor_acrescimo']
        comandaRecebimento.valor_desconto = request.form['valor_desconto']
        comandaRecebimento.valor_total  = request.form['subtotal']
        comandaRecebimento.funcionario_id = session['id_funcionario']
        comandaRecebimento.insert()

        ultimoId = comandaRecebimento.pegarLastrowid()

        #insert tb_comanda recebimento
        comandaRecebimento.id_comanda = request.form['id_comanda']
        comandaRecebimento.recebimento_id = ultimoId
        comandaRecebimento.insertTbComandaRecebimento()

            #update status comanda e pagamento tb_comanda
        comandaRecebimento.id_comanda = request.form['id_comanda']
        _msg = comandaRecebimento.updateTbComandaFiadoPaga()
        


        
        return jsonify(erro=False, mensagem=_msg)

    except Exception as e:
        _msg, _msg_excpetion = e.args

        return jsonify(erro=True, mensagem=_msg, mensagem_exception=_msg_excpetion)

@bp_comanda.route("/formRecebimentosFiados", methods=['GET','POST'])
@validaSessao
def formRecebimentosFiados():

    clientes=Clientes()
    listaClientes = clientes.selectALLClientes()
    return render_template("formRecebimentosFiados.html",listaClientes=listaClientes,clientes=clientes,content_type='application/json')

@bp_comanda.route("/RecebimentosFiados", methods=['GET','POST'])
@validaSessao
def RecebimentosFiados():
    clientes=Clientes()
    comandaRecebimento=ComandaRecebimento()
    listaClientes = clientes.selectALLClientes()
    comandaRecebimento.id_cliente = request.form['id_cliente' ]
    res = comandaRecebimento.selectONEComandasFiados()  

    return render_template("formRecebimentosFiados.html",result=res,listaClientes=listaClientes, content_type='application/json')

@bp_comanda.route('/buscaCliente', methods = ['POST'])
@validaSessao
def buscaCliente():

    try:
        cliente=Clientes()
        cliente.id_cliente = request.form['id_cliente']
        cliente.selectONE()

        clienteJson = cliente.toJSON()
        
        return jsonify(error=False, cliente=clienteJson)

    except Exception as e:
        return jsonify(erro=True, mensagem_exception = str(e))


@bp_comanda.route('/pdfComandasAtrasadas', methods=['POST'])
@validaSessao
def pdfComandasAtrasadas():
    geraPdf = PDF()
    geraPdf.pdfComandasAtrasadas()
    return send_file('pdfComandasAtrasadas.pdf', attachment_filename='pdfComandasAtrasadas.pdf')

@bp_comanda.route('/pdfRecebimentoAVista', methods=['POST'])
@validaSessao
def pdfRecebimentoAVista():
    geraPdf = PDF()
    geraPdf.pdfRecebimentoAVista()
    return send_file('pdfRecebimentoAVista.pdf', attachment_filename='pdfRecebimentoAVista.pdf')

@bp_comanda.route('/pdfRecebimentoFiado', methods=['POST'])
@validaSessao
def pdfRecebimentoFiado():
    geraPdf = PDF()
    geraPdf.pdfRecebimentoFiado()
    return send_file('pdfRecebimentoFiado.pdf', attachment_filename='pdfRecebimentoFiado.pdf')

    
