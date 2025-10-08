function eliminar(id){
    Swal.fire({
        title: "¿Está usted seguro de Eliminar el Libro?",    
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        cancelButtonText: "NO",
        confirmButtonText: "SI"
    })
    .then((result) => {
        if (result.isConfirmed) {
            location.href=`/delete/${id}`
        }
    });
}