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
#print(tabulate(pago.getAllPagoYear(), tablefmt= "grid"))


#PUNTO 9: Listado con codigo de pedido, codigo cliente, fecha esperada,
# fecha de entrega de los pedidos que no han sido entregados a tiempo.
#print(tabulate(pedido.getAllPedidosEntregadosAtrasadosDeTiempo(), tablefmt= "grid"))


#PUNTO 10: Listado con el código de pedido, código cliente, fecha esperada
#          fecha de entrega de pedidos cuya fecha de entrega ha sido al menos dos
#          días antes de la fecha esperada.
#print(tabulate(pedido.getAllPedidoEntregadoDosDiasAntes(), tablefmt = "grid"))


#PUNTO 11: Devuelve listado con pedidos rechazados en 2009
#print(tabulate(pedido.getAllPedidosRechazados(), tablefmt = "rounded_grid"))


#PUNTO 12: Devuelve un listado de pedidos ENTREGADOS en el mes de Enero.
#print(tabulate(pedido.getAllPedidosEnero(), tablefmt = "rounded_grid")) 






#FALTA: 
#PUNTO 13: Listado con todos los pagos que se realizaron en 2008
#          mediante Paypal. ORDENE RESULTADO DE MAYOR A MENOR. 


#PUNTO 14: Listado con TODAS las formas de pago. 
#          NO DEBEN APARECER FORMAS DE PAGO REPETIDAS. 


#PUNTO 15: Listado de productos de GAMA ORNAMENTALS y que tienen más
#          de 100 unidades en stock. 
#          DEBE ORDENAR EL LISTADO: precio de venta, mostrar en primer lugar
#          de mayor precio. 