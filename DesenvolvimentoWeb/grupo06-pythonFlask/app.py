from flask import Flask
from flask import send_from_directory
from flask import session
import logging

#encerrar sessão por inatividade
from datetime import timedelta

#gerador randomico de chave
import os

#importando Blueprints
from mod_home.home import bp_home
from mod_funcionario.funcionario import bp_funcionario
from mod_cliente.cliente import bp_cliente
from mod_produto.produto import bp_produto
from mod_comanda.comanda import bp_comanda
from mod_configuracoes.configuracoes import bp_configuracoes
from mod_dashboard.dashboard import bp_dashboard
from mod_login.login import bp_login

#Log
logging.basicConfig(filename='log/app.log', format= '%(levelname)s|%(name)s|%(asctime)s|%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.DEBUG)

app = Flask(__name__)

#gerador randÔmico de chaves para a session
app.secret_key = os.urandom(12).hex()

#mod_home
app.register_blueprint(bp_home)

#mod_funcionario
app.register_blueprint(bp_funcionario)

#mod_cliente
app.register_blueprint(bp_cliente)

#mod_produto
app.register_blueprint(bp_produto)

#mod_comanda
app.register_blueprint(bp_comanda)

#mod_configuracoes
app.register_blueprint(bp_configuracoes)

#mod_dashboard
app.register_blueprint(bp_dashboard)

#mod_login
app.register_blueprint(bp_login)

#encerrando a sessao por inatividade
@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)

if __name__ == "__main__":
    app.run()