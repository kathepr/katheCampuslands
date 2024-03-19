from tabulate import tabulate
from datetime import datetime
import requests
import json



def getAllPedido():
    peticion = requests.get("http://154.38.171.54:5007/pedidos")
    data = json.loads(peticion.text)
    return data


#FUNCION 1: 
def getEstadoPedido ():
    estadoPedido = []
    estados = set()
    for val in getAllPedido(): 
        estados.add(val.get("estado"))
    for val in estados:
        estadoPedido.append({
            "Estados": val
        })
    return (estadoPedido)



#FUNCIÓN 2: 
def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregados = []

    for val in getAllPedido():
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
                
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])

            start = datetime.strptime(date_1, "%d/%m/%Y")
            end =   datetime.strptime(date_2, "%d/%m/%Y")

            diff = end.date() - start.date()

            if diff.days < 0:
                pedidosEntregados.append({
                    "Código del pedido": val.get("codigo_pedido"),
                    "Código del cliente": val.get("codigo_cliente"),
                    "Fecha esperada": val.get("fecha_esperada"),
                    "Fecha de entrega": val.get("fecha_entrega")
                })
    return pedidosEntregados


#FUNCIÓN 3: 
def getAllPedidoEntregadoDosDiasAntes():
    pedidoEntregadoAntes = []

    for val in getAllPedido():
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")

        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            date_2 = "/".join(val.get ("fecha_entrega").split ("-")[::-1])

            start = datetime.strptime(date_2, "%d/%m/%Y")
            end = datetime.strptime(date_1, "%d/%m/%Y")
        
            diff = end.date() - start.date()
            

            if diff.days >= 2:
                pedidoEntregadoAntes.append({
                    "Código del pedido": val.get("codigo_pedido"),
                    "Código del cliente": val .get("codigo_cliente"),
                    "Fecha esperada": val.get("fecha_esperada"),
                    "Fecha de entrega": val.get("fecha_entrega")
                    })
    return pedidoEntregadoAntes


#FUNCION 4:
def getAllPedidosRechazados():
    pedidoRechazado = []

    for val in getAllPedido():
        if val.get("estado") == "Rechazado" and val.get("fecha_entrega") is not None:
            if val.get("fecha_entrega")[:4] == "2009":
                pedidoRechazado.append({
                    "Código del pedido": val.get("codigo_pedido"),
                    "Fecha del pedido": val.get("fecha_pedido"),
                    "Fecha esperada": val.get("fecha_esperada"),
                    "Fecha de entrega": val.get("fecha_entrega"),
                    "Estado": val.get("estado"),
                    "Comentarios": val.get("comentario"),
                    "Código del cliente": val .get("codigo_cliente")
                    })
    return pedidoRechazado


#FUNCIÓN 5:
def getAllPedidosEnero():
    pedidoEnero = []

    for val in getAllPedido():
        if val.get("estado") == "Entregado":
            if val.get("fecha_entrega") is not None and val.get("fecha_entrega")[5:7] == "01":
                pedidoEnero.append({
                    "Código del pedido": val.get("codigo_pedido"),
                    "Fecha del pedido": val.get("fecha_pedido"),
                    "Fecha esperada": val.get("fecha_esperada"),
                    "Fecha de entrega": val.get("fecha_entrega"),
                    "Estado": val.get("estado"),
                    "Comentarios": val.get("comentario"),
                    "Código del cliente": val.get("codigo_cliente")
                })
    return pedidoEnero



def menu():
    while True:
        print("""

                        ***********************************
                                Reportes de Pedidos
                        ***********************************

    0. Regresar al menú principal. 
    1. Obtener información de los distintos estados por los que puede pasar un pedido
    2. Obtener información de los pedidos entregados pero que experimentaron retrasos en la entrega
    3. Obtener información de los pedidos entregados que llegaron antes de la fecha estimada
    4. Obtener información de los pedidos rechazados en el 2009
    5. Obtener información de los pedidos entregados en el mes de enero de cualquier año
          


     """)

        opcion = int(input("Seleccione una de las opciones "))
        if opcion == 1:
            print(tabulate(getEstadoPedido(), headers = "keys", tablefmt = "rounded_grid"))
        elif opcion ==2:
            print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers = "keys", tablefmt = "rounded_grid"))
        elif opcion ==3:
            print(tabulate(getAllPedidoEntregadoDosDiasAntes(), headers = "keys", tablefmt = "rounded_grid"))
        elif opcion == 4:
            print(tabulate(getAllPedidosRechazados(), headers = "keys", tablefmt = "rounded_grid"))
        elif opcion == 5:
            print(tabulate(getAllPedidosEnero(), headers = "keys", tablefmt = "rounded_grid"))
        elif opcion == 0:
            break