from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<html><body><h1>Este es el servidor de Jocelyne en Flask</h1></body></html>"

@app.route("/hola")
def hello():
    return "<html><body><h1>Esta es otra pagina</h1></body></html>"

@app.route("/alumno")
def alumno():
    alumno={'id': 1,'nombre':'Pedro', 'edad':20, 'aprobado':False } #diccionario
    cadenaJson=json.dumps(alumno)
    return cadenaJson
