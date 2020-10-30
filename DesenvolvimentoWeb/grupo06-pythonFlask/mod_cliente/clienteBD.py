from BancoBD import Banco

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

        banco = Banco()

        try:
            c = banco.conexao.cursor()

            c.execute("select id_cliente,nome,cpf,telefone,compra_fiado,dia_fiado,senha from tb_cliente")

            result = c.fetchall()

            c.close()

            return result
            
        except:

            return "Ocorreu um erro na busca do cliente"


    def selectONE(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("select id_cliente,nome,cpf,telefone,compra_fiado,dia_fiado,senha from tb_cliente where id_cliente = %s", (self.id_cliente))
            
            for linha in c:

                self.id_cliente = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.telefone = linha[3]
                self.compra_fiado = linha[4]
                self.dia_fiado = linha[5]
                self.senha = linha [6]

            c.close()

            return "Busca feita com sucesso!"

        except:

            return "Ocorreu um erro na busca do cliente"
            

    def insert(self):

        banco = Banco()

        try:
            c = banco.conexao.cursor()

            c.execute("insert into tb_cliente(nome,cpf,telefone,compra_fiado,dia_fiado,senha) values (%s,%s,%s,%s,%s,%s)",(self.nome, self.cpf, self.telefone, self.compra_fiado, self.dia_fiado, self.senha))
            
            banco.conexao.commit()
            
            c.close()
            
            return "Cliente cadastrado com sucesso!"
        
        except:
            return "Ocorreu um erro na inserção do cliente"


    def update(self):

        banco = Banco()

        try:
            c = banco.conexao.cursor()

            c.execute("update tb_cliente set nome=%s, cpf=%s, telefone=%s, compra_fiado=%s, dia_fiado=%s, senha=%s where id_cliente=%s",(self.nome, self.cpf, self.telefone, self.compra_fiado, self.dia_fiado, self.senha, self.id_cliente))
            

            banco.conexao.commit()

            c.close()

            return "Usuário atualizado com sucesso!"

        except:
            return "Ocorreu um erro na alteração do usuário"


    def delete(self):


        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("delete from tb_cliente where id_cliente = %s", (self.id_cliente))

            banco.conexao.commit()

            c.close()

            return "Cliente excluído com sucesso!"
        except:

            return "Ocorreu um erro na exclusão do Cliente"