from flask import Flask, request
# instancia de la calse flsk<  
app =Flask(import_name= __name__)
#se define el decorador de rutas
@app.route("/echo")
def echo():
    #extracion del requerimieno para los datos ingresados
    to_dato1  = request.args.get("dato1")
    to_dato2  = request.args.get("dato2")

    respose = "<u>" + to_dato1 + "</u>" + "<br>" + "<i>" + to_dato2 + "</i>" 
    return respose
if (__name__ == '__main__'):
    #app.run() forma general
    app.run(host="127.0.0.1" , port = 15003)
"""
    esto e con el metodo get
    ejecucion http://localhost:15003/echo?dato1=ESTO Es&dato2=Una Prueba
"""