from flask import *
from flask import Flask
# declaracion de varaible con contenido html yccs
mensaje = "<H1 style='text-aling:center; backgroun-color:blue,color:yelow'>Phyton nivel 3 </H1> <br><h2 style='text-align:center;background-color:purple;color:yellow'>Marco de desarrollo Flask</h2>"

app = Flask(__name__)
@app.route('/')
def salida ():
    return mensaje

if (__name__ == '__main__'):
    #app.run() forma general
    app.run(host="127.0.0.1" , port = 15003)
 