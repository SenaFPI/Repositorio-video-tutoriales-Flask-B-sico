from flask import Flask
from flask_mail import Mail
from config import *
import os

#creamos un objeto de tipo Flask
app = Flask(__name__)
app.secret_key = 'clave_secreta_docente'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#configuración para email
app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = MAIL_DEFAULT_SENDER

#creamos un objeto de tipo Mail
mail = Mail(app)
#mail.init_app(app)
#importamos las rutas
from routes.route import *

#inicio de la aplicación
if __name__=='__main__':
    #crea el directorio uploads sino existe
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)   
    app.run(port=3000,debug=True)
