from database.base import BaseDao

class Test(BaseDao):

    def validar_cpf(cpf):
        pass

    def validar_se_ja_existe_cpf(cpf):
        sql = f"SELECT FROM * usuario WHERE cpf = {cpf}"
        dados = super().listar(sql)
        print(dados)