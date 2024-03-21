import json
import requests
from tabulate import tabulate
import re



def validar_input(patron, mensaje):
    while True: 
        entrada = input(mensaje)
        if patron.match(entrada):
            confirmacion = input(f"¿Confirma el ingreso de este dato '{entrada}'? (S/N) ").strip().lower()
            if confirmacion == "s":
                return entrada
        else:
            print("El dato no cumple con los parametros establecidos. Vuelva a intentarlo.")



def postPago():

#Expresiones regulares para cada dato: 
    codigoClienteR = re.compile(r'^[0-9]+$')
    formaPagoR = re.compile(r'^[A-Za-z]+$')
    idTransaccionR = re.compile(r'^[a-z]{2}-[a-z]{3}-[0-9]{6}+$') 
    fechaPagoR = re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$')
    totalR = re.compile(r'^[0-9]+$')
    

#Obtener los datos del usuario: 
    codigo_cliente = int(validar_input(codigoClienteR, "Ingrese el código del cliente: "))
    forma_pago = validar_input(formaPagoR, "Ingrese la forma de pago: ")
    id_transaccion = validar_input(idTransaccionR, "Ingrese el código de la transacción: ")
    fecha_pago = validar_input(fechaPagoR, "Ingrese la fecha de pago (año-mes-día): ")
    total = int(validar_input(totalR, "Ingrese el total del pago: "))


    pago = {
            "codigo_cliente": codigo_cliente,
            "forma_pago": forma_pago,
            "id_transaccion": id_transaccion,
            "fecha_pago": fecha_pago,
            "total": total
    }
    
    url = "http://154.38.171.54:5006/pagos"
    data = json.dumps(pago)
    peticion = requests.post(url,data)
    print("\nPago Guardado")


def deletePago(id):
    peticion=requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
    if peticion.status_code == 200:
            print("\nPago Eliminado")


def updatePago(id):


#Expresiones regulares para cada dato: 
    codigoClienteR = re.compile(r'^[0-9]+$')
    formaPagoR = re.compile(r'^[A-Za-z]+$')
    idTransaccionR = re.compile(r'^[a-z]{2}-[a-z]{3}-[0-9]{6}+$') 
    fechaPagoR = re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$')
    totalR = re.compile(r'^[0-9]+$')
    

#Obtener los datos del usuario: 
    codigo_cliente = int(validar_input(codigoClienteR, "Ingrese el código del cliente: "))
    forma_pago = validar_input(formaPagoR, "Ingrese la forma de pago: ")
    id_transaccion = validar_input(idTransaccionR, "Ingrese el código de la transacción: ")
    fecha_pago = validar_input(fechaPagoR, "Ingrese la fecha de pago (año-mes-día): ")
    total = int(validar_input(totalR, "Ingrese el total del pago: "))


    pagoActualizado = {
            "codigo_cliente": codigo_cliente,
            "forma_pago": forma_pago,
            "id_transaccion": id_transaccion,
            "fecha_pago": fecha_pago,
            "total": total
    }
    url = (f"http://154.38.171.54:5006/pagos/{id}")
    data = json.dumps(pagoActualizado)
    peticion = requests.put(url,data)
    if peticion.status_code == 200:
        print("\nPago Actualizado")


def menu():
    while True:
        print("""
        ********************************
            ADMINISTRAR DATOS DE PAGO:
        ********************************
              
        1. Guardar pago nuevo
        2. Eliminar un pago
        3. Actualizar un pago
        0. Regresar
        
        
        """)
        

        try: 
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion >=0 and opcion<=3:
                if(opcion == 1):
                    print(tabulate(postPago(), headers="keys", tablefmt="github"))
                elif(opcion == 2):
                    id = input("Ingrese el ID del pago que desea eliminar: ")
                    print(tabulate(deletePago(id), headers="keys", tablefmt="github"))
                elif(opcion == 3):
                    id = input("Ingrese el ID del pago que desea actualizar: ")
                    print(tabulate(updatePago(id), headers="keys", tablefmt="github"))
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
            
