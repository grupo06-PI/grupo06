from flask import Flask

#importando Blueprints
from mod_home.home import bp_home
from mod_funcionario.funcionario import bp_funcionario
from mod_cliente.cliente import bp_cliente
from mod_produto.produto import bp_produto
from mod_comanda.comanda import bp_comanda
from mod_configuracoes.configuracoes import bp_configuracoes
from mod_dashboard.dashboard import bp_dashboard


app = Flask(__name__)

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

if __name__ == "__main__":
    app.run()