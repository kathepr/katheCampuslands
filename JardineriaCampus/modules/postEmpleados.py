import json
import requests
from tabulate import tabulate


def postEmpleado():
    empleado = {
        "codigo_empleado": int(input("Ingrese el código del empleado: ")),
        "nombre": input("Ingrese el nombre del empleado: "),
        "apellido1": input("Ingrese el primer apellido: "), 
        "apellido2": input("Ingrese el segundo apellido: "),
        "extension": input("Ingrese la extensión: "),
        "email": input("Ingrese el email: "),
        "codigo_oficina": input("Ingrese el nombre de la oficina: "),
        "codigo_jefe": int(input("Ingrese el código del jefe: ")),
        "puesto": input("Ingrese el puesto del empleado: ")
    }
    url = "http://154.38.171.54:5003/empleados"
    data = json.dumps(empleado)
    peticion = requests.post(url,data)
    print("\nEmpleado Guardado")



def deleteEmpleado(id):
    peticion = requests.delete(f"http://154.38.171.54:5003/empleados/{id}")
    if peticion.status_code == 200:
          print("\nEmpleado Eliminado")

def updateEmpleado(id):
    empleadoActualizado = {
        "codigo_empleado": int(input("Ingrese el código del empleado: ")),
        "nombre": input("Ingrese el nombre del empleado: "),
        "apellido1": input("Ingrese el primer apellido: "), 
        "apellido2": input("Ingrese el segundo apellido: "),
        "extension": input("Ingrese la extensión: "),
        "email": input("Ingrese el email: "),
        "codigo_oficina": input("Ingrese el nombre de la oficina: "),
        "codigo_jefe": int(input("Ingrese el código del jefe: ")),
        "puesto": input("Ingrese el puesto del empleado: ")
    }
    url = (f"http://154.38.171.54:5003/empleados/{id}")
    data = json.dumps(empleadoActualizado)
    peticion = requests.put(url,data)
    if peticion.status_code == 200:
            print("\nEmpleado Actualizado")

def menu():
    while True:
        print("""
        
        ADMINISTRAR DATOS DE EMPLEADOS:

        1. Guardar empleado nuevo
        2. Eliminar un empleado
        3. Actualizar un empleado
        0. Regresar
        
        
        """)
        
        try: 
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion >=0 and opcion<=3:
                if(opcion == 1):
                    print(tabulate(postEmpleado(), headers="keys", tablefmt="github"))
                elif(opcion == 2):
                    id = input("Ingrese el ID del empleado que desea eliminar: ")
                    print(tabulate(deleteEmpleado(id), headers="keys", tablefmt="github"))
                elif(opcion == 3):
                    id = input("Ingrese el ID del empleado que desea actualizar: ")
                    print(tabulate(updateEmpleado(id), headers="keys", tablefmt="github"))    
                elif(opcion == 0):
                    break

            else:
                print("\nOJO: No existe esa opción, por favor vuelva a intentarlo")

        except ValueError:
            print("""
                  -----------------------------------------------------------------------------
                  Solo se permiten los NÚMEROS ENTEROS correspondientes a la OPCIÓN ESCOGIDA
                                        Por favor, intentelo de nuevo.
                  -----------------------------------------------------------------------------""")
            