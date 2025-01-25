from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def inicio():
  enlaces= [['Martin_uneweb','https://uneweb.edu.ve/'],['Martin_tutoriales uneweb','https://uneweb.edu.ve/tutoriales'],['Martin_flask', 'https://flask.palletsprojects.com/en/stable/']]
  return render_template('ejemplo06.html', lista=enlaces)

#app.run()
app.run(host="127.0.0.1" , port = 15003)

