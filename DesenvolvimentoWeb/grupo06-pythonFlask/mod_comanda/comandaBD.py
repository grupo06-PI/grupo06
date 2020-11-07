from BancoBD import Banco

class Comandas(object):

    def __init__(self, id_comanda=0, numero_comanda="", data_hora="", status_comanda="", status_pagamento="", funcionario_id="", cliente_id=""):

        self.id_comanda = id_comanda
        self.numero_comanda = numero_comanda
        self.data_hora = data_hora
        self.status_comanda = status_comanda
        self.status_pagamento = status_pagamento
        self.funcionario_id = funcionario_id
        self.cliente_id = cliente_id

    def selectALL(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "select id_comanda, numero_comanda, data_hora, status_comanda, status_pagamento, funcionario_id, cliente_id from tb_comanda"

            _sql_data = ()

            c.execute(_sql, _sql_data)

            result = c.fetchall()

            return result

        except Exception as e:
            return "Ocorreu um erro na busca das Comandas"

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def insert(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "insert into tb_comanda(numero_comanda,data_hora,status_comanda,status_pagamento,funcionario_id) values (%s,%s,%s,%s,%s)"

            _sql_data = (self.numero_comanda, self.data_hora, self.status_comanda,
                         self.status_pagamento, self.funcionario_id,)

            c.execute(_sql, _sql_data)

            banco.conexao.commit()

            return "Comanda Aberto com Sucesso!"

        except Exception as e:
            raise Exception('Erro ao Abrir Comanda!', str(e))
        finally:
            if c:
                c.close
            if banco:
                banco.conexao.close()

    def delete(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "delete from tb_comanda where id_comanda = %s"
            _sql_data = (self.id_comanda,)

            c.execute(_sql,_sql_data)

            banco.conexao.commit()

            return "Comanda excluída com sucesso!"

        except Exception as e:
            raise Exception("Erro ao tentar excluir comanda!", str(e))
        
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()
