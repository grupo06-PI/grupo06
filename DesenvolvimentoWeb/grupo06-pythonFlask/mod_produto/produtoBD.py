from BancoBD import Banco

import json

class Produtos(object):

    def __init__(self, id_produto=0, nome="", descricao="", valor_unitario=0, foto=""):

        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.valor_unitario = valor_unitario
        self.foto = foto


    def selectALL(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "select id_produto, nome, descricao, valor_unitario, CONVERT(foto USING utf8) from tb_produto"

            _sql_data = ()

            c.execute(_sql,_sql_data)

            result = c.fetchall()

            return result

        except Exception as e:
            return "Ocorreu um erro na busca do produto"

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

            _sql = "select id_produto, nome, descricao, CONVERT(valor_unitario,CHAR), CONVERT(foto USING utf8) from tb_produto where id_produto = %s"

            _sql_data = (self.id_produto,)

            c.execute(_sql,_sql_data)

            for linha in c:
                self.id_produto = linha[0]
                self.nome = linha[1]
                self.descricao = linha[2]
                self.valor_unitario = linha[3]
                self.foto = linha[4]
                
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do produto"
            
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

            print(self.foto)

            c = banco.conexao.cursor()

            _sql = "insert into tb_produto(nome, descricao, valor_unitario, foto) values (%s,%s,%s,%s)"

            _sql_data = (self.nome,self.descricao, self.valor_unitario, self.foto,)

            c.execute(_sql,_sql_data)

            banco.conexao.commit()

            return "Produto cadastrado com sucesso!"

        except Exception as e:
            raise Exception('Erro ao tentar cadastrar produto!', str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()


    def update(self):
        banco = None
        c = None

        try:
            banco = Banco()
            
            c = banco.conexao.cursor()

            _sql = "update tb_produto set nome=%s,descricao=%s,valor_unitario=%s, foto=%s where id_produto = %s"

            _sql_data = (self.nome, self.descricao, self.valor_unitario, self.foto, self.id_produto,)

            c.execute(_sql,_sql_data)

            banco.conexao.commit()

            return "Produto atualizado com sucesso!"

        except Exception as e:
            raise Exception("Erro ao editar produto!", str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def delete(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "delete from tb_produto where id_produto = %s"

            _sql_data = (self.id_produto,)

            c.execute(_sql,_sql_data)

            banco.conexao.commit()

            return "Produto excluído com sucesso!"

        except Exception as e:
            raise Exception("Erro ao tentar excluir produto!", str(e))
        
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class ProdutosComandas(object):

    def __init__(self, id_comanda_produto=0, quantidade="", valor_unitario="", comanda_id="", produto_id="", funcionario_id=""):

        self.id_comanda_produto = id_comanda_produto
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.comanda_id = comanda_id
        self.produto_id = produto_id
        self.funcionario_id = funcionario_id
        
    def selectALL(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "SELECT TBCP.ID_COMANDA_PRODUTO, TBCP.COMANDA_ID, TBP.NOME, TBCP.QUANTIDADE, TBCP.VALOR_UNITARIO, CONVERT(TBP.FOTO USING utf8) FROM TB_PRODUTO TBP INNER JOIN TB_COMANDA_PRODUTO TBCP ON TBP.ID_PRODUTO = TBCP.PRODUTO_ID WHERE comanda_id = %s;"

            _sql_data = (self.comanda_id,)

            c.execute(_sql,_sql_data)

            resultProd = c.fetchall()

            return resultProd

        except Exception as e:
            return "Ocorreu um erro na busca do produto"

    
    def selectALLSubTotal(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "SELECT TBCP.ID_COMANDA_PRODUTO, TBCP.COMANDA_ID, TBP.NOME, TBCP.QUANTIDADE, SUM(TBCP.VALOR_UNITARIO), CONVERT(TBP.FOTO USING utf8) FROM TB_PRODUTO TBP INNER JOIN TB_COMANDA_PRODUTO TBCP ON TBP.ID_PRODUTO = TBCP.PRODUTO_ID WHERE comanda_id = %s;"

            _sql_data = (self.comanda_id,)

            c.execute(_sql,_sql_data)

            resultProd = c.fetchall()

            return resultProd

        except Exception as e:
            return "Ocorreu um erro na busca do produto"


    def deleteProdComanda(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "delete from tb_comanda_produto where id_comanda_produto = %s"

            _sql_data = (self.id_comanda_produto,)

            c.execute(_sql,_sql_data)

            banco.conexao.commit()

            return "Produto excluído com sucesso!"

        except Exception as e:
            raise Exception("Erro ao tentar excluir produto!", str(e))
        
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

            _sql = "select id_comanda_produto, quantidade, valor_unitario, comanda_id, produto_id, funcionario_id from tb_comanda_produto where comanda_id = %s"

            _sql_data = (self.comanda_id,)

            c.execute(_sql,_sql_data)

            for linha in c:
                self.id_comanda_produto = linha[0]
                self.quantidade = linha[1]
                self.comanda_id = linha[2]
                self.produto_id = linha[3]
                self.funcionario_id = linha[4]
                
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do produto"
            
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()