from tabulate import tabulate
import requests
import json
import modules.getPago as pago
import modules.getEmpleados as empleado

def getAll():
    peticion = requests.get("http://154.38.171.54:5001/cliente")
    #data = json.dumps(peticion.json(), indent = 4)
    data = json.loads(peticion.text)
    return data
#Importar el archivo cliente que está en la carpeta storage
#as ayuda a ponerle un alias.

# PARA MOSTRAR CLIENTES:
#print(getAll())
#Se coloca el alias del archivo y el nombre del dato que se quiere imprimir


#FUNCIÓN 1: 
def getAllClientName():
    clienteName = []
    for val in getAll():
        clienteName.append({
            "Código": val.get('codigo_cliente'),
            "Nombre": val.get('nombre_cliente')
        })
    return clienteName

#FUNCIÓN 2
def getOneClientCodigo(codigo):
    clienteName = []
    for val in getAll():
        if val.get('codigo_cliente') == codigo:
            clienteName.append({
                "Código": val.get('codigo_cliente'),
                "Nombre": val.get('nombre_cliente')
            })
    return clienteName

#FUNCIÓN 3
def getAllClientCreditCiudad(limiteCredit, ciudad):
    clientCredit = list()
    for val in getAll():
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad')==ciudad):
            clientCredit.append({
                "Código": val.get("codigo_cliente"),
                "Responsable": val.get("nombre_cliente"),
                "Director": f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                "Teléfono": val.get("telefono"),
                "Fax": val.get("fax"),
                "Dirección": f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                "Origen": f"{val.get('ciudad')} {val.get('region')}",
                "Código del Asesor": val.get("codigo_empleado_rep_ventas"),
                "Crédito": val.get("limite_credito")
                })
    return clientCredit


#FUNCIÓN 4:
def getAllClientPaisRegionCiudad(pais, region, ciudad):
    clientZone = []
    for val in getAll():
        if(
            val.get('pais') == pais and 
            (val.get('region') == region or val.get('region') == None) and
            (val.get('ciudad') == ciudad or val.get('ciudad') == None)
        ):
            clientZone.append({
                "Código": val.get("codigo_cliente"),
                "Responsable": val.get("nombre_cliente"),
                "Director": f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                "Teléfono": val.get("telefono"),
                "Fax": val.get("fax"),
                "Dirección": f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                "Origen": f"{val.get('ciudad')} {val.get('region')} {val.get('pais')}",
                "Código Postal": val.get("codigo_postal"),
                "Código del Asesor": val.get("codigo_empleado_rep_ventas"),
                "Crédito": val.get("limite_credito")
            })
    return clientZone

#FUNCION 5: 
def getAllApellido(apellido):
    clientApellido = []
    for val in getAll():
        if val.get ('apellido_contacto') == apellido:
            clientApellido.append({
                "Código": val.get("codigo_cliente"),
                "Responsable": val.get("nombre_cliente"),
                "Director": f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                "Teléfono": val.get("telefono"),
                "Fax": val.get("fax"),
                "Dirección": f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                "Origen": f"{val.get('ciudad')} {val.get('region')} {val.get('pais')}",
                "Código Postal": val.get("codigo_postal"),
                "Código del Asesor": val.get("codigo_empleado_rep_ventas"),
                "Crédito": val.get("limite_credito")
            })
    return clientApellido

#FUNCIÓN 6: 
def getAllFax(fax):
    clientFax = []
    for val in getAll():
        if val.get('fax') == fax:
            clientFax.append({
                "Código": val.get("codigo_cliente"),
                "Responsable": val.get("nombre_cliente"),
                "Director": f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                "Teléfono": val.get("telefono"),
                "Fax": val.get("fax"),
                "Dirección": f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                "Origen": f"{val.get('ciudad')} {val.get('region')} {val.get('pais')}",
                "Código Postal": val.get("codigo_postal"),
                "Código del Asesor": val.get("codigo_empleado_rep_ventas"),
                "Crédito": val.get("limite_credito")
            })
    return clientFax


#FUNCIÓN 7: 
def getAllTelefono(telefono):
    clienteTelefono = []
    for val in getAll():
        if val.get('telefono') == telefono:
            clienteTelefono.append({
                "Código": val.get("codigo_cliente"),
                "Responsable": val.get("nombre_cliente"),
                "Director": f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                "Teléfono": val.get("telefono"),
                "Fax": val.get("fax"),
                "Dirección": f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                "Origen": f"{val.get('ciudad')} {val.get('region')} {val.get('pais')}",
                "Código Postal": val.get("codigo_postal"),
                "Código del Asesor": val.get("codigo_empleado_rep_ventas"),
                "Crédito": val.get("limite_credito")
            })
    return clienteTelefono


