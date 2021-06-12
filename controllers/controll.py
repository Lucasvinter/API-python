import sys

sys.path.append("C:/Users/vinte/OneDrive/Documentos/API-python/")

from flask_restful import Resource
from database.usuario import *



class SquadsController(Resource):

    def __init__(self):
        self.criar = UsuarioDb()
        self.listar = UsuarioDb()

    def get(self):
        return self.listar.listar()

