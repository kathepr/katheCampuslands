import storage.pedido as ped

def getEstadoPedido ():
    estadoPedido = []
    for val in ped.pedido: 
        estados = ({
            "estado": val.get("estado")
        })
        estadoPedido.append(estados)
    return (estadoPedido)