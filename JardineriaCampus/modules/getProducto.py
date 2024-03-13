from tabulate import tabulate
import json
import requests
import modules.postProducto as psProducto
import modules.getGamas as gG

#FUNCION 1:
#Devuelve listado con todos los productos que pertenecen a gama Ornamentales
#Que tienen más de 100 unidades en stock
#Listado debe estar ordenado pro precio de venta
#Mostrar en primer lugar los de mayor precio.
def getAllData():
    #json-server storage/producto.json -b 5009
    peticion = requests.get("Remote: http://172.16.100.114:5009")
    data = peticion.json()
    return(data)



def getAllStockPriceGama():
    gamaStock = []
    for val in getAllData():
        if val.get("gama") == "Ornamentales" and val.get("cantidad_en_stock") >= 100:
            gamaStock.append({
            "Código del Producto": val.get("codigo_producto"),
            "Nombre del Producto": val.get("nombre"),
            "Gama": val.get("gama"),
            "Dimensiones": val.get("dimensiones"),
            "Proveedor": val.get("proveedor"),
            "Cantidad en Stock": val.get("cantidad_en_stock"),
            "Precio de Venta": val.get("precio_venta"),
            "Precio Proveedor": val.get("precio_proveedor")
        })
    gamaStockordenada= sorted(gamaStock, key=lambda precio: precio["Precio de Venta"], reverse = True)
    return gamaStockordenada



def menu():
    while True: 
        print("""

                                *****************************
                                    Reportes de Productos
                                *****************************
    0. Regresar al menú principal     
    1. Obtener productos de gama Ornamentales con más de 100 unidades en Stock
    2. Añadir producto personalizado a lista de productos

    """)

        opcion = int(input("Seleccione una de las opciones "))
        if opcion == 1:
            print(tabulate(getAllStockPriceGama(), headers = "keys", tablefmt= "rounded_grid"))
        elif(opcion == 2):
            producto = {
                "codigo_producto": input("Ingrese el codigo del producto: "),
                "nombre": input("Ingrese el nombre del producto: "),
                "gama": input("\t\n".join([f"{i}. {val}" for i, val in enumerate(gG.getAllNombre())])),
                "dimensiones": input("Ingrese las dimensiones del producto: "),
                "proveedor": input("Ingrese el proveedor del producto: "),
                "descripcion": input("Ingrese la descripción del producto: "),
                "cantidad_en_stock": int(input("Ingrese la cantidad en stock: ")),
                "precio_venta": int(input("Ingrese el precio de venta del producto: ")),
                "precio_proveedor": int(input("Ingrese el precio del proveedor: "))
            }
            psProducto.postProducto(producto)
            print("Producto Guardado")
        elif opcion == 0:
            break