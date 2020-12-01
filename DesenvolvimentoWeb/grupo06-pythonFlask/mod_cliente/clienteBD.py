from BancoBD import Banco
import json


class Clientes(object):

    def __init__(self, id_cliente=0, nome="", cpf="", telefone="", compra_fiado="", dia_fiado="", senha=""):

        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.compra_fiado = compra_fiado
        self.dia_fiado = dia_fiado
        self.senha = senha

    def selectALL(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "select id_cliente,nome,cpf,telefone, case when compra_fiado = 1 then 'Sim' when compra_fiado = 2 then 'Não'end  as compra_fiado,dia_fiado,senha from tb_cliente where id_cliente != 1 order by nome"

            _sql_data = ()

            c.execute(_sql, _sql_data)

            result = c.fetchall()

            return result

        except Exception as e:
            return "Ocorreu um erro na busca do cliente"

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def selectALLClientes(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "select id_cliente,nome,cpf,telefone,case when compra_fiado = 1 then 'Sim' when compra_fiado = 2 then 'Não'end  as compra_fiado,dia_fiado,senha from tb_cliente where id_cliente order by nome"

            _sql_data = ()

            c.execute(_sql, _sql_data)

            result = c.fetchall()

            return result

        except Exception as e:
            return "Ocorreu um erro na busca do cliente"

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

            _sql = "select id_cliente,nome,cpf,telefone,case when compra_fiado = 1 then 'Sim' when compra_fiado = 2 then 'Não'end  as compra_fiado,dia_fiado,senha from tb_cliente where id_cliente = %s"

            _sql_data = (self.id_cliente,)

            c.execute(_sql, _sql_data)

            for linha in c:

                self.id_cliente = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.telefone = linha[3]
                self.compra_fiado = linha[4]
                self.dia_fiado = linha[5]
                self.senha = linha[6]

            return "Busca feita com sucesso!"

        except:
            return "Ocorreu um erro na busca do cliente"

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

            _sql = "insert into tb_cliente(nome,cpf,telefone,compra_fiado,dia_fiado,senha) values (%s,%s,%s,%s,%s,%s)"

            _sql_data = (self.nome, self.cpf, self.telefone,
                         self.compra_fiado, self.dia_fiado, self.senha,)

            c.execute(_sql, _sql_data)

            banco.conexao.commit()

            return "Cliente cadastrado com sucesso!"

        except Exception as e:
            raise Exception('Erro ao cadastrar Cliente!', str(e))
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

            _sql = "update tb_cliente set nome=%s, cpf=%s, telefone=%s, compra_fiado=%s, dia_fiado=%s, senha=%s where id_cliente=%s"

            _sql_data = (self.nome, self.cpf, self.telefone, self.compra_fiado,
                         self.dia_fiado, self.senha, self.id_cliente,)

            c.execute(_sql, _sql_data)

            banco.conexao.commit()

            return "Cliente atualizado com sucesso!"

        except Exception as e:
            raise Exception("Erro ao editar cliente!", str(e))

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

            _sql = "delete from tb_cliente where id_cliente = %s"
            _sql_data = (self.id_cliente,)

            c.execute(_sql,_sql_data)

            banco.conexao.commit()

            return "Cliente excluído com sucesso!"

        except Exception as e:
            raise Exception("Erro ao tentar excluir cliente!", str(e))
        
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    

    def selectLogin(self):
        banco = Banco()

        try:
            c = banco.conexao.cursor()

            c.execute("select id_cliente, nome, cpf, telefone, compra_fiado, dia_fiado, senha from tb_cliente where cpf = %s and senha = %s", (self.cpf, self.senha))

            for linha in c:
                self.id_cliente = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.telefone = linha[3]
                self.compra_fiado = linha[4]
                self.dia_fiado = linha[5]
                self.senha = linha[6]
                
            c.close()

            return "Busca feita com sucesso!"

        except Exception as e:
            raise Exception("Dados do Cliente Incorretos", str(e))