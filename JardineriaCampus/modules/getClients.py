from tabulate import tabulate
import storage.cliente as cli #cli = abreviación de cliente 



#Importar el archivo cliente que está en la carpeta storage
#as ayuda a ponerle un alias.

# PARA MOSTRAR CLIENTES:
#print(cli.clientes)
#Se coloca el alias del archivo y el nombre del dato que se quiere imprimir

def getAllClientName():
    clienteName = []
    for val in cli.clientes:
        codigoName = dict({
            "codigo": val.get('codigo_cliente'),
            "nombre": val.get('nombre_cliente')
        })
        clienteName.append(codigoName)
    return clienteName

def getOneClientCodigo(codigo):
    clienteName = []
    for val in cli.clientes:
        if(val.get('codigo_cliente')== codigo):
            return [{
                "codigo": val.get('codigo_cliente'),
                "nombre": val.get('nombre_cliente')
            }]

def getAllClientCreditCiudad(limiteCredit, ciudad):
    clientCredit = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad')==ciudad):
            clientCredit.append({
                "Codigo": val.get("codigo_cliente"),
                "Responsable": val.get("nombre_cliente"),
                "Director": f"{val.get('nombre_contacto')} {val.get('apellido_contacto')}",
                "Telefono": val.get("telefono"),
                "Fax": val.get("fax"),
                "Dirección": f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                "Origen": f"{val.get('ciudad')} {val.get('region')}",
                "Código del asesor": val.get("codigo_empleado_rep_ventas"),
                "Crédito": val.get("limite_credito")
                })
    return clientCredit



#ARREGLAR ESTA PARTE DEL CÓDIGO - OJO: 
def getAllClientPaisRegionCiudad(pais, region=None, ciudad=None):
    clientZone = []
    for val in cli.clientes:
        if(
            val.get('pais') == pais or
            (val.get('region') == region or val.get('region') == None) and
            (val.get('ciudad') == ciudad or val.get('ciudad') == None)
        ):
            clientZone.append(val)
    return clientZone

def getAllApellido(apellido):
    clientApellido = []
    for val in cli.clientes:
        if val.get ('apellido_contacto') == apellido:
            clientApellido.append(val)
    return clientApellido


def getAllFax(fax):
    clientFax = []
    for val in cli.clientes:
        if val.get('fax') == fax:
            clientFax.append(val)
    return clientFax


def getAllTelefono(telefono):
    clienteTelefono = []
    for val in cli.clientes:
        if val.get('telefono') == telefono:
            clienteTelefono.append(val)
    return clienteTelefono


def getAllDireccion(direccion):
    clientDireccion = []
    for val in cli.clientes:
        if val.get('linea_direccion1') == direccion:
            clientDireccion.append(val)
    return clientDireccion


def getAllPostal(postal):
    clientPostal = []
    for val in cli.clientes:
        if val.get('codigo_postal') == postal:
            clientPostal.append(val)
    return clientPostal



def getAllEspañoles():
    nombresEspañoles = []
    for val in cli.clientes:
        if val.get("pais") == "Spain":
            nombresEspañoles.append({
                "nombre": val.get("nombre_cliente"),
                "pais": val.get("pais")
            })
    return nombresEspañoles






def menu():
    print("""
    Reportes de los clientes:
        1. Obtener todos los clientes (codigo y nombre)
        2. Obtener un cliente por el código (código y nombre)
        3. Obtener toda la información de un cliente segun su limite crédito y ciudad que pertene (ejemplo: 3000.0, San Francisco)

    """)
    opcion = int(input("\nSeleccione una de las opciones "))
    if opcion == 1:
        print(tabulate(getAllClientName(), headers = "keys", tablefmt= "rounded_grid"))
    elif opcion == 2:
        codigoCliente = input("Ingrese el código del cliente ")
        print(tabulate(getOneClientCodigo(codigoCliente), headers = "keys", tablefmt= "rounded_grid"))
    elif opcion == 3:
        limite = float(input("Ingrese el limite de credito de los clientes que desea visualizar: "))
        ciudad = input("Ingrese el nombre de la ciudad que desea filtrar: ")
        print(tabulate(getAllClientCreditCiudad(limite, ciudad), headers = "keys", tablefmt= "rounded_grid"))