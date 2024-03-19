 
from datetime import datetime
from tabulate import tabulate
import json
import requests


def getAllPago(): 
    peticion = requests.get("http://154.38.171.54:5006/pagos")
    data = json.loads(peticion.text) 
    return data
#Cuando haces una solicitud HTTP utilizando requests.get(), 
#el objeto de respuesta que se devuelve contiene varios atributos, 
#uno de los cuales es text. Este atributo contiene el cuerpo de la respuesta HTTP como una cadena de texto Unicode.

#FUNCIÓN 1: 
def getAllPagoYear():
    codigoPagoYear = []
    codigoVisto = set() # set se utiliza para crear un conjunto, que es una colección desordenada y sin elementos duplicados
    for val in getAllPago():
        year = val.get("fecha_pago")[:4] # Se selecciona los primeros 4 caracteres, que corresponden al año
        codigo = val.get("codigo_cliente")
        if year == "2008" and codigo not in codigoVisto:
            codigoPagoYear.append ({
            "Código del cliente": codigo,
            "Fecha del Pago": val.get("fecha_pago")
        })
        codigoVisto.add(codigo) #add se usa para añadir elementos a conjuntos set
        
    return codigoPagoYear


#FUNCIÓN 2: 
def getAllPago2008():
    pago2008 = []
    for val in getAllPago():
        formaPago = val.get("forma_pago")
        yearPago = val.get("fecha_pago")[:4]
        totalPago = val.get("total")
        if formaPago == "PayPal" and yearPago == "2008":
            pago2008.append({
                "Código del Cliente": val.get("codigo_cliente"),
                "Forma de Pago": formaPago,
                "Año del Pago": yearPago,
                "ID de la transacción": val.get("id_transaccion"),
                "Pago": totalPago
            })
    pago2008_ordenado = sorted(pago2008, key=lambda paypalPago: paypalPago["Pago"])
                              # sorted es una función que nos ayuda a ordenar datos
                              # pago2008 es el nombre de nuestro diccionario
                              # lambda  permite definir funciones pequeñas y anónimas en una sola línea de código
                              # paypalPago es el nombre que le di a la variable en la cual se va a guardar y expresar el valor de la clave "Pago"
    return pago2008_ordenado
    



#FUNCIÓN 3:
def getAllFormasPago():
    formasPago = []
    formasPagoVistas = set() 
    for val in getAllPago():
        formasPagoVistas.add(val.get("forma_pago"))
    for val in formasPagoVistas:
        formasPago.append({     
            "Forma de Pago":val
        })
    return formasPago




def menu():
    while True: 
        print("""

                                *****************************
                                       Reportes de Pagos
                                *****************************
    0. Regresar al menú principal     
    1. Obtener los códigos de los clientes que realizaron algún pago en el 2008
    2. Obtener información de todos los pagos que se realizaron en el año 2008 mediante Paypal
    3. Obtener información de las formas de pago





    """)
        opcion = int(input("Seleccione una de las opciones "))
        if opcion == 1:
            print(tabulate(getAllPagoYear(), headers = "keys", tablefmt = "rounded_grid"))
        elif opcion == 2:
            print(tabulate(getAllPago2008(), headers = "keys", tablefmt = "rounded_grid"))
        elif opcion == 3:
            print(tabulate(getAllFormasPago(), headers = "keys", tablefmt = "rounded_grid"))
        elif opcion == 0:
            break