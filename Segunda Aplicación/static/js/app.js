let contactos=[] //arreglo con los contactos
const btnEnviar = document.querySelector("#btnEnviar")

btnEnviar.addEventListener("click",()=>{
    //objeto para hacer referencia al formulario
    const frmContacto = document.querySelector("#frmContacto")
    //objeto de tipo formdata con los datos del formulario
    const frmDataContacto = new FormData(frmContacto)
    //objeto en formato json para enviarlo al servidor
    const jsonData = {}
    // Convierte FormData a JSON
    for (const [key, value] of frmDataContacto.entries()) {
        jsonData[key] = value;
    }
    //la url para realizar la petición
    const URL = "/agregarJson"
    //hacer la petición al servidor
    fetch(URL, {
        headers: {     
           'Content-Type': 'application/json'
        },
        method:'post',
        body: JSON.stringify(jsonData)
    })
    .then(resultado=>resultado.json())
    .then(datos=>{
        console.log(datos)
        contactos=datos.contactos
        document.querySelector("#mensaje").textContent=datos.mensaje  
        frmContacto.reset()
        mostrarContactosTabla()
    })
})

/**
 * Agrega filas a la tabla de acuerdo
 * a la cantidad de contactos
 */
function mostrarContactosTabla(){
    let datos = document.querySelector("#datos")
    let filas=""
    contactos.forEach((contacto,index) => {
        filas += "<tr>"
        filas += "<td>" + contacto.nombre + "</td>"
        filas += "<td>" + contacto.correo + "</td>"
        filas += "<td>" + contacto.telefono + "</td>"
        filas += `<td class='text-center'>
                  <button class='btn btn-warning' onClick='eliminar(${index})'>X</button></td>`
        filas += `<td class='text-center'>
                  <button class='btn btn-danger text-white' onClick='eliminar(${index})'>X</button></td>`
        filas += "</tr>"         
    });
    datos.innerHTML=filas
}

/**
 * Función que realiza la petición al servidor
 * para eliminar un contacto a partir de la
 * posición en el arreglo
 * @param {int} index 
 */
function eliminar(index){
    const URL = "/eliminarJson"
    const datos = {
        posicion: index
    }
    //hacer la petición al servidor
    fetch(URL, {
        headers: {     
           'Content-Type': 'application/json'
        },
        method:'delete',
        body: JSON.stringify(datos)
    })
    .then(resultado=>resultado.json())
    .then(datos=>{
        console.log(datos)   
        contactos=datos.contactos 
        document.querySelector("#mensaje").textContent=datos.mensaje   
        mostrarContactosTabla()
    })
}

