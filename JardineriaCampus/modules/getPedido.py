from datetime import datetime
import storage.pedido as ped

def getEstadoPedido ():
    estadoPedido = []
    for val in ped.pedido: 
        estados = ({
            "estado": val.get("estado")
        })
        estadoPedido.append(estados)
    return (estadoPedido)



def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregados = []

    for val in ped.pedido:
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
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_cliente": val.get("codigo cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_entrega": val.get("fecha_entrega")
                })
    return pedidosEntregados



def getAllPedidoEntregadoDosDiasAntes():
    pedidoEntregadoAntes = []

    for val in ped.pedido:
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
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_cliente": val .get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_entrega": val.get("fecha_entrega")
                    })
    return pedidoEntregadoAntes



def getAllPedidosRechazados():
    pedidoRechazado = []

    for val in ped.pedido:
        if val.get("estado") == "Rechazado" and val.get("fecha_entrega") is not None:
            if val.get("fecha_entrega")[:4] == "2009":
                pedidoRechazado.append (val)
    return pedidoRechazado


def getAllPedidosEnero():
    pedidoEnero = []

    for val in ped.pedido:
        if val.get("estado") == "Entregado":
            if val.get("fecha_entrega") is not None and val.get("fecha_entrega")[5:7] == "01":
                pedidoEnero.append(val)
    return pedidoEnero