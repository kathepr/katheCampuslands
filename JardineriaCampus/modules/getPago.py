import storage.pago as pay   
from datetime import datetime

def getAllPagoYear():
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



def getAllFormasPago():
    formasPago = []
    formasPagoVistas = set()
    for val in pay.pago:
        formasPago.append ({
            "Forma de Pago":val.get("forma_pago")
        }) 
        formasPagoVistas.add(val.get("forma_pago"))
    return formasPagoVistas