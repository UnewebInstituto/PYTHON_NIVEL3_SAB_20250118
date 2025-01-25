from flask import Flask, request, render_template
import math
app = Flask(__name__)
@app.route('/')
def cargar_formulario():
  return render_template('ejemplo08.html')

@app.route('/', methods =['post'])
def procesar_formulario():

    lista_respuesta = []
    a = request.form["a"]
    b = request.form["b"]
    c = request.form["c"]

    an = float(a)
    bn = float(b)
    cn = float(c)

    if (an==0):
        respuesta = "Error:valor de A debe ser distinto de cero"
        lista_respuesta.append(["error", "valor de A debe ser distinto de cero"])
    else:
 
        subradical = math.pow(bn,2) - 4 *an * cn
        if (subradical < 0):
            respuesta = "Alerta:es una raiz de un nro negativo"
            lista_respuesta.append(["alerta", "es una raiz de un nro negativo"])
        else:
            x1 = (-bn + math.sqrt(subradical))/ 2 * an
            x2 = (-bn - math.sqrt(subradical))/ 2 * an
            respuesta = "<H1>X1: " + str(x1) + "<br>"  + "X2: " + str(x2) + "</h1>"
            lista_respuesta.append(["exito", "X1: " + str(x1) ])
            lista_respuesta.append(["exito", "X2: " + str(x2) ])
 
   
    
    return render_template('ejemplo08.html', resultado = lista_respuesta)
if __name__=="__main__":
    #app.run()
    app.run(host="127.0.0.1" , port = 15003)