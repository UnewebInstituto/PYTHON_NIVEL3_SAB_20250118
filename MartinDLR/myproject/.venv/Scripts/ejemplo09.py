from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/')
def cargar_formulario():
    return render_template('ejemplo09.html')

@app.route('/', methods=['POST'])
def procesar_formulario():
    lista_response = []

    a = request.form["a"]
    b = request.form["b"]
    c = request.form["c"]
    
    a = float(a)
    b = float(b)
    c = float(c)

    if a == 0:
        lista_response.append(["danger","Valor de 'a' debe ser difente de cero"])
    else:
        subradical = math.pow(b,2)-4*a*c
        if subradical < 0:
            lista_response.append(["warning","Expresión sub radical no puede ser negativa"])
        else:
            x1 = (-b + math.sqrt(subradical))/2*a
            x2 = (-b - math.sqrt(subradical))/2*a
            lista_response.append(["success", "x1:" + str(x1) +  ", x2:" + str(x2)])
    
    return render_template('ejemplo09.html',resultado=lista_response)

if __name__=="__main__":
    app.run()
    #app.run(host="127.0.0.1" , port = 5555)