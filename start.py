import sys
sys.path.append("C:/Users/vinte/OneDrive/Documentos/API-python/")


from flask import Flask
from flask_restful import Api
from controllers.controll import SquadsController

app = Flask(__name__)
api = Api(app)

api.add_resource(SquadsController, '/post/', endpoint="cadastrar")
api.add_resource(SquadsController, '/get/', endpoint="list_all")


app.run(debug=True)