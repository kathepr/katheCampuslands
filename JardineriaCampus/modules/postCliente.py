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






def postCliente():


#Expresiones regulares para cada dato:
    codigoEmpleadoR = re.compile(r'^[0-9]+$')
    nombreClienteR = re.compile(r'^[A-Za-z\s]+$')
    nombreContactoR = re.compile(r'^[A-Za-z\s]+$')
    apellidoContactoR = re.compile(r'^[A-Za-z]+$')
    telefonoR = re.compile(r'^\d+(\s*\d+)*$')
    faxR = re.compile(r'^\d+(\s*\d+)*$')
    direccion1R = re.compile(r'^[^\n]+$')
    direccion2R = re.compile(r'^[^\n]+$')
    ciudadR = re.compile(r'^[A-Za-z\s]+$') 
    regionR = re.compile(r'^[A-Za-z\s]+$')
    paisR = re.compile(r'^[A-Za-z\s]+$')
    codigoPostalR = re.compile(r'^[0-9]+$')
    codigoRepVentasR = re.compile(r'^[0-9]+$')
    limiteCreditoR = re.compile(r'^[0-9]+(\.[0-9]+)?$')

#Obtener los datos del usuario: 
    codigo_cliente = int(validar_input(codigoEmpleadoR, "Ingrese el código del cliente: "))
    nombre_cliente = validar_input(nombreClienteR, "Ingrese el nombre del cliente: ")
    nombre_contacto = validar_input(nombreContactoR, "Ingrese el nombre del contacto: ")
    apellido_contacto = validar_input(apellidoContactoR, "Ingrese el apellido del contacto: ")
    telefono = validar_input(telefonoR, "Ingrese el número de telefono: ")
    fax = validar_input(faxR, "Ingrese el número de fax: ")
    direccion1 = validar_input(direccion1R, "Ingrese la dirección 1: ")
    direccion2 = validar_input(direccion2R, "Ingrese la dirección 2: ")
    ciudad = validar_input(ciudadR, "Ingrese la ciudad: ")
    region = validar_input(regionR, "Ingrese la región: ")
    pais = validar_input(paisR, "Ingrese el pais: ")
    codigo_postal = validar_input(codigoPostalR, "Ingrese el código postal: ")
    codigo_repVentas = int(validar_input(codigoRepVentasR, "Ingrese el código del representante de ventas: "))
    limite_credito = int(validar_input(limiteCreditoR, "Ingrese el limite de crédito: "))



    cliente = {
        "codigo_cliente": codigo_cliente,
        "nombre_cliente": nombre_cliente,
        "nombre_contacto": nombre_contacto,
        "apellido_contacto": apellido_contacto,
        "telefono": telefono,
        "fax": fax,
        "linea_direccion1": direccion1,
        "linea_direccion2": direccion2,
        "ciudad": ciudad,
        "region": region,
        "pais": pais,
        "codigo_postal": codigo_postal,
        "codigo_empleado_rep_ventas": codigo_repVentas,
        "limite_credito": limite_credito
    }
    
    url = "http://154.38.171.54:5001/cliente"
    data = json.dumps(cliente)
    peticion = requests.post(url,data)
    print("\nCliente Guardado")
    

def deleteCliente(id):
    peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
    if peticion.status_code == 200:
        print("\nCliente Eliminado")


def updateCliente(id):


#Expresiones regulares para cada dato:
    codigoEmpleadoR = re.compile(r'^[0-9]+$')
    nombreClienteR = re.compile(r'^[A-Za-z\s]+$')
    nombreContactoR = re.compile(r'^[A-Za-z\s]+$')
    apellidoContactoR = re.compile(r'^[A-Za-z]+$')
    telefonoR = re.compile(r'^\d+(\s*\d+)*$')
    faxR = re.compile(r'^\d+(\s*\d+)*$')
    direccion1R = re.compile(r'^[^\n]+$')
    direccion2R = re.compile(r'^[^\n]+$')
    ciudadR = re.compile(r'^[A-Za-z\s]+$') 
    regionR = re.compile(r'^[A-Za-z\s]+$')
    paisR = re.compile(r'^[A-Za-z\s]+$')
    codigoPostalR = re.compile(r'^[0-9]+$')
    codigoRepVentasR = re.compile(r'^[0-9]+$')
    limiteCreditoR = re.compile(r'^[0-9]+(\.[0-9]+)?$')

#Obtener los datos del usuario: 
    codigo_cliente = int(validar_input(codigoEmpleadoR, "Ingrese el código del cliente: "))
    nombre_cliente = validar_input(nombreClienteR, "Ingrese el nombre del cliente: ")
    nombre_contacto = validar_input(nombreContactoR, "Ingrese el nombre del contacto: ")
    apellido_contacto = validar_input(apellidoContactoR, "Ingrese el apellido del contacto: ")
    telefono = validar_input(telefonoR, "Ingrese el número de telefono: ")
    fax = validar_input(faxR, "Ingrese el número de fax: ")
    direccion1 = validar_input(direccion1R, "Ingrese la dirección 1: ")
    direccion2 = validar_input(direccion2R, "Ingrese la dirección 2: ")
    ciudad = validar_input(ciudadR, "Ingrese la ciudad: ")
    region = validar_input(regionR, "Ingrese la región: ")
    pais = validar_input(paisR, "Ingrese el pais: ")
    codigo_postal = validar_input(codigoPostalR, "Ingrese el código postal: ")
    codigo_repVentas = int(validar_input(codigoRepVentasR, "Ingrese el código del representante de ventas: "))
    limite_credito = int(validar_input(limiteCreditoR, "Ingrese el limite de crédito: "))




    clienteActualizado = {
        "codigo_cliente": codigo_cliente,
        "nombre_cliente": nombre_cliente,
        "nombre_contacto": nombre_contacto,
        "apellido_contacto": apellido_contacto,
        "telefono": telefono,
        "fax": fax,
        "linea_direccion1": direccion1,
        "linea_direccion2": direccion2,
        "ciudad": ciudad,
        "region": region,
        "pais": pais,
        "codigo_postal": codigo_postal,
        "codigo_empleado_rep_ventas": codigo_repVentas,
        "limite_credito": limite_credito
    }

    url = (f"http://154.38.171.54:5001/cliente/{id}")
    data = json.dumps(clienteActualizado)
    peticion = requests.put(url, data)
    if peticion.status_code == 200:
            print("\nCliente Actualizado")




def menu():
    while True:
        print("""
        **************************************
            ADMINISTRAR DATOS DE CLIENTES:
        **************************************

        1. Guardar cliente nuevo
        2. Eliminar un cliente
        3. Actualizar un cliente
        0. Regresar
        
        
        """)
        
        try: 
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion >=0 and opcion<=3:
                if(opcion == 1):
                    print(tabulate(postCliente(), headers="keys", tablefmt="github"))
                elif(opcion == 2):
                    id = input("Ingrese el ID del cliente que desea eliminar: ")
                    print(tabulate(deleteCliente(id), headers="keys", tablefmt="github"))
                elif(opcion == 3):
                    id = input("Ingrese el ID del cliente que desea actualizar: ")
                    print(tabulate(updateCliente(id), headers="keys", tablefmt="github"))    
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
            

    