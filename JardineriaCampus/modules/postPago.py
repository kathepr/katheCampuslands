import json
import requests
from tabulate import tabulate


def postPago():
    pago = {
            "codigo_cliente": int(input("Ingrese el código del cliente: ")),
            "forma_pago": input("Ingrese la forma de pago: "),
            "id_transaccion": input("Ingrese el código de la transacción: "),
            "fecha_pago": input("Ingrese la fecha de pago (año-mes-día): "),
            "total": int(input("Ingrese el total del pago: ")),
    }
    url = "http://154.38.171.54:5006/pagos"
    data = json.dumps(pago)
    peticion = requests.post(url,data)
    print("\nProducto Guardado")


def deletePago(id):
    peticion=requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
    if peticion.status_code == 200:
            print("\nProducto Eliminado")





def menu():
    while True:
        print("""
        
        ADMINISTRAR DATOS DE PAGO:

        1. Guardar pago nuevo
        2. Eliminar un pago
        0. Regresar
        
        
        """)
        opcion = int(input("\nSelecione una de las opciones: "))


        if opcion >=0 and opcion<=2:
            if(opcion == 1):
                print(tabulate(postPago(), headers="keys", tablefmt="github"))
            elif(opcion == 2):
                id = input("Ingrese el ID del producto que desea eliminar: ")
                print(tabulate(deletePago(id), headers="keys", tablefmt="github"))
                
            elif(opcion == 0):
                break
        input("Presione una tecla para continuar.....")