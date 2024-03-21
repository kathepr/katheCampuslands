import json
import requests
from tabulate import tabulate
import modules.getPedido as datosPedido

def postPedido():
    pedido = {

        "codigo_pedido": int(input("Ingrese el código del pedido: ")),
        "fecha_pedido": input("Ingrese la fecha (año - mes - día): "),
        "fecha_esperada": input("Ingrese la fecha esperada (año-mes-día): "),
        "fechaEntrega": input("Ingrese la fecha de entrega (año-mes-día): "),
        "estado": input("Ingrese estado del pedido: "),
        "comentario": input("Ingrese comentarios: "),
        "codigo_cliente": int(input("Ingrese el código del cliente: ")),
        }
    url = "http://154.38.171.54:5007/pedidos"
    data = json.dumps(pedido)
    peticion = requests.post(url,data)
    print("\nPedido Guardado")




def deletePedido(id):
    peticion = requests.delete(f"http://154.38.171.54:5007/pedidos/{id}")
    if peticion.status_code == 200:
        print("\nPedido Eliminado")


def updatePedido(id):
    pedidoActualizado = {

        "codigo_pedido": int(input("Ingrese el código del pedido: ")),
        "fecha_pedido": input("Ingrese la fecha (año - mes - día): "),
        "fecha_esperada": input("Ingrese la fecha esperada (año-mes-día): "),
        "fechaEntrega": input("Ingrese la fecha de entrega (año-mes-día): "),
        "estado": input("Ingrese estado del pedido: "),
        "comentario": input("Ingrese comentarios: "),
        "codigo_cliente": int(input("Ingrese el código del cliente: ")),
        }
    
    url = (f"http://154.38.171.54:5007/pedidos/{id}")
    data = json.dumps(pedidoActualizado)
    peticion = requests.put(url,data)
    if peticion.status_code == 200:
        print("\nPedido Actualizado")



def menu():
    while True:
        print("""
        
        ADMINISTRAR DATOS DE PEDIDOS:

        1. Guardar un pedido nuevo
        2. Eliminar un pedido
        3. Actualizar pedido
        0. Regresar
        
        
        """)
        
        try: 
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion >=0 and opcion<=3:
                if(opcion == 1):
                    print(tabulate(postPedido(), headers="keys", tablefmt="github"))
                elif(opcion == 2):
                    id = input("Ingrese el ID del pedido que desea eliminar: ")
                    print(tabulate(deletePedido(id), headers="keys", tablefmt="github"))
                elif opcion == 3:
                    id = input("Ingrese el ID del pedido que desea actualizar: ")
                    print(tabulate(updatePedido(id), headers="keys", tablefmt = "github"))    
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
            

    