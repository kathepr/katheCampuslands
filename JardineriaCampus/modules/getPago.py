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



def getAllPago2008():
    pago2008 = []
    for val in pay.pago:
        formaPago = val.get("forma_pago")
        yearPago = val.get("fecha_pago")[:4]
        totalPago = val.get("total")
        if formaPago == "PayPal" and yearPago == "2008":
            pago2008.append({
                "Pago": totalPago
            })
    pago2008_ordenado = sorted(pago2008, key=lambda paypalPago: paypalPago["Pago"])
                              # sorted es una función que nos ayuda a ordenar datos
                              # pago2008 es el nombre de nuestro diccionario
                              # lambda  permite definir funciones pequeñas y anónimas en una sola línea de código
                              # paypalPago es el nombre que le di a la variable en la cual se va a guardar y expresar el valor de la clave "Pago"
    return pago2008_ordenado
    






def getAllFormasPago():
    formasPago = []
    formasPagoVistas = set() 
    for val in pay.pago:
        formasPagoVistas.add(val.get("forma_pago"))
    for val in formasPagoVistas:
        formasPago.append({     
            "metodo_pago":val
        })
    return formasPago

