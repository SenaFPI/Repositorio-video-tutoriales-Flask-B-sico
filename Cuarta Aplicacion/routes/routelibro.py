from app import app, libros
from flask import render_template, request, redirect, url_for, jsonify
from bson.objectid import ObjectId
from flask_cors import cross_origin
# Listar libros
@app.route('/')
def index():
    todos = libros.find()
    return render_template('index.html', libros=todos)

# Agregar libro
@cross_origin() # Habilita CORS para esta ruta
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nuevo = {
            'titulo': request.form['titulo'],
            'autor': request.form['autor']
        }
        resultado = libros.insert_one(nuevo)
        if(resultado.acknowledged):
            return redirect(url_for('index'))
    return render_template('add.html')

# Editar libro
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    libro = libros.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        libros.update_one({'_id': ObjectId(id)}, {
            '$set': {
                'titulo': request.form['titulo'],
                'autor': request.form['autor']
            }
        })
        return redirect(url_for('index'))
    return render_template('edit.html', libro=libro)

# Eliminar libro
@app.route('/delete/<id>')
def delete(id):
    libros.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

@app.route("/api/libros", methods=['GET'])
def apiLibros():
    todos = libros.find()
    listaSerializada=[]
    for libro in todos:
        libroSerializado = {
            "id": str(libro['_id']),
            "titulo": libro['titulo'],
            "autor": libro['autor']
        }
        listaSerializada.append(libroSerializado)
    return jsonify({"libros":listaSerializada})

@app.route("/api/libros/<id>", methods=['GET'])
def consultarPorId(id):
    try:
        id = ObjectId(id)
        libro=libros.find_one({"_id": id})
        if libro is not None:
            libroSerializado={
                "id": str(libro['_id']),
                "titulo": libro['titulo'],
                "autor": libro['autor']
            }
            return jsonify({"libro": libroSerializado})
        else:
            return jsonify({"mensaje": "No existe libro con ese id"})
    except Exception as error:
        mensaje = str(error)
        return jsonify({"mensaje": mensaje})
    

@app.route('/api/libros', methods=['POST'])
def apiAdd():  
    try:  
        datos=request.get_json()
        nuevo = {
            'titulo': datos['titulo'],
            'autor': datos['autor']
        }
        resultado = libros.insert_one(nuevo)
        if(resultado.acknowledged):
            return jsonify({"mensaje": f"Libro agregado correcamente \
                con id: {resultado.inserted_id}"})
        else:
            return jsonify({"mensaje": "problemas al agregar el libro"})
    except Exception as error:
        mensaje = str(error)
        return jsonify({"mensaje": mensaje}) 