#FUNCIÓN 8:
def getAllDireccion(direccion):
    clientDireccion = []
    for val in getAll():
        if val.get('linea_direccion1') == direccion:
            clientDireccion.append({
                "Código": val.get("codigo_cliente"),
                "Responsable": val.get("nombre_cliente"),
                "Director": f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                "Teléfono": val.get("telefono"),
                "Fax": val.get("fax"),
                "Dirección": f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                "Origen": f"{val.get('ciudad')} {val.get('region')} {val.get('pais')}",
                "Código Postal": val.get("codigo_postal"),
                "Código del Asesor": val.get("codigo_empleado_rep_ventas"),
                "Crédito": val.get("limite_credito")
            })
    return clientDireccion


#FUNCIÓN 9:
def getAllPostal(postal):
    clientPostal = []
    for val in getAll():
        if val.get('codigo_postal') == postal:
            clientPostal.append({
                "Código": val.get("codigo_cliente"),
                "Responsable": val.get("nombre_cliente"),
                "Director": f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                "Teléfono": val.get("telefono"),
                "Fax": val.get("fax"),
                "Dirección": f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                "Origen": f"{val.get('ciudad')} {val.get('region')} {val.get('pais')}",
                "Código Postal": val.get("codigo_postal"),
                "Código del Asesor": val.get("codigo_empleado_rep_ventas"),
                "Crédito": val.get("limite_credito")
            })
    return clientPostal


#FUNCION 10:
def getAllEspañoles():
    nombresEspañoles = []
    for val in getAll():
        if val.get("pais") == "Spain":
            nombresEspañoles.append({
                "Nombre del Cliente": val.get("nombre_cliente"),
                "Pais": val.get("pais")
            })
    return nombresEspañoles



#FUNCIÓN 11:
def getAllMadrid():
    madridRepresentanteVentas = []
    for val in getAll():
         if val.get("ciudad") == "Madrid" and (val.get("codigo_empleado_rep_ventas") == 11 or val.get("codigo_empleado_rep_ventas") == 30):
               madridRepresentanteVentas.append({
                "Código": val.get("codigo_cliente"),
                "Responsable": val.get("nombre_cliente"),
                "Director": f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                "Teléfono": val.get("telefono"),
                "Fax": val.get("fax"),
                "Dirección": f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                "Origen": f"{val.get('ciudad')} {val.get('region')} {val.get('pais')}",
                "Código Postal": val.get("codigo_postal"),
                "Código del Asesor": val.get("codigo_empleado_rep_ventas"),
                "Crédito": val.get("limite_credito")
               })
    return madridRepresentanteVentas

#MULTITABLA:
#FUNCIÓN 12:
def getAllClientsRepresentante():
    representanteCodigo = []
    for cliente in getAll():
         for empleados in empleado.getAllEmpleado():
            if (cliente.get("codigo_empleado_rep_ventas") == empleados.get("codigo_empleado")):
                representanteCodigo.append({
                "Nombre del Cliente": cliente.get("nombre_cliente"),
                #"Código del Asesor": cliente.get("codigo_empleado_rep_ventas"),
                #"Codigo del empleado": empleados.get("codigo_empleado"),
                "Nombre del Representante de Ventas": f"{empleados.get('nombre')} {empleados.get('apellido1')}"
              })
              
    return representanteCodigo
         

#FUNCIÓN 13:
#Muestra el nombre de los clientes que hayan realizado pagos junto con el
#nombre de sus representantes de ventas. 

def getAllClientePagoRepresentante():
    clientePagoRepresentante = []
    clientePago = set()
    for payment in pago.getAllPago():
        clientePago.add(payment.get("codigo_cliente"))
    for val in clientePago:
        for cliente in getAll():
            for empleados in empleado.getAllEmpleado():
                if cliente.get("codigo_cliente") == val:
                    if (cliente.get("codigo_empleado_rep_ventas") == empleados.get("codigo_empleado")):
                        clientePagoRepresentante.append({
                           "Codigo del cliente que pagó": val,
                           "Nombre del Cliente": cliente.get("nombre_cliente"),
                           "Nombre del Representante de Ventas": f"{empleados.get('nombre')} {empleados.get('apellido1')}"
                        })           
    return clientePagoRepresentante
     

#FUNCIÓN 14: 
def getAllClientesSinPago():
    clientesSinPagoRepresentante = []
    clientePago = set()
    clientePago.add(payment.get("codigo_cliente")for payment in pago.getAllPago())
    for cliente in getAll():
        if cliente.get("codigo_cliente") not in clientePago:
            for empleados in empleado.getAllEmpleado():
                if (cliente.get("codigo_empleado_rep_ventas") == empleados.get("codigo_empleado")):
                        clientesSinPagoRepresentante.append({
                           "Nombre del Cliente que NO realizó pagos": cliente.get("nombre_cliente"),
                           "Nombre del Representante de Ventas": f"{empleados.get('nombre')} {empleados.get('apellido1')}"
                        })
                                   
    return clientesSinPagoRepresentante






    


