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

    def selectONE(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "select id_comanda, numero_comanda, data_hora, status_comanda, status_pagamento, funcionario_id, cliente_id from tb_comanda where id_comanda = %s"

            _sql_data = (self.id_comanda,)

            c.execute(_sql,_sql_data)

            for linha in c:
                self.id_comanda = linha[0]
                self.numero_comanda = linha[1]
                self.data_hora = linha[2]
                self.status_comanda = linha[3]
                self.status_pagamento = linha[4]
                self.funcionario_id = linha[5]
                self.cliente_id = linha[6]
                
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do produto"
            
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()


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


class ComandaAddProd(object):

    def __init__(self, id_comanda_produto=0, quantidade="", valor_unitario="", comanda_id="", produto_id="", funcionario_id=""):
        self.id_comanda_produto = id_comanda_produto
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.comanda_id = comanda_id
        self.produto_id = produto_id
        self.funcionario_id = funcionario_id

    def insert(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "insert into tb_comanda_produto(quantidade,valor_unitario,comanda_id,produto_id,funcionario_id) values (%s,%s,%s,%s,%s)"

            _sql_data = (self.quantidade, self.valor_unitario, self.comanda_id,
                         self.produto_id, self.funcionario_id,)

            c.execute(_sql, _sql_data)

            banco.conexao.commit()

            return "Produto adicionado com sucesso!"

        except Exception as e:
            raise Exception('Erro ao Abrir Comanda!', str(e))
        finally:
            if c:
                c.close
            if banco:
                banco.conexao.close()

    def update(self):
        banco = None
        c = None

        try:
            banco = Banco()
            
            c = banco.conexao.cursor()

            _sql = "update tb_comanda_produto set quantidade=%s,valor_unitario=%s,comanda_id=%s, produto_id=%s, funcionario_id=%s where id_comanda_produto = %s"

            _sql_data = (self.quantidade, self.valor_unitario, self.comanda_id, self.produto_id, self.funcionario_id,self.id_comanda_produto)

            c.execute(_sql,_sql_data)

            banco.conexao.commit()

            return "Produto Adicionado com Sucesso!"

        except Exception as e:
            raise Exception("Erro ao adicionar produto!", str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()


    def selectONE(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "select id_comanda, numero_comanda, data_hora, status_comanda, status_pagamento, funcionario_id, cliente_id from tb_comanda where id_comanda = %s"

            _sql_data = (self.id_comanda,)

            c.execute(_sql,_sql_data)

            for linha in c:
                self.id_comanda = linha[0]
                self.numero_comanda = linha[1]
                self.data_hora = linha[2]
                self.status_comanda = linha[3]
                self.status_pagamento = linha[4]
                self.funcionario_id = linha[5]
                self.cliente_id = linha[6]
                
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do produto"
            
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()