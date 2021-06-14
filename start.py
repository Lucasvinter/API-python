import sys
sys.path.append("C:/Users/vinte/OneDrive/Documentos/API-python/")


from flask import Flask
from flask_restful import Api
from controllers.controll import UsuarioController

app = Flask(__name__)
api = Api(app)

api.add_resource(UsuarioController, '/post/', endpoint="criar")
api.add_resource(UsuarioController, '/get/', endpoint="listar")
api.add_resource(UsuarioController, '/put/<int:id>/', endpoint="alterar")

app.run(debug=True)