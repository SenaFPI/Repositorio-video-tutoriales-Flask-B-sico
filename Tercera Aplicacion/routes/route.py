from app import app, mail
from flask import request, render_template, session, redirect, url_for
from config import ALLOWED_EXTENSIONS, MAIL_DEFAULT_SENDER
from werkzeug.utils import secure_filename
from flask_mail import Message
import os

listaArchivos=[]
# Verifica si el archivo es permitido
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#ruta raiz
@app.route('/')
def index():
    #valida si el usuario está en la sesión
    if 'usuario' in session:
        return redirect(url_for('upload'))
    return redirect(url_for('login'))

#ruta para iniciar la sesión
@app.route('/login', methods=['GET', 'POST'])
def login():     
    if request.method == 'POST':
        if request.form['usuario'] == 'ccuellar@sena.edu.co' and request.form['clave'] == 'sena12345':
            session['usuario'] = request.form['usuario']   
            listaArchivos.clear()     
            return redirect(url_for('upload'))
        else:
            mensaje="Credenciales Incorrectas"
            return render_template("login.html", mensaje=mensaje)
    
    return render_template("login.html")
            

#ruta que carga los archivos enviados desde el cliente
#mediante petición post
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'usuario' not in session:        
        mensaje = 'Debe primero ingresar con credenciales'
        return render_template("login.html", mensaje=mensaje)

    if request.method == 'POST':
        archivo = request.files['archivo']
        if archivo and allowed_file(archivo.filename):
            filename = secure_filename(archivo.filename)
            archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            enviarCorreo(filename)
            listaArchivos.append(filename)
            return render_template('success.html', archivos=listaArchivos)
        else:
            mensaje="Tipo de Archivo no permitido, vuelva a seleccionar \
            con alguna de estas extensiones: [jpg, pdf, jpeg, png]"
            return render_template("upload.html",mensaje=mensaje)

    return render_template('upload.html')

#Ruta para salir del sistema y eliminar las variables de sesión
@app.route('/logout')
def logout():
    #elimina las variables de sesión existentes
    session.clear()
    mensaje="Ha cerrado la sesión"
    return render_template("login.html", mensaje=mensaje)


def enviarCorreo(archivo):
    asunto="Confirmación subida de archivo al aplicativo"
    mensaje=f"Cordial saludo, nos permitimos confirmar el cargue del archivo \
        con nombre <b>{archivo}</b>.<br><br> Muchas gracias, <br><br> \
        Cordialmente,<br><br><b>Administrador</b>"
    remitente = MAIL_DEFAULT_SENDER
    correo = Message(asunto, sender=remitente, recipients=[session['usuario']])
    correo.html = mensaje  # en formato html  
    mail.send(correo)
    return 'Correo enviado!'
    

