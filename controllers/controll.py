import sys

sys.path.append("C:/Users/vinte/OneDrive/Documentos/API-python/")

from flask_restful import Resource
from database.usuario import *
from flask import request



class UsuarioController(Resource):

    def __init__(self):
        self.criar = UsuarioDb()
        self.listar = UsuarioDb()
        self.alterar = UsuarioDb()

    def get(self):
        return self.listar.listar()

    def post(self):
        id = request.json['id']
        cpf = request.json['cpf']
        email = request.json['email']
        telefone = request.json['telefone']
        # datanascimento = request.json['datascimento']

        return self.criar.criar(id, cpf, email, telefone)
        # return self.criar.criar(cpf, email, telefone, datanascimento)

    def put(self,):
        cpf = request.json['cpf']
        email = request.json['email']
        telefone = request.json['telefone']

        return self.alterar.alterar( cpf, email, telefone)
