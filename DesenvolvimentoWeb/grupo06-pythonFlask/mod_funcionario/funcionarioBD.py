from BancoBD import Banco


class Funcionarios(object):
    def __init__(self, id_funcionario=0, nome="", matricula="", cpf="", telefone="", grupo="", senha=""):

        self.id_funcionario = id_funcionario
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.telefone = telefone
        self.grupo = grupo
        self.senha = senha

    def selectALL(self):
        banco = None
        c = None

        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = "select id_funcionario, nome, matricula, cpf, telefone, if(grupo =1,'Admin','Atendente'), senha from tb_funcionario"

            _sql_data = ()

            c.execute(_sql, _sql_data)

            result = c.fetchall()

            return result

        except Exception as e:
            return "Ocorreu um erro na busca do funcionário"

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

            _sql = "select id_funcionario, nome, matricula, cpf, telefone, grupo, senha from tb_funcionario where id_funcionario = %s"

            _sql_data = (self.id_funcionario,)

            c.execute(_sql, _sql_data)

            for linha in c:

                self.id_funcionario = linha[0]
                self.nome = linha[1]
                self.matricula = linha[2]
                self.cpf = linha[3]
                self.telefone = linha[4]
                self.grupo = linha[5]
                self.senha = linha[6]

            return "Busca feita com sucesso!"

        except:
            return "Ocorreu um erro na busca do funcionário"

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

            _sql = "insert into tb_funcionario(nome,matricula,cpf,telefone,grupo,senha) values (%s,%s,%s,%s,%s,%s)"

            _sql_data = (self.nome, self.matricula, self.cpf,
                         self.telefone, self.grupo, self.senha,)

            c.execute(_sql, _sql_data)

            banco.conexao.commit()

            return "Funcionário cadastrado com sucesso!"

        except Exception as e:
            raise Exception('Erro ao cadastrar Funcionário!', str(e))
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

            _sql = "update tb_funcionario set nome=%s, matricula=%s, cpf=%s, telefone=%s, grupo=%s, senha=%s where id_funcionario=%s"

            _sql_data = (self.nome, self.matricula, self.cpf, self.telefone,
                         self.grupo, self.senha, self.id_funcionario,)

            c.execute(_sql, _sql_data)

            banco.conexao.commit()

            return "Funcionário atualizado com sucesso!"

        except Exception as e:
            raise Exception("Erro ao editar Funcionário!", str(e))

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

            _sql = "delete from tb_funcionario where id_funcionario = %s"
            _sql_data = (self.id_funcionario,)

            c.execute(_sql,_sql_data)

            banco.conexao.commit()

            return "Funcionário excluído com sucesso!"

        except Exception as e:
            raise Exception("Erro ao tentar excluir Funcionário!", str(e))
        
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    #criação de método para ver se o cpf e senha existe no bd
    def selectLogin(self):
        banco = Banco()

        try:
            c = banco.conexao.cursor()

            c.execute("select id_funcionario, nome, matricula, cpf, telefone, if(grupo =1,'Admin','Atendente'), senha from tb_funcionario where cpf = %s and senha = %s", (self.cpf, self.senha))

            for linha in c:
                self.id_funcionario = linha[0]
                self.nome = linha[1]
                self.matricula = linha[2]
                self.cpf = linha[3]
                self.telefone = linha[4]
                self.grupo = linha[5]
                self.senha = linha[6]
                

            c.close()

            return "Busca feita com sucesso!"

        except:
            return "Ocorreu um erro na busca do usuário."
