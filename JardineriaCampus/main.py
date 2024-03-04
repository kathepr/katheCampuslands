from tabulate import tabulate

import modules.getClients as cliente

#El primer archivo, está importando el segundo y el segundo al tercero
#De esta forma, tenemos acceso al contenido de los tres archivos. 

#print(cliente.getAllClientName())
#print(cliente.getOneClientCodigo(20))
#print(cliente.getAllClientCreditCiudad(5000, "Humanes"))
#print(cliente.getAllClientPaisRegionCiudad("France", None, "Paris"))

print(tabulate(cliente.getAllClientPaisRegionCiudad("Australia"),tablefmt="grid"))