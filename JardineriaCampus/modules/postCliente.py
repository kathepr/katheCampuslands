import json
import requests
from tabulate import tabulate



def postCliente():
    cliente = {
        "codigo_cliente": int(input("Ingrese el código del cliente: ")),
        "nombre_cliente": input("Ingrese el nombre del cliente: "),
        "nombre_contacto": input("Ingrese el nombre del contacto: "),
        "apellido_contacto": input("Ingrese el apellido del contacto: "),
        "telefono": input("Ingrese el número de telefono: "),
        "fax": input("Ingrese el número de fax: "),
        "linea_direccion1": input("Ingrese la dirección 1: "),
        "linea_direccion2": input("Ingrese la dirección 1: "),
        "ciudad": input("Ingrese la ciudad: "),
        "region": input("Ingrese la región: "),
        "pais": input("Ingrese el pais: "),
        "codigo_postal": input("Ingrese el código postal: "),
        "codigo_empleado_rep_ventas": int(input("Ingrese el código del representante de ventas: ")),
        "limite_credito": int(input("Ingrese el limite de crédito: "))
    }
    url = "http://154.38.171.54:5001/cliente"
    data = json.dumps(cliente)
    peticion = requests.post(url,data)
    print("\nCliente Guardado")
    

def deleteCliente(id):
    peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
    if peticion.status_code == 200:
        print("\nCliente Eliminado")


def updateCliente(id):
    clienteActualizado = {
        "codigo_cliente": int(input("Ingrese el código del cliente: ")),
        "nombre_cliente": input("Ingrese el nombre del cliente: "),
        "nombre_contacto": input("Ingrese el nombre del contacto: "),
        "apellido_contacto": input("Ingrese el apellido del contacto: "),
        "telefono": input("Ingrese el número de telefono: "),
        "fax": input("Ingrese el número de fax: "),
        "linea_direccion1": input("Ingrese la dirección 1: "),
        "linea_direccion2": input("Ingrese la dirección 1: "),
        "ciudad": input("Ingrese la ciudad: "),
        "region": input("Ingrese la región: "),
        "pais": input("Ingrese el pais: "),
        "codigo_postal": input("Ingrese el código postal: "),
        "codigo_empleado_rep_ventas": int(input("Ingrese el código del representante de ventas: ")),
        "limite_credito": int(input("Ingrese el limite de crédito: "))
    }
    url = (f"http://154.38.171.54:5001/cliente/{id}")
    data = json.dumps(clienteActualizado)
    peticion = requests.put(url, data)
    if peticion.status_code == 200:
            print("\nCliente Actualizado")




def menu():
    while True:
        print("""
        
        ADMINISTRAR DATOS DE CLIENTES:

        1. Guardar cliente nuevo
        2. Eliminar un cliente
        3. Actualizar un cliente
        0. Regresar
        
        
        """)
        opcion = int(input("\nSelecione una de las opciones: "))


        if opcion >=0 and opcion<=3:
            if(opcion == 1):
                print(tabulate(postCliente(), headers="keys", tablefmt="github"))
            elif(opcion == 2):
                id = input("Ingrese el ID del cliente que desea eliminar: ")
                print(tabulate(deleteCliente(id), headers="keys", tablefmt="github"))
            elif(opcion == 3):
                id = input("Ingrese el ID del cliente que desea actualizar: ")
                print(tabulate(updateCliente(id), headers="keys", tablefmt="github"))    
            elif(opcion == 0):
                break
        input("Presione una tecla para continuar.....")