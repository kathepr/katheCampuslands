from tabulate import tabulate

import storage.empleado as em


#FUNCIÓN 1:
def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = []
    for val in em.empleados:
        if(val.get("codigo_jefe") == codigo):
            nombreApellidoEmail.append({
                "Nombre": val.get("nombre"),
                "Apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "Email": val.get("email"),
                "Código del Jefe": val.get("codigo_jefe")
            })
    return nombreApellidoEmail


#FUNCIÓN 2:
def getNombreApellidosEmailJefeEmpresa():
    nombreApellidoEmailJefe = []
    for val in em.empleados:
        if(val.get("puesto") == "Director General"):
            nombreApellidoEmailJefe.append({
                "Nombre": val.get("nombre"),
                "Apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "Email": val.get("email"),
                "Puesto": val.get("puesto")
            })
    return nombreApellidoEmailJefe


#FUNCIÓN 3:
def getAllNoRepresentante():
    nombreApellidosPuesto = []
    for val in em.empleados:
        if val.get("puesto") != ("Representante Ventas"):
            nombreApellidosPuesto.append({
                "Nombre": val.get("nombre"),
                "Apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "Puesto": val.get("puesto")
            })
    return nombreApellidosPuesto



def menu():
    while True:
        print("""

                        ******************************************
                                Reportes de los Empleados
                        ******************************************
          
        0. Regresar al menú principal
        1. Obtener información del nombre, apellidos y email de los empleados a través del código del jefe (ejemplo: 2)
        2. Obtener información del nombre, apellidos, email y puesto del jefe de la empresa
        3. Obtener información del nombre, apelidos y puesto de aquellos empleados que NO son representantes de ventas

        """)
        opcion = int(input("\nSeleccione una de las opciones "))
        if opcion == 1:
            codigo = int(input("Ingrese el código del jefe: "))
            print(tabulate(getAllNombreApellidoEmailJefe(codigo), headers = "keys", tablefmt = "rounded_grid"))
        elif opcion == 2:
            print(tabulate(getNombreApellidosEmailJefeEmpresa(), headers = "keys", tablefmt = "rounded_grid"))
        elif opcion == 3:
            print(tabulate(getAllNoRepresentante(), headers = "keys", tablefmt = "rounded_grid"))
        elif opcion == 0:
            break