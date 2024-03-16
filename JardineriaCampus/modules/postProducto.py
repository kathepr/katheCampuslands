import os
import json
import requests
from tabulate import tabulate
import modules.getGamas as gG
import modules.getProducto as gP

def obtener_gama_seleccionada():
    nombres_gama = gG.getAllNombre()

    if not nombres_gama:
        print("No hay nombres de gama disponibles.")
        return None

    print("Seleccione la gama:")
    for i, val in enumerate(nombres_gama):
        print(f"\t{i}. {val}")

    while True:
        opcion = input("Ingrese el número correspondiente a la opción seleccionada: ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 0 <= opcion < len(nombres_gama):
                return nombres_gama[opcion]
            else:
                print("La opción seleccionada no es válida.")
        else:
            print("La entrada no es un número válido.")

def postProducto():
    #json-server storage/producto.json -b 5009
    producto = {
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre": input("Ingrese el nombre del producto: "),
        "gama": obtener_gama_seleccionada(),
        "dimensiones": input("Ingrese la dimensiones del producto: "),
        "proveedor": input("Ingrese el proveedor del producto: "),
        "descripcion": input("Ingrese el descripcion del producto: "),
        "cantidad_en_stock": int(input("Ingrese el cantidad en stock: ")),
        "precio_venta": int(input("Ingrese el precio de ventas: ")),
        "precio_proveedor": int(input("Ingrese el precio del proveedor: "))
    }
    peticion = requests.post("http://192.168.68.115:5009", data = json.dumps(producto)) #Este es el puerto de mi computador
    #peticion = requests.post("http://172.16.100.114:5009", data = json.dumps(producto)) #Campuslands
    res = peticion.json()
    res ["Mensaje"] = "Producto Guardado"
    return [res]


def menu():
    while True:
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