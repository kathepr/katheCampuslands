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



def postEmpleado():
#Expresiones regulares para cada dato: 
    codigoEmpleadoR = re.compile(r'^[0-9]+$')
    nombreR = re.compile(r'^[A-Za-z]+$')
    apellido1R = re.compile(r'^[A-Za-z]+$')
    apellido2R = re.compile(r'^[A-Za-z]+$')
    extensionR = re.compile(r'^[0-9]+$')
    emailR = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')
    codigoOficinaR = re.compile(r'^[a-zA-Z0-9]+-[a-zA-Z0-9]+$')
    codigoJefeR = re.compile(r'^[0-9]+$')
    puestoR = re.compile(r'^[A-Za-z\s]+$')

#Obtener los datos del usuario: 
    codigo_empleado = int(validar_input(codigoEmpleadoR, "Ingrese el código del empleado: "))
    nombre = validar_input(nombreR, "Ingrese el nombre del empleado: ")
    apellido1 = validar_input(apellido1R, "Ingrese el primer apellido: ")
    apellido2 = validar_input(apellido2R, "Ingrese el segundo apellido: ")
    extension = validar_input(extensionR, "Ingrese la extensión: ")
    email = validar_input(emailR, "Ingrese el email: ")
    codigo_oficina = validar_input(codigoOficinaR, "Ingrese el nombre de la oficina: ")
    codigo_jefe = int(validar_input(codigoJefeR, "Ingrese el código del jefe: "))
    puesto = validar_input(puestoR, "Ingrese el puesto del empleado: ")


    empleado = {
        "codigo_empleado": int(input("Ingrese el código del empleado: ")),
        "codigo_empleado": codigo_empleado,
        "nombre": nombre,
        "apellido1": apellido1, 
        "apellido2": apellido2,
        "extension": extension,
        "email": email,
        "codigo_oficina": codigo_oficina,
        "codigo_jefe": codigo_jefe,
        "puesto": puesto
    }
    
    url = "http://154.38.171.54:5003/empleados"
    data = json.dumps(empleado)
    peticion = requests.post(url,data)
    print("\nEmpleado Guardado")



def deleteEmpleado(id):
    peticion = requests.delete(f"http://154.38.171.54:5003/empleados/{id}")
    if peticion.status_code == 200:
          print("\nEmpleado Eliminado")

def updateEmpleado(id):

#Expresiones regulares para cada dato: 
    codigoEmpleadoR = re.compile(r'^[0-9]+$')
    nombreR = re.compile(r'^[A-Za-z]+$')
    apellido1R = re.compile(r'^[A-Za-z]+$')
    apellido2R = re.compile(r'^[A-Za-z]+$')
    extensionR = re.compile(r'^[0-9]+$')
    emailR = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')
    codigoOficinaR = re.compile(r'^[a-zA-Z0-9]+-[a-zA-Z0-9]+$')
    codigoJefeR = re.compile(r'^[0-9]+$')
    puestoR = re.compile(r'^[A-Za-z\s]+$')

#Obtener los datos del usuario: 
    codigo_empleado = int(validar_input(codigoEmpleadoR, "Ingrese el código del empleado: "))
    nombre = validar_input(nombreR, "Ingrese el nombre del empleado: ")
    apellido1 = validar_input(apellido1R, "Ingrese el primer apellido: ")
    apellido2 = validar_input(apellido2R, "Ingrese el segundo apellido: ")
    extension = validar_input(extensionR, "Ingrese la extensión: ")
    email = validar_input(emailR, "Ingrese el email: ")
    codigo_oficina = validar_input(codigoOficinaR, "Ingrese el nombre de la oficina: ")
    codigo_jefe = int(validar_input(codigoJefeR, "Ingrese el código del jefe: "))
    puesto = validar_input(puestoR, "Ingrese el puesto del empleado: ")



    empleadoActualizado = {
        "codigo_empleado": codigo_empleado,
        "nombre": nombre,
        "apellido1": apellido1, 
        "apellido2": apellido2,
        "extension": extension,
        "email": email,
        "codigo_oficina": codigo_oficina,
        "codigo_jefe": codigo_jefe,
        "puesto": puesto
    }

    url = (f"http://154.38.171.54:5003/empleados/{id}")
    data = json.dumps(empleadoActualizado)
    peticion = requests.put(url,data)
    if peticion.status_code == 200:
            print("\nEmpleado Actualizado")

def menu():
    while True:
        print("""
        **************************************
            ADMINISTRAR DATOS DE EMPLEADOS:
        **************************************

        1. Guardar empleado nuevo
        2. Eliminar un empleado
        3. Actualizar un empleado
        0. Regresar
        
        
        """)
        
        try: 
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion >=0 and opcion<=3:
                if(opcion == 1):
                    print(tabulate(postEmpleado(), headers="keys", tablefmt="github"))
                elif(opcion == 2):
                    id = input("Ingrese el ID del empleado que desea eliminar: ")
                    print(tabulate(deleteEmpleado(id), headers="keys", tablefmt="github"))
                elif(opcion == 3):
                    id = input("Ingrese el ID del empleado que desea actualizar: ")
                    print(tabulate(updateEmpleado(id), headers="keys", tablefmt="github"))    
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
            