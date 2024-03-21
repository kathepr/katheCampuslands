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



def postOficina():

#Expresiones regulares para cada dato:
    codigoOficinaR = re.compile(r'^[A-Z]{3}-[A-Z]{2,3}$')
    ciudadR = re.compile(r'^[A-Za-z\s]$')
    paisR = re.compile (r'^[A-Za-z]$')
    regionR = re.compile (r'^[A-Za-z\s-]+$')
    codigoPostalR= re.compile (r'^[a-zA-Z\w\s-]+$')
    telefonoR = re.compile (r'^\+\d+(\s\d+)*$')
    direccion1R= re.compile (r'^[^\n]+$')
    direccion2R= re.compile (r'^[^\n]+$')

#Obtener los datos del usuario:
    codigo_oficina = validar_input(codigoOficinaR, "Ingrese el código de la oficina: ")
    ciudad = validar_input(ciudadR, "Ingrese la ciudad: ")
    pais = validar_input(paisR, "Ingrese el pais: ")
    region = validar_input(regionR, "Ingrese la región: ")
    codigo_postal = validar_input(codigoPostalR, "Ingrese el código postal: ")
    telefono = validar_input(telefonoR, "Ingrese el telefono: ")
    direccion1 = validar_input(direccion1R, "Ingrese dirección # 1: ")
    direccion2= validar_input(direccion2R, "Ingrese dirección # 2: ")

    oficina = {
        "codigo_oficina": codigo_oficina,
        "ciudad": ciudad,
        "pais": pais,
        "region": region,
        "codigo_postal": codigo_postal,
        "telefono": telefono,
        "linea_direccion1": direccion1,
        "linea_direccion2": direccion2
    }
    
    url = "http://154.38.171.54:5005/oficinas"
    data = json.dumps(oficina)
    peticion = requests.post(url,data)
    print("\nOficina Guardada")


def deleteOficina(id):
    peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
    if peticion.status_code == 200:
        print("\nOficina Eliminada")


def updateOficina(id):

#Expresiones regulares para cada dato:
    codigoOficinaR = re.compile(r'^[A-Z]{3}-[A-Z]{2,3}$')
    ciudadR = re.compile(r'^[A-Za-z\s]$')
    paisR = re.compile (r'^[A-Za-z]$')
    regionR = re.compile (r'^[A-Za-z\s-]+$')
    codigoPostalR= re.compile (r'^[a-zA-Z\w\s-]+$')
    telefonoR = re.compile (r'^\+\d+(\s\d+)*$')
    direccion1R= re.compile (r'^[^\n]+$')
    direccion2R= re.compile (r'^[^\n]+$')

#Obtener los datos del usuario:
    codigo_oficina = validar_input(codigoOficinaR, "Ingrese el código de la oficina: ")
    ciudad = validar_input(ciudadR, "Ingrese la ciudad: ")
    pais = validar_input(paisR, "Ingrese el pais: ")
    region = validar_input(regionR, "Ingrese la región: ")
    codigo_postal = validar_input(codigoPostalR, "Ingrese el código postal: ")
    telefono = validar_input(telefonoR, "Ingrese el telefono: ")
    direccion1 = validar_input(direccion1R, "Ingrese dirección # 1: ")
    direccion2= validar_input(direccion2R, "Ingrese dirección # 2: ")



    oficinaActualizada = {
        "codigo_oficina": codigo_oficina,
        "ciudad": ciudad,
        "pais": pais,
        "region": region,
        "codigo_postal": codigo_postal,
        "telefono": telefono,
        "linea_direccion1": direccion1,
        "linea_direccion2": direccion2
    }

    url = (f"http://154.38.171.54:5005/oficinas/{id}")
    data = json.dumps(oficinaActualizada)
    peticion = requests.put(url,data)
    if peticion.status_code == 200:
            print("\nOficina Actualizada")


def menu():
    while True:
        print("""
        ***********************************
            ADMINISTRAR DATOS DE OFICINA:
        ***********************************

        1. Guardar oficina nueva
        2. Eliminar una oficina
        3. Actualizar Oficina
        0. Regresar
        
        
        """)
        
        try: 
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion >=0 and opcion<=3:
                if(opcion == 1):
                    print(tabulate(postOficina(), headers="keys", tablefmt="github"))
                elif(opcion == 2):
                    id = input("Ingrese el ID de la oficina que desea eliminar: ")
                    print(tabulate(deleteOficina(id), headers="keys", tablefmt="github"))
                elif(opcion == 3):
                    id = input("Ingrese el ID de la oficina que desea actualizar: ")
                    print(tabulate(updateOficina(id), headers="keys", tablefmt="github"))    
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
            
