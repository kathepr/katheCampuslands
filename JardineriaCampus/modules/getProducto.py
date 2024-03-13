from tabulate import tabulate
import storage.producto as pro

#FUNCION 1:
#Devuelve listado con todos los productos que pertenecen a gama Ornamentales
#Que tienen más de 100 unidades en stock
#Listado debe estar ordenado pro precio de venta
#Mostrar en primer lugar los de mayor precio.

def getAllStockPriceGama():
    gamaStock = []
    for val in pro.producto:
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


    """)

        opcion = int(input("Seleccione una de las opciones "))
        if opcion == 1:
            print(tabulate(getAllStockPriceGama(), headers = "keys", tablefmt= "rounded_grid"))
        elif opcion == 0:
            break