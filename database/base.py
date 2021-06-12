from database.conection import Conexao


class BaseDao(Conexao):

    def inserir(self, sql):
        self.cursor.execute(sql)
        self.cursor.commit()
        return True

    def listar(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def alterar(self, sql_id):
        self.cursor.execute(sql_id)
        return self.cursor.commit()
