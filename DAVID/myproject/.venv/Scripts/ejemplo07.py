from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def cargar_formulario():
  return render_template('ejemplo07.html')

@app.route('/', methods=['POST'])
def procesar_formulario():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    texto_procesado = "<h1>Datos recibidos</h1><br>Nombre: " + nombre + "<br>Apellido: " + apellido + "<br>Correo electronico: " + correo + "<br>Fin. . . "
    return texto_procesado





#app.run(host="127.0.0.1" , port = 5010)

if __name__ == '__main__':
    app.run(host="127.0.0.1" , port = 5010)