from tabulate import tabulate

import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleados as empleado
import modules.getPedido as pedido
import modules.getPago as pago

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

#print(tabulate(cliente.getAllPostal('24010'), tablefmt="grid"))



#-----------------------------------------------

#print (tabulate(oficina.getAllCodigoCiudad(), tablefmt="grid"))
#print (tabulate(oficina.getAllCiudadTelefono("Inglaterra"), tablefmt="grid"))
#print(tabulate(empleado.getAllNombreApellidoEmailJefe(3), tablefmt="grid"))



#PUNTO 4: Nombre, apellidos y email del jefe de la empresa 
#print(tabulate(empleado.getNombreApellidosEmailJefeEmpresa(), tablefmt = "grid"))

#PUNTO 5: Devolver listado de empleados que NO SON representantes de ventas
#print(tabulate(empleado.getAllNoRepresentante(), tablefmt="grid"))

#PUNTO 6: Listado con nombres de clientes 
#print(tabulate(cliente.getAllEspañoles(), tablefmt = "grid"))

#PUNTO 7: Listado con distintos estados de pedido
#print(tabulate(pedido.getEstadoPedido(), tablefmt = "grid"))

#PUNTO 8: Listado con código de clientes que realizaron pago en 2008. 
#         Elimine códigos que aparezcan repetidos
print(tabulate(pago.getAllPagoYear(), tablefmt= "grid"))
