from flask import Flask, request
# Instancia de la clase flask
app = Flask(import_name=__name__)

# Se define el decorador de ruta
@app.route("/echo")
def echo():
    # Extraccion del equerimiento para los datos ingresados
    to_dato1 = request.args.get("dato1")
    to_dato2 = request.args.get("dato2")
    response = "<u>" + to_dato1 + "</u>" + "<br>" + "<i>" + to_dato2 + "</i>"
    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5010)
    #app.run(host="127.0.0.1" , port = 5010)
    
"""""
    Ejecucion:
    http://127.0.0.1:5010/echo?dato1=ESTO ES&dato2=UNA PRUEBA
    """
    