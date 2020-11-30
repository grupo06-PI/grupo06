from flask import Blueprint, render_template, request, redirect, url_for, session

#utilizado para copiar as informações da função original
from functools import wraps

#import funcionarios
from mod_funcionario.funcionarioBD import Funcionarios

from funcoes import Funcoes


bp_login = Blueprint('login', __name__, template_folder='templates')



@bp_login.route("/")
def login():
    return render_template("formLogin.html")

#rota ajustada para validação de login
@bp_login.route("/login", methods=['POST'])
def validaLogin():
    #cria objeto funcoes para armazenar log
    funcoes = Funcoes()

    #cria o objeto e armezena usuário e senha digitado
    funcionario = Funcionarios()

    funcionario.cpf = request.form['cpf']
    funcionario.senha = request.form['senha']  #funcoes.encrypt(request.form['senha']) 

    #realiza a busca pelo usuário e armazena o resultado no objeto
    funcionario.selectLogin()

    #verifica se o usuário foi encontrado
    if funcionario.id_funcionario > 0:
        #limpa a sessão
        session.clear()

        #registra o usuário na sessão, armazenando o login do usuário
        session['usuario'] = funcionario.nome
        session['cpf'] = funcionario.cpf
        session['grupo'] = funcionario.grupo
        session['id_funcionario'] = funcionario.id_funcionario

        #log
        log = "Login Efetuado com sucesso" + "|Usuário:" + session['usuario']+ "|"
        funcoes.logInfo(log)

        #abre a aplicação na tela home
        return redirect(url_for('home.formHome'))

    else:
        #log
        log = "Tentativa de Login" + "|Usuário:" + request.form['cpf'] + "|"
        funcoes.logWarning(log)

        #retornna para a tela de login
        return redirect(url_for('login.login', falhaLogin=1))


#rota de log-out, para exibir mensagem de erro
@bp_login.route("/logout")
def logout ():
    #cria objeto funcoes para armazenar log
    funcoes = Funcoes()

    #log
    log = "Logout efetuado" + "|Usuário:" + session['usuario']+ "|"
    funcoes.logInfo(log)

    session.pop('usuario',None)

    #poderiamos limpar toda a sessão utiliazando session.clear()
    return redirect (url_for('login.login', falhaSessao=2))


# valida se o usuário esta ativo na sessão
def validaSessao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            
            #descarta os dados copiados da função original e retorna a tela de login
            return redirect(url_for('login.login',falhaSessao=1))
        else:
            #retorna os dados copiados da função original
            return f(*args, **kwargs)

    #retorna o resultado do if acima
    return decorated_function
