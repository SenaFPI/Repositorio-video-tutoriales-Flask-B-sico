#importar la libreria Flask
from flask import Flask, render_template, request, jsonify

#crear un objeto de tipo Flask
app = Flask(__name__)

#lista donde vamos a guardar los datos
contactos=[]

@app.route("/", methods=['GET'])
def home():
    if request.method == 'GET':
        #retorna al documento html y envía la lista de contactos
        return render_template("contacto.html", contactos=contactos)
    
    
@app.route("/agregar", methods=['GET','POST'])
def agregar():
    if request.method == 'GET':
        #retorna al documento html y envía la lista de contactos
        return render_template("contacto.html", contactos=contactos)
    elif request.method == 'POST': 
        nombre=request.form['txtNombre']
        correo=request.form['txtCorreo']
        telefono=request.form['txtTelefono']
        #crear un objeto llamado contacto de tipo diccionario / json
        contacto={"nombre": nombre, "correo": correo, "telefono": telefono}
        #agregar el contacto a la lista de contactos
        contactos.append(contacto)
        mensaje="Contacto Agregado correctamente..."
        return render_template("contacto.html", contactos=contactos, mensaje=mensaje)
       
        
@app.route("/agregarJson", methods=['POST'])
def agregarJson():
    """_summary_
    Función que atiende la petición de agregar
    un contacto del cliente. Los datos vienen
    en formato Json
    Returns:
        _type_: _description_
    """
    if request.method == 'POST':        
        datos = request.get_json()
        nombre=datos["txtNombre"]
        correo=datos['txtCorreo']
        telefono=datos['txtTelefono']
        #crear un objeto llamado contacto de tipo diccionario / json
        contacto={"nombre": nombre, "correo": correo, "telefono": telefono}
        contactos.append(contacto)
        mensaje="Contacto Agregado correctamente..."
        print(datos)
        return jsonify({"mensaje": mensaje, "contactos": contactos})
    

@app.route("/",methods=['GET'])
def inicio():
    if request.method == 'GET':
        return render_template("contacto.html", contactos=contactos)
    
    
@app.route("/eliminar/<int:posicion>", methods=['GET'])
def eliminar(posicion):
    """_summary_
    Elimina un contacto de acuerdo a la posición 
    del contacto en el arreglo que viene en la ruta
    Args:
        posicion (int): posición en el arreglo
    Returns:
        _type_: _description_
    """
    if request.method == 'GET':
        if len(contactos)>0:
            contactos.pop(posicion)
            mensaje="Contacto Eliminado..."
        else:
            mensaje="No hay contactos para eliminar"
            
    return render_template("contacto.html", contactos=contactos, mensaje=mensaje)

@app.route("/eliminarJson", methods=['DELETE'])
def eliminarJson():
    """_summary_
    Elimina un contacto. Recibe como parametro
    dentro del requesta la posición del contacto
    en el arreglo para eliminarlo.
    Returns:
        _type_: _description_
    """
    if request.method == 'DELETE':        
        datos = request.get_json()
        contactos.pop(datos['posicion'])
        mensaje="Contacto eliminado"
        return jsonify({"mensaje": mensaje, "contactos": contactos})
    
        
    
#iniciar la aplicación
if __name__=="__main__":
    app.run(port=3000, debug=True)