def menu():
   while True: 
        print("""
    
                                                        ******************************************      
                                                                Reportes de los clientes
                                                        ******************************************
        0. Regresar al menú principal
        1. Obtener todos los clientes (codigo y nombre)
        2. Obtener un cliente por el código (código y nombre)
        3. Obtener toda la información de un cliente segun su limite crédito y ciudad que pertene (ejemplo: 3000.0, San Francisco)
        4. Obtener toda la información de un cliente segun su pais, region y ciudad (ejemplo: Spain, Madrid, Fuenlabrada)
        5. Obtener toda la información del cliente por el apellido del Director (ejemplo: GoldFish)
        6. Obtener toda la información del cliente por el número de Fax (por ejemplo: 5556901746)
        7. Obtener toda la información del cliente por el número de Telefono (por ejemplo: 5556901745)
        8. Obtener toda la información del cliente por su dirección principal (por ejemplo: Oaks Avenue nº22)
        9. Obtener toda la información del cliente por el código postal (por ejemplo: 28930)
        10.Obtener un listado de los nombres de todos los clientes españoles  
        11.Obtener un listado con clientes de Madrid y cuyo representante de ventas tenga el código 11 o 30.
        12.Obtener un listado con el nombre de cada cliente y el nombre y apellido de su representante de ventas
        13.Obtener un listado con el nombre de los clientes que hayan realizado pagos junto con el nombre de sus representantes de ventas
        14.Obtener un listado con el nombre de los clientes que NO hayan realizado pagos junto con el nombre de sus representantes de ventas
          


        """)

        try:
            opcion = int(input("\nSeleccione una de las opciones "))
            if opcion>=0 and opcion<15:
                if opcion == 1:
                        print(tabulate(getAllClientName(), headers = "keys", tablefmt= "rounded_grid"))
                elif opcion == 2:
                        codigoCliente = int(input("Ingrese el código del cliente "))
                        print(tabulate(getOneClientCodigo(codigoCliente), headers = "keys", tablefmt= "rounded_grid"))
                elif opcion == 3:
                        limite = float(input("Ingrese el limite de credito de los clientes que desea visualizar: "))
                        ciudad = input("Ingrese el nombre de la ciudad que desea filtrar: ")
                        print(tabulate(getAllClientCreditCiudad(limite, ciudad), headers = "keys", tablefmt= "rounded_grid"))
                elif opcion == 4:
                        pais = input("Ingrese el nombre del pais: ")
                        region = input("Ingrese el nombre de la región: ")
                        ciudad = input("Ingrese el nombre de la ciudad: ")
                        print(tabulate(getAllClientPaisRegionCiudad(pais, region, ciudad), headers = "keys", tablefmt = "rounded_grid"))
                elif opcion == 5:
                        apellido = input("Ingrese el apellido del Director: ")
                        print(tabulate(getAllApellido(apellido), headers = "keys", tablefmt= "rounded_grid"))
                elif opcion == 6:
                        fax = input("Ingrese el número del Fax: ")
                        print(tabulate(getAllFax(fax), headers = "keys", tablefmt= "rounded_grid"))
                elif opcion == 7:
                        telefono = input("Ingrese el número de Télefono ")
                        print(tabulate(getAllTelefono(telefono), headers = "keys", tablefmt= "rounded_grid"))
                elif opcion == 8:
                        direccion = input("Ingrese la dirección principal del cliente: ")
                        print(tabulate(getAllDireccion(direccion), headers = "keys", tablefmt= "rounded_grid"))
                elif opcion == 9:
                        postal = input("Ingrese el código postal del cliente: ")
                        print(tabulate(getAllPostal(postal), headers = "keys", tablefmt = "rounded_grid"))
                elif opcion == 10:
                        print(tabulate(getAllEspañoles(), headers = "keys", tablefmt = "rounded_grid"))
                elif opcion == 11:
                        print(tabulate(getAllMadrid(), headers = "keys", tablefmt = "rounded_grid"))
                elif opcion ==12:
                        print(tabulate(getAllClientsRepresentante(), headers = "keys", tablefmt = "rounded_grid"))
                elif opcion ==13:
                        print(tabulate(getAllClientePagoRepresentante(), headers = "keys", tablefmt = "rounded_grid"))
                elif opcion == 14:
                        print(tabulate(getAllClientesSinPago(), headers = "keys", tablefmt = "rounded_grid"))
                elif opcion == 0:
                        break
            else:
                print("\nOJO: No existe esa opción, por favor vuelva a intentarlo")


        except ValueError:
            print("""
                  -----------------------------------------------------------------------------
                  Solo se permiten los NÚMEROS ENTEROS correspondientes a la OPCIÓN ESCOGIDA
                                        Por favor, intentelo de nuevo.
                  -----------------------------------------------------------------------------""")
            

    
                

