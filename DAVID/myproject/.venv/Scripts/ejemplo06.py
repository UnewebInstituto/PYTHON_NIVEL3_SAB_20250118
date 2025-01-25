from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    enlaces = [['Uneweb','https://www.uneweb.edu.ve/'],['Tutoriales Uneweb','https://www.uneweb.edu.ve/tutoriales/'],['Flask framework','https://flask.palletsprojects.com/en/stable/']]

    return render_template('ejemplo06.html', lista=enlaces)

#app.run(host="127.0.0.1" , port = 5010)
app.run(host="127.0.0.1" , port = 5010)