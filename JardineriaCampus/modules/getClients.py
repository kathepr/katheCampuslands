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
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente')
        })
        clienteName.append(codigoName)
    return clienteName

def getOneClientCodigo(codigo):
    clienteName = []
    for val in cli.clientes:
        if(val.get('codigo_cliente')== codigo):
            return {
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente')
            }

def getAllClientCreditCiudad(limiteCredit, ciudad):
    clientCredit = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad')==ciudad):
            clientCredit.append(val)
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