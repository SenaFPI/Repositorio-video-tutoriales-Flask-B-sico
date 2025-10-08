#importar la libreria Flask
from flask import Flask, render_template

#crear un objeto de tipo Flask
app = Flask(__name__)

#crear la ruta raiz
@app.route("/")
def home():
    return "Bienvenido al curso Desarrollo Web en Python con Flask"

#ruta con una variable
@app.route("/saludo/<nombre>")
def saludar(nombre):
    return f"Hola {nombre}, bienvenido al curso de Ptyhon con Flask desde el SENA."

#ruta que retorna a un documento html
@app.route("/pagina")
def mostrarHtml():
    return render_template("index.html")


#ruta que retorna a un documento html y envía datos
@app.route("/bienvenido")
def mostrarHtmlDatos():
    titulo="CURSO DESARROLLO WEB EN PYTHON CON FLASK"
    mensaje="Hola, le damos la bienvenida al curso. En cada vídeo aprenderemos cosas nuevas."
    return render_template("index.html", titulo=titulo, mensaje=mensaje )

#iniciar la aplicación
if __name__=="__main__":
    app.run(port=3000, debug=True)