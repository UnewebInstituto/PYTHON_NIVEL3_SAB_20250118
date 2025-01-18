from flask import Flask, request
import math
app = Flask(import_name = __name__)
@app.route("/ecuacion")
def ecuacionSegundoGrado():
    a = request.args.get("a","0")
    b = request.args.get("b","0")
    c = request.args.get("c","0")

    if (a==0):
        respuesta = "<H1 style='background-color:red;color:white;text-aling:center'>Error:valor de A debe ser distinto de cero"
    else:
        an = float(a)
        bn = float(b)
        cn = float(c)
        subradical = math.pow(bn,2) - 4 *an * cn
        if (subradical < 0):
            respuesta = "<H1 style='background-color:red;color:white;text-aling:center'>Error:es una raiz de un nro negativo"
        else:
            x1 = (-bn + math.sqrt(subradical))/ 2 * an
            x2 = (-bn - math.sqrt(subradical))/ 2 * an
            respuesta = "<H1>X1: " + str(x1) + "<br>"  + "X2: " + str(x2) + "</h1>"
if __name__=="__main__":
    #app.run()
    app.run(host="127.0.0.1" , port = 15003)
"""
    caso 1
    http://127.0.0.1:15003/ecuacion?a=0&b=1&c=1

    caso 2
    http://127.0.0.1:15003/ecuacion?a=1&b=1&c=1

    caso 3
    http://127.0.0.1:15003/ecuacion?a=1&b=4&c=1

    caso 4
    http://127.0.0.1:15003/ecuacion
"""