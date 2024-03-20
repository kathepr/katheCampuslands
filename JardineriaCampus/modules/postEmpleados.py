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


def menu():
    while True:
        print("""
        
        ADMINISTRAR DATOS DE EMPLEADOS:

        1. Guardar empleado nuevo
        2. Eliminar un empleado
        0. Regresar
        
        
        """)
        opcion = int(input("\nSelecione una de las opciones: "))


        if opcion >=0 and opcion<=2:
            if(opcion == 1):
                print(tabulate(postEmpleado(), headers="keys", tablefmt="github"))
            elif(opcion == 2):
                id = input("Ingrese el ID del producto que desea eliminar: ")
                print(tabulate(deleteEmpleado(id), headers="keys", tablefmt="github"))
                
            elif(opcion == 0):
                break
        input("Presione una tecla para continuar.....")