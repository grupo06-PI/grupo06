from BancoBD import Banco

class Configuracoes(object):

    def __init__(self, taxa_juro_diario=0, multa_atraso=0):
        self.taxa_juro_diario = taxa_juro_diario
        self.multa_atraso = multa_atraso


    def SelectALL(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "select taxa_juro_diario, multa_atraso from tb_empresa"

            _sql_data = ()

            c.execute(_sql,_sql_data)

            result = c.fetchall()

            return result

        except Exception as e:
            return "Ocorreu um erro na busca"

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

            _sql = "select taxa_juro_diario, multa_atraso from tb_empresa"
            
            _sql_data = ()
            
            c.execute(_sql, _sql_data)

            for linha in c:
                self.taxa_juro_diario = linha[0]
                self.multa_atraso = linha[1]

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do produto"
            
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

            _sql = "update tb_empresa set taxa_juro_diario=%s, multa_atraso=%s"

            _sql_data = (self.taxa_juro_diario, self.multa_atraso,)

            c.execute(_sql,_sql_data)

            banco.conexao.commit()

            return "Configurações atualizadas com sucesso!"

        except Exception as e:
            raise Exception("Erro ao editar configurações!", str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()
