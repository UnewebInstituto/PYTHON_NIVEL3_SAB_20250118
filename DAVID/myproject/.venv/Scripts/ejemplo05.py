from flask import Flask, request 
import math
app = Flask(import_name = __name__)

@app.route("/ecuacion")
def ec2dogrado():
    a = request.args.get("a","0")
    b = request.args.get("b","0")
    c = request.args.get("c","0")
    
    a = float(a)
    b = float(b)
    c = float(c)

    if a == 0:
        response = "<h1 style='background-color:red;color:white;text-align:center'>ERROR: Valor de 'a' debe ser difente de cero'</h1>"
    else:
        subradical = math.pow(b,2)-4*a*c
        if subradical < 0:
            response = "<h1 style='background-color:red;color:white;text-align:center'>ERROR: Expresión sub radical no puede ser negativa'</h1>"
        else:
            x1 = (-b + math.sqrt(subradical))/2*a
            x2 = (-b - math.sqrt(subradical))/2*a
            response = "<h1>x1:" + str(x1) +  "<br>x2:" + str(x2) + "</h1>"
    return response


if __name__ == '__main__':
    app.run(host="127.0.0.1" , port = 5010)

"""
    caso 1
    http://127.0.0.1:5010/ecuacion?a=0&b=1&c=1

    caso 2
    http://127.0.0.1:5010/ecuacion?a=1&b=1&c=1

    caso 3
    http://127.0.0.1:5010/ecuacion?a=1&b=4&c=1

    caso 4
    http://127.0.0.1:5010/ecuacion
"""