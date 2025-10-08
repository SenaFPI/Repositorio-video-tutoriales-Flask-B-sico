from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS

#creamos un objeto de tipo Flask
app = Flask(__name__)

#dando permisos para que accedan a las rutas
#desde cualquier dominio
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Conexión local a MongoDB
miConexion = MongoClient('mongodb://localhost:27017/')

#objeto que representa la base de datos
baseDatos = miConexion['biblioteca']
#obeto que representa la colección libros
libros = baseDatos['libros']

#hacemos la importación de las rutas
from routes.routelibro import *

#inicio de la aplicación
if __name__=='__main__':
    app.run(port=3000,debug=True)
