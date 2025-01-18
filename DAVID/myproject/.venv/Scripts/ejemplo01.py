from flask import *
from flask import Flask
# Instancia de la clase Flask
app = Flask(__name__)
# Referencia a decorador de ruta
@app.route('/')
def hello():
    return 'Hola alumnos de UNEWEB, Flask se ha activado'
if __name__ == '__main__':
    #app.run()
    app.run(host="127.0.0.1", port=5010)