from flask import *
from flask import Flask
#instancia de la clase flask
app = Flask(__name__)
@app.route('/') 
def hello():
    texto = "hola alumnos Flak se ha activado"
    return texto
if (__name__ == '__main__'):
    #app.run() forma general
    app.run(host="127.0.0.1" , port = 15003)