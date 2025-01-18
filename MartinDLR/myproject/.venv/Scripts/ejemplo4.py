from flask import Flask, request

app = Flask(import_name = __name__)
"""
# Thinking


# Searching


# Thinking


# Responding



#### Descripción de la función `echo` en Flask

La función `echo` es un ejemplo de una ruta en una aplicación Flask que maneja solicitudes HTTP. Aquí está el desglose de lo que hace cada parte del código:

```python
@app.route("/echo")
def echo():
    to_echo = request.args.get("echo", "")
    response = "{}".format(to_echo)
    return response
```

1. **Decorador `@app.route("/echo")`**:
   - Este decorador define una ruta en la aplicación Flask. Cuando un usuario accede a la URL `/echo`, se invoca la función `echo`.

2. **Función `echo`**:
   - La función se encarga de procesar la solicitud que llega a la ruta `/echo`.

3. **Obtención de parámetros de consulta**:
   - `to_echo = request.args.get("echo", "")`: Aquí se utiliza `request.args.get` para obtener el valor del parámetro de consulta llamado `echo`. Si no se proporciona este parámetro en la solicitud, se asigna una cadena vacía como valor predeterminado. Esto significa que si un usuario accede a `/echo?echo=Hola`, `to_echo` contendrá "Hola".

4. **Formateo de la respuesta**:
   - `response = "{}".format(to_echo)`: Esta línea crea una cadena de respuesta que contiene el valor de `to_echo`. En este caso, simplemente se está formateando el texto para que sea una cadena.

5. **Devolución de la respuesta**:
   - `return response`: Finalmente, la función devuelve la cadena formateada como respuesta a la solicitud HTTP. Esto significa que el usuario verá el valor que pasó como parámetro `echo` en la URL.

#### Ejemplo de uso

Si un usuario accede a la URL `http://tu_dominio/echo?echo=Hola`, la respuesta será "Hola". Si no se proporciona el parámetro `echo`, la respuesta será una cadena vacía.

Este tipo de función es útil para crear APIs simples que devuelven datos basados en las solicitudes del cliente.


"""
@app.route("/echo")
def echo():
    to_echo = request.args.get("echo","")
    response = "{}".format(to_echo)
    return response

@app.route("/projects")
def proyectos():
    return "<h1 style='background-color:green;color:yellow'>Este es el sitio de proyectos</h1>"

@app.route("/about")
def acercade():
    return "<h1 style='background-color:green;color:yellow'>Este es el sitio acerca de...</h1>"

if __name__=="__main__":
    app.run()
    #app.run(host="127.0.0.1" , port = 15003)


"""
MODO DE EJECUCIÓN:
    CASO 1
    http://127.0.0.1:15003/echo
    CASO 2
    http://127.0.0.1:15003/echo?echo=ESTE ES EL VALOR DEL ECHO

    http://127.0.0.1:15003/about

    http://127.0.0.1:15003/projects

"""

