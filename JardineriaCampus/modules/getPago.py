import storage.pago as pay   
from datetime import datetime

def getAllPagoYear ():
    codigoPagoYear = []
    codigoVisto = set() # set se utiliza para crear un conjunto, que es una colección desordenada y sin elementos duplicados
    for val in pay.pago:
        year = val.get("fecha_pago")[:4] # Se selecciona los primeros 4 caracteres, que corresponden al año
        codigo = val.get("codigo_cliente")
        if year == "2008" and codigo not in codigoVisto:
            codigoPagoYear.append ({
            "codigo_cliente": codigo,
            "fecha_pago": val.get("fecha_pago")
        })
        codigoVisto.add(codigo) #add se usa para añadir elementos a conjuntos set
        
    return codigoPagoYear


def getAllPagosPaypalYear():
    pagoPaypalYear = []
    
    for val in pay.pago:
        fecha_pago = val.get("fecha_pago")
        forma_pago = val.get("forma_pago")
        if fecha_pago is not None:
            fecha_pago_dt = datetime.strptime(fecha_pago, '%Y-%m-%d')
            if fecha_pago_dt.year == "2008" and forma_pago == "Paypal":
                pagoPaypalYear.append(val)

    return pagoPaypalYear