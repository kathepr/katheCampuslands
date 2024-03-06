import storage.pago as pay   

#TOCA CORREGIRLO, PARA QUE LEA LOS PRIMEROS 4 ELEMENTOS DEL AÑO
def getAllPagoYear ():
    codigoPagoYear = []
    for val in pay.pago:
        if val.get("fecha_pago") == "2008":
            codigoPagoYear.append ({
            "codigo_cliente": val.get("codigo_cliente"),
            "fecha_pago": val.get("fecha_pago")
            })
        
    return codigoPagoYear