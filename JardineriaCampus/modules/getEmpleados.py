from tabulate import tabulate
import json
import requests


def getAllEmpleado():
    peticion = requests.get("http://154.38.171.54:5003/empleados")
    data = json.loads(peticion.text)
    return data

#FUNCIÓN 1:
def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = []
    for val in getAllEmpleado():
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
    for val in getAllEmpleado():
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
    for val in getAllEmpleado():
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

        try: 
            opcion = int(input("\nSeleccione una de las opciones "))
            if opcion>=0 and opcion<4:
                if opcion == 1:
                    codigo = int(input("Ingrese el código del jefe: "))
                    print(tabulate(getAllNombreApellidoEmailJefe(codigo), headers = "keys", tablefmt = "rounded_grid"))
                elif opcion == 2:
                    print(tabulate(getNombreApellidosEmailJefeEmpresa(), headers = "keys", tablefmt = "rounded_grid"))
                elif opcion == 3:
                    print(tabulate(getAllNoRepresentante(), headers = "keys", tablefmt = "rounded_grid"))
                elif opcion == 0:
                    break
            else:
                print("\nOJO: No existe esa opción, por favor vuelva a intentarlo")

        except ValueError:
            print("""
                  -----------------------------------------------------------------------------
                  Solo se permiten los NÚMEROS ENTEROS correspondientes a la OPCIÓN ESCOGIDA
                                        Por favor, intentelo de nuevo.
                  -----------------------------------------------------------------------------""")
                        