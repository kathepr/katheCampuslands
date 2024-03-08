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
            pago2008_ordenado = sorted(pago2008, key=lambda x: x["Pago"])
                              # sorted es una función que nos ayuda a ordenar datos
                              # pago2008 es el nombre de nuestro diccionario
                              # key=lambda x: x["Pago"], estamos diciendo que queremos ordenar la lista según el valor asociado con la clave "Pago" 
                              # Con sorted se usa key. Y key se usa cuando quieres ordenar diccionarios u objetos personalizados, 
                              # basandote en una característica de esos objetos, entonces usarías key para especificar cómo deseas que se realice el ordenamiento.
                              # lambda  permite definir funciones pequeñas y anónimas en una sola línea de código
                              # lambda es especialmente útil cuando necesitas una función rápida y desechable, como en este caso donde solo la usamos para el 
                              # propósito específico de ordenar una lista de diccionarios por un campo específico
                              # x: Es el argumento que recibe la función. En este caso, x representa cada elemento de la lista pago2008 que estamos ordenando.
                              # x["Pago"]: Esto significa que queremos acceder al valor asociado con la clave "Pago" en el diccionario x (puede haber muchos diccionarios, dentro de otro diccionarios). 
                              # Es por eso que x, representaria uno de esos diccionarios x, "Pago" es una clave que tiene asociado un valor. Entonces, x["Pago"] extrae ese valor.
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

