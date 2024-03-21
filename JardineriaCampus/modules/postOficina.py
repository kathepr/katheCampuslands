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
        "linea_direccion2": input("Ingrese dirección # 2: ")
    }
    url = "http://154.38.171.54:5005/oficinas"
    data = json.dumps(oficina)
    peticion = requests.post(url,data)
    print("\nOficina Guardada")


def deleteOficina(id):
    peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
    if peticion.status_code == 200:
        print("\nOficina Eliminada")


def updateOficina(id):
    oficinaActualizada = {
        "codigo_oficina": input("Ingrese el código de la oficina: "),
        "ciudad": input("Ingrese la ciudad: "),
        "pais": input("Ingrese el pais: "),
        "region": input("Ingrese la región: "),
        "codigo_postal": input("Ingrese el código postal: "),
        "telefono": input("Ingrese el telefono: "),
        "linea_direccion1": input("Ingrese dirección # 1: "),
        "linea_direccion2": input("Ingrese dirección # 2: ")
    }
    url = (f"http://154.38.171.54:5005/oficinas/{id}")
    data = json.dumps(oficinaActualizada)
    peticion = requests.put(url,data)
    if peticion.status_code == 200:
            print("\nOficina Actualizada")


def menu():
    while True:
        print("""
        
        ADMINISTRAR DATOS DE OFICINA:

        1. Guardar oficina nueva
        2. Eliminar una oficina
        3. Actualizar Oficina
        0. Regresar
        
        
        """)
        
        try: 
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion >=0 and opcion<=3:
                if(opcion == 1):
                    print(tabulate(postOficina(), headers="keys", tablefmt="github"))
                elif(opcion == 2):
                    id = input("Ingrese el ID de la oficina que desea eliminar: ")
                    print(tabulate(deleteOficina(id), headers="keys", tablefmt="github"))
                elif(opcion == 3):
                    id = input("Ingrese el ID de la oficina que desea actualizar: ")
                    print(tabulate(updateOficina(id), headers="keys", tablefmt="github"))    
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
            
