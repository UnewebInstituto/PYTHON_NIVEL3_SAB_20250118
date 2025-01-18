from flask import *
# from flask import Flask
# Declaración de variable con contenido
# html y css
mensaje = "<h1 style='text-align:center;background-color:blue;color:yellow'>Python nivel 3</h1><br><h2 style='text-align:center;background-color:purple;color:yellow'>Marco de desarrollo Flask</h2>"

app = Flask(__name__)
@app.route('/')
def salida():
    return mensaje

if __name__ == "__main__":
    app.run(host="127.0.0.1" , port = 5010)
# app.run(host="127.0.0.1" , port = 5010)