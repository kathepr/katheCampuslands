from tabulate import tabulate

import modules.getClients as cliente

#El primer archivo, está importando el segundo y el segundo al tercero
#De esta forma, tenemos acceso al contenido de los tres archivos. 

#print(cliente.getAllClientName())
#print(cliente.getOneClientCodigo(20))
#print(cliente.getAllClientCreditCiudad(5000, "Humanes"))
#print(cliente.getAllClientPaisRegionCiudad("France", None, "Paris"))

#print(tabulate(cliente.getAllClientPaisRegionCiudad("Australia"),tablefmt="grid"))

#print(tabulate(cliente.getAllApellido("GoldFish"),tablefmt="grid"))

#print (tabulate(cliente.getAllFax('5557410346'), tablefmt="grid"))

#print (tabulate(cliente.getAllTelefono('5552323129'),tablefmt="grid"))

#print (tabulate(cliente.getAllDireccion('Wall-e Avenue'), tablefmt="grid"))

print(tabulate(cliente.getAllPostal('24010'), tablefmt="grid"))