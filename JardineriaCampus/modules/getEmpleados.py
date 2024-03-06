import storage.empleado as em

def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = []
    for val in em.empleados:
        if(val.get("codigo_jefe") == codigo):
            nombreApellidoEmail.append({
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "email": val.get("email"),
                "jefe": val.get("codigo_jefe")
            })
    return nombreApellidoEmail


def getNombreApellidosEmailJefeEmpresa():
    nombreApellidoEmailJefe = []
    for val in em.empleados:
        if(val.get("puesto") == "Director General"):
            nombreApellidoEmailJefe.append({
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "email": val.get("email"),
                "puesto": val.get("puesto")
            })
    return nombreApellidoEmailJefe



def getAllNoRepresentante ():
    nombreApellidosPuesto = []
    for val in em.empleados:
        if val.get("puesto") != ("Representante Ventas"):
            nombreApellidosPuesto.append({
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "puesto": val.get("puesto")
            })
    return nombreApellidosPuesto