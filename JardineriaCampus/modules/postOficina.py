import json
import requests
from tabulate import tabulate


def postOficina():
    oficina = {
        "codigo_oficina": input("Ingrese el código de la oficina: "),
        "ciudad": input("Ingrese la ciudad: "),
        "pais": input("Ingrese el pais: "),
        "region": input("Ingrese la región: "),
        "codigo_postal": input("Ingrese el código postal: "),
        "telefono": input("Ingrese el telefono: "),
        "linea_direccion1": input("Ingrese dirección # 1: "),
        "linea_direccion2": input("Ingrese dirección # 2: "),
    }
    url = "http://154.38.171.54:5005/oficinas"
    data = json.dumps(oficina)
    peticion = requests.post(url,data)
    print("\nProducto Guardado")


def deleteOficina(id):
    peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
    if peticion.status_code == 200:
        print("\nProducto Eliminado")






def menu():
    while True:
        print("""
        
        ADMINISTRAR DATOS DE OFICINA:

        1. Guardar oficina nueva
        2. Eliminar una oficina
        0. Regresar
        
        
        """)
        opcion = int(input("\nSelecione una de las opciones: "))


        if opcion >=0 and opcion<=2:
            if(opcion == 1):
                print(tabulate(postOficina(), headers="keys", tablefmt="github"))
            elif(opcion == 2):
                id = input("Ingrese el ID del producto que desea eliminar: ")
                print(tabulate(deleteOficina(id), headers="keys", tablefmt="github"))
                
            elif(opcion == 0):
                break
        input("Presione una tecla para continuar.....")