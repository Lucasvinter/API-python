import sys

from app.domains.user.actions import Test

sys.path.append("C:/Users/vinte/OneDrive/Documentos/API-python/")
from app.domains.user.models import Usuario
from database.base import BaseDao



class UsuarioDb(BaseDao):

    def listar(self):
        lista_usuario = []
        sql = "SELECT * FROM usuario"
        tupla = super().listar(sql)
        for linha in tupla:
            # p = Usuario(linha[0], linha[1], linha[2], linha[3], linha[4])
            p = Usuario(linha[0], linha[1], linha[2], linha[3])
            lista_usuario.append(p.__dict__)
        return lista_usuario

    def alterar(self,id, cpf, email, telefone):
        super().cursor.execute(
            f"Update apipython.usuario set cpf={cpf}, email={email}, telefone={telefone} datanscimento = DEFAULT WHERE id = {id} ")
        return "usuario alterado com sucesso"


    def criar(self, id, cpf, email, telefone):
        # if validar_cpf(cpf):
        # Test.validar_se_ja_existe_cpf(cpf)
        super().cursor.execute(
            f"Insert into usuario values ({id}, {cpf}, '{email}', {telefone}, DEFAULT )")
        super().con.commit()
        return "usuario cadastrado"
