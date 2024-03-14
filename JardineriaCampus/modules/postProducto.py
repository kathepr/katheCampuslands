import os
import json
import requests
from tabulate import tabulate
import modules.getGamas as gG


def postProducto(producto):
    #json-server storage/producto.json -b 5009

    producto = {
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre": input("Ingrese el nombre del producto: "),
        "gama": gG.getAllNombre()[int(input("Seleccione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
        "dimensiones": input("Ingrese las dimensiones del producto: "),
        "proveedor": input("Ingrese el proveedor del producto: "),
        "descripcion": input("Ingrese la descripcion del producto: "),
        "cantidad_en_stock": int(input("Ingrese la cantidad en stock: ")),
        "precio_venta": int(input("Ingrese el precio de ventas: ")),
        "precio_proveedor": int(input("Ingrese el precio del proveedor: "))
    }
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://172.16.100.114:5009", data = json.dumps(producto))
    res = peticion.json()
    res ["Mensaje"] = "Producto Guardado"
    return [res]


def menu():
    while True:
        os.system("clear")
        print("""
        
        ADMINISTRAR DATOS DE PRODUCTOS:

        1. Guardar producto nuevo
        0. Regresar
        
        
        """)

        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(postProducto(), headers="keys", tablefmt="github"))
            input("Presione una tecla para continuar.....")
        elif(opcion == 0):
            break