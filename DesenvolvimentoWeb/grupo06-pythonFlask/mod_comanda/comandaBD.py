from BancoBD import Banco

class Comandas(object):

    def __init__(self, id_comanda=0, numero_comanda="", data_hora="", status_comanda=0, status_pagamento=0, funcionario_id="", cliente_id=""):

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

            _sql = "select tbc.id_comanda, tbc.numero_comanda, tbc.data_hora, if(tbc.status_comanda =0,'Aberta','Fechada'), if(tbc.status_pagamento =0,'Em Aberto','Fechado'), tf.nome, tbc.cliente_id, tc.nome  from tb_comanda tbc left join tb_cliente tc on tbc.cliente_id = tc.id_cliente  left join tb_funcionario tf on tbc.funcionario_id = tf.id_funcionario order by status_comanda"

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

    def selectALLDashboard(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "SELECT TBC.ID_COMANDA, TBC.NUMERO_COMANDA, TBC.DATA_HORA, TBC.STATUS_COMANDA, TBC.STATUS_PAGAMENTO, TBC.FUNCIONARIO_ID, TBF.NOME, TBC.CLIENTE_ID, TBCLI.NOME FROM TB_COMANDA TBC INNER JOIN TB_FUNCIONARIO TBF ON TBF.ID_FUNCIONARIO = TBC.FUNCIONARIO_ID INNER JOIN TB_CLIENTE TBCLI ON TBCLI.ID_CLIENTE = TBC.CLIENTE_ID where TBC.STATUS_COMANDA = 0"

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

    def selectALLComandasAtrasadas(self):
            banco = None
            c = None

            try:
                banco = Banco()

                c = banco.conexao.cursor()

                _sql = "select tbc.id_comanda as ID, tbc.numero_comanda as Comanda, tbc.data_hora as 'Data', SUM( tbcp.quantidade * tbcp.valor_unitario) as Total, tcl.nome as Cliente, tf.nome as Funcionario, CASE WHEN (DATEDIFF(NOW(),tbc.data_hora)-30) > 0 THEN (DATEDIFF(NOW(),tbc.data_hora)-30) ELSE 0 END AS 'Dias Atraso', CASE WHEN (DATEDIFF(NOW(),tbc.data_hora)-30) > 0 THEN (select multa_atraso from tb_empresa) ELSE 0 END as 'Multa', CASE WHEN (DATEDIFF(NOW(),tbc.data_hora)-30) > 0 THEN round((((select taxa_juro_diario from tb_empresa)* SUM(tbcp.quantidade * tbcp.valor_unitario))/100)*(DATEDIFF(NOW(),tbc.data_hora)-30), 2) ELSE 0 END as 'Juro' from tb_comanda tbc inner join tb_comanda_produto tbcp on tbcp.comanda_id = tbc.id_comanda inner join tb_produto tp on tbcp. produto_id = tp.id_produto inner join tb_funcionario tf on tbcp.funcionario_id = tf.id_funcionario inner join tb_cliente tcl on tbc.cliente_id = tcl.id_cliente  where tbc.status_pagamento = 1  and tbc.status_comanda = 1   and (DATEDIFF(NOW(),tbc.data_hora)-30) > 0 group by tbcp.comanda_id order by tbc.data_hora"

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

            _sql = "insert into tb_comanda(numero_comanda,data_hora,status_comanda,status_pagamento,funcionario_id,cliente_id) values (%s,%s,%s,%s,%s,%s)"

            _sql_data = (self.numero_comanda, self.data_hora, self.status_comanda,
                         self.status_pagamento, self.funcionario_id, self.cliente_id)

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

class ComandaAddCliente(object):

    def __init__(self, id_comanda=0, numero_comanda="", data_hora="", status_comanda=1, status_pagamento=1, funcionario_id="", cliente_id=""):

        self.id_comanda = id_comanda
        self.numero_comanda = numero_comanda
        self.data_hora = data_hora
        self.status_comanda = status_comanda
        self.status_pagamento = status_pagamento
        self.funcionario_id = funcionario_id
        self.cliente_id = cliente_id

                

    def update(self):
        banco = None
        c = None

        try:
            banco = Banco()
            
            c = banco.conexao.cursor()

            _sql = "update tb_comanda set cliente_id=%s where id_comanda = %s"

            _sql_data = (self.cliente_id, self.id_comanda,)

            c.execute(_sql,_sql_data)

            banco.conexao.commit()

            return "Cliente vinculado com Sucesso!"

        except Exception as e:
            raise Exception("Erro ao vincular Cliente!", str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()


class ComandaRecebimento(object):

    def __init__(self, id_recebimento=0, data_hora="", tipo="", valor_acrescimo=0, valor_desconto="", valor_total="", funcionario_id="", recebimento_id="", id_comanda="", id_cliente=""):

        self.id_recebimento = id_recebimento
        self.data_hora = data_hora
        self.tipo = tipo
        self.valor_acrescimo = valor_acrescimo
        self.valor_desconto = valor_desconto
        self.valor_total = valor_total
        self.funcionario_id = funcionario_id
        self.recebimento_id = recebimento_id
        self.id_comanda = id_comanda
        self.id_cliente = id_cliente





    def insert(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "insert into tb_recebimento(data_hora,tipo,valor_acrescimo,valor_desconto,valor_total,funcionario_id) values (%s,%s,%s,%s,%s,%s)"

            _sql_data = (self.data_hora, self.tipo, self.valor_acrescimo,
                         self.valor_desconto, self.valor_total, self.funcionario_id,)

            c.execute(_sql, _sql_data)

            banco.conexao.commit()

            x = c.lastrowid

            return x

        except Exception as e:
            raise Exception('Erro ao Finalizar Comanda!', str(e))
        finally:
            if c:
                c.close
            if banco:
                banco.conexao.close()

    def pegarLastrowid(self):
        banco = None
        c = None

        try:
            banco = Banco()
            c = banco.conexao.cursor()

            _sql = "select max(id_recebimento) from tb_recebimento;"

            c.execute(_sql) 

            banco.conexao.commit()

            lastId = c.fetchall()

            return lastId

        except Exception as e:
            raise Exception('Erro ao Pegar Ultimo ID Comanda!', str(e))
        finally:
            if c:
                c.close
            if banco:
                banco.conexao.close()

    def updateTbComandaAVista(self):
        banco = None
        c = None

        try:
            banco = Banco()
            
            c = banco.conexao.cursor()

            _sql = "UPDATE TB_COMANDA SET STATUS_COMANDA=1, STATUS_PAGAMENTO=1 WHERE ID_COMANDA = %s"

            _sql_data = (self.id_comanda,)

            c.execute(_sql,_sql_data)

            banco.conexao.commit()

            return "Comanda Recebida com Sucesso!"

        except Exception as e:
            raise Exception("Erro ao Receber Comanda", str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def updateTbComandaFiado(self):
        banco = None
        c = None

        try:
            banco = Banco()
            
            c = banco.conexao.cursor()

            _sql = "UPDATE TB_COMANDA SET STATUS_COMANDA=2, STATUS_PAGAMENTO=0 WHERE ID_COMANDA = %s"

            _sql_data = (self.id_comanda,)

            c.execute(_sql,_sql_data)

            banco.conexao.commit()

            return "Comanda Finalizada com Sucesso!"

        except Exception as e:
            raise Exception("Erro ao Receber Comanda", str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def updateTbComandaFiadoPaga(self):
        banco = None
        c = None

        try:
            banco = Banco()
            
            c = banco.conexao.cursor()

            _sql = "UPDATE TB_COMANDA SET STATUS_COMANDA=2, STATUS_PAGAMENTO=1 WHERE ID_COMANDA = %s"

            _sql_data = (self.id_comanda,)

            c.execute(_sql,_sql_data)

            banco.conexao.commit()

            return "Comanda Finalizada com Sucesso!"

        except Exception as e:
            raise Exception("Erro ao Receber Comanda", str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def insertTbComandaRecebimento(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "insert into tb_comanda_recebimento(recebimento_id, comanda_id) values (%s,%s)"

            _sql_data = (self.recebimento_id, self.id_comanda,)

            c.execute(_sql, _sql_data)

            banco.conexao.commit()

            return "Comanda Finalizada com Sucesso!"

        except Exception as e:
            raise Exception('Erro ao Finalizar Comanda!', str(e))
        finally:
            if c:
                c.close
            if banco:
                banco.conexao.close()

    

    

    def selectRecebimentoAVista(self):
        banco = None
        c = None

        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "select tbr.id_recebimento, tbc.numero_comanda, tbr.data_hora, if(tbr.tipo =1, 'A Vista', 'Fiado') as tipo, tbr.valor_total, tbf.nome from tb_recebimento tbr left join tb_funcionario tbf  on tbr.funcionario_id = tbf.id_funcionario  inner join tb_comanda_recebimento tbcr on tbr.id_recebimento = tbcr.recebimento_id inner join tb_comanda tbc on tbcr.comanda_id = tbc.id_comanda where tbr.tipo = 1 order by data_hora"
            _sql_data = ()
            c.execute(_sql,_sql_data)
            result = c.fetchall()
            return result
            
        except Exception as e:
            return "Ocorreu um erro na busca do Recebimento"
            
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def selectRecebimentoFiado(self):
        banco = None
        c = None

        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "select tbr.id_recebimento, tbc.numero_comanda, tbr.data_hora, if(tbr.tipo =1, 'A Vista', 'Fiado') as tipo, tbr.valor_total, tbf.nome from tb_recebimento tbr left join tb_funcionario tbf  on tbr.funcionario_id = tbf.id_funcionario  inner join tb_comanda_recebimento tbcr on tbr.id_recebimento = tbcr.recebimento_id inner join tb_comanda tbc on tbcr.comanda_id = tbc.id_comanda where tbr.tipo = 2 order by data_hora"
            _sql_data = ()
            c.execute(_sql,_sql_data)
            result = c.fetchall()
            return result
            
        except Exception as e:
            return "Ocorreu um erro na busca do Recebimento"
            
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def selectSubTotalProdsPedidos(self):
        banco = None
        c = None

        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "SELECT SUM(VALOR_UNITARIO) FROM TB_COMANDA_PRODUTO WHERE COMANDA_ID = %s"
            _sql_data = (self.comanda_id,)
            c.execute(_sql,_sql_data)
            resultSubTotal = c.fetchall()
            return resultSubTotal
            
        except Exception as e:
            return "Ocorreu um erro na busca do subTotal"
            
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()


    def selectALLComandasFiados(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "SELECT TBC.NUMERO_COMANDA, TBC.DATA_HORA, TBCLI.ID_CLIENTE, TBCLI.NOME, SUM(TBCP.VALOR_UNITARIO) as 'VALOR TOTAL' FROM TB_COMANDA TBC INNER JOIN TB_CLIENTE TBCLI ON TBCLI.ID_CLIENTE = TBC.CLIENTE_ID INNER JOIN TB_COMANDA_PRODUTO TBCP ON TBC.ID_COMANDA = TBCP.COMANDA_ID WHERE STATUS_COMANDA = 2 AND STATUS_PAGAMENTO = 0  GROUP BY TBC.NUMERO_COMANDA"
            
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

    def selectONEComandasFiados(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "SELECT TBC.ID_COMANDA,TBC.NUMERO_COMANDA, TBC.DATA_HORA, TBCLI.ID_CLIENTE, TBCLI.NOME, SUM(TBCP.VALOR_UNITARIO) as 'VALOR TOTAL' FROM TB_COMANDA TBC INNER JOIN TB_CLIENTE TBCLI ON TBCLI.ID_CLIENTE = TBC.CLIENTE_ID INNER JOIN TB_COMANDA_PRODUTO TBCP ON TBC.ID_COMANDA = TBCP.COMANDA_ID WHERE STATUS_COMANDA = 2 AND STATUS_PAGAMENTO = 0 AND TBCLI.ID_CLIENTE = %s GROUP BY TBC.NUMERO_COMANDA"
            
            _sql_data = (self.id_cliente)

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

    






