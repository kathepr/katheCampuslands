from tabulate import tabulate
import requests
import json
import os

#FUNCION 1:
# Devuelve listado con todos los productos que pertenecen a gama Ornamentales
# Que tienen más de 100 unidades en stock
# Listado debe estar ordenado pro precio de venta
# Mostrar en primer lugar los de mayor precio.
def getAllProducto():
    peticion = requests.get("http://154.38.171.54:5008/producto")
    data = json.dumps(peticion.json(), indent = 4)


def getProductoCodigo(codigo):
    peticion = requests.get(f"http://154.38.171.54:5008/producto{codigo}")
    return [peticion.json()] if peticion.ok else []

def getAllStockPriceGama(gama, stock):
    condiciones = []
    for val in getAllProducto():
        if(val.get("gama") == gama and val.get("cantidad_en_stock") >= stock):
            condiciones.append(val)
    def price(val):
        return val.get("precio_venta")    
    condiciones.sort(key=price, reverse=True)
    for i, val in enumerate(condiciones):
        condiciones[i] = {
                "codigo": val.get("codigo_producto"),
                "venta": val.get("precio_venta"),
                "nombre": val.get("nombre"),
                "gama": val.get("gama"),
                "dimensiones": val.get("dimensiones"),
                "proveedor": val.get("proveedor"),
                "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else None,
                "stock": val.get("cantidad_en_stock"),
                "base": val.get("precio_proveedor")
            }
    return condiciones



def menu():
    
    while True: 
        print("""

                                *****************************
                                    Reportes de Productos
                                *****************************
    0. Regresar al menú principal     
    1. Obtener todos los productos de una categoría ordenando sus precios de venta, también que su cantidad de inventario sea superior (ejem: Ornamentales, 100)

    """)

        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            gama = input("Ingrese la gama que deseas filtrar: ")
            stock = int(input("Ingrese las unidades que seas mostrar: "))
            print(tabulate(getAllStockPriceGama(gama, stock), headers="keys", tablefmt="rounded_grid"))
        elif(opcion == 0):
            break