from tabulate import tabulate
import requests
import os
import json
import modules.getClients as gCliente
import modules.postCliente as pCliente
import modules.getOficina as gOficina
import modules.postOficina as pOficina
import modules.getEmpleados as gEmpleado
import modules.postEmpleados as pEmpleado
import modules.getPago as gPago
import modules.postPago as pPago
import modules.getProducto as Repproducto
import modules.postProducto as CRUDproducto
import modules.getPedido as gPedido
import modules.postPedido as pPedido


def menuProducto():
    while True: 
        print("""
          
        *******************************
                 Menu de Productos
        *******************************
          
            1. Reportes de los productos
            2. Guardar, Actualizar y Eliminar productos
            0. Regresar al menú principal. 
          
          """)
        try:
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion >= 0 and opcion <3:
                if(opcion == 1):
                    Repproducto.menu()
                elif(opcion == 2):
                    CRUDproducto.menu()
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





def menuPedido():
    while True:
        print("""
          
        *******************************
                 Menu de Pedidos
        *******************************
          
            1. Reportes de los pedidos
            2. Guardar, Actualizar y Eliminar pedidos
            0. Regresar al menú principal. 
          
          """)
        try: 
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion >= 0 and opcion < 3:
                if(opcion == 1):
                    gPedido.menu()
                elif(opcion == 2):
                    pPedido.menu()
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





def menuPago():
    while True:
        print("""
          
        *******************************
                 Menu de Pagos
        *******************************
          
            1. Reportes de los pagos
            2. Guardar, Actualizar y Eliminar pagos
            0. Regresar al menú principal. 
          
          """)
        try:
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion >=0 and opcion <3:
                if(opcion == 1):
                    gPago.menu()
                elif(opcion == 2):
                    pPago.menu()
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





def menuOficina():
    while True:
        print("""
          
        *******************************
                 Menu de Oficina
        *******************************
          
            1. Reportes de las oficinas
            2. Guardar, Actualizar y Eliminar oficinas
            0. Regresar al menú principal. 
          
          """)
        
        try: 
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion >=0 and opcion < 3:
                if(opcion == 1):
                    gOficina.menu()
                elif(opcion == 2):
                    pOficina.menu()
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




def menuCliente():
    while True:
        print("""
          
        *******************************
                 Menu de Clientes
        *******************************
          
            1. Reportes de clientes
            2. Guardar, Actualizar y Eliminar clientes
            0. Regresar al menú principal. 
          
          """)
        
        try:
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion >= 0 and opcion < 3:
                if(opcion == 1):
                    gCliente.menu()
                elif(opcion == 2):
                    pCliente.menu()
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
        




def menuEmpleado():
    while True:
        print("""
          
        *******************************
                 Menu de Empleados
        *******************************
          
            1. Reportes de empleados
            2. Guardar, Actualizar y Eliminar empleados
            0. Regresar al menú principal.
          
          """)
        
        try: 
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion >=0 and opcion <3:
                if(opcion == 1):
                    gEmpleado.menu()
                elif(opcion == 2):
                    pEmpleado.menu()
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
        




if __name__ == "__main__":


    while True: 
        print("""
          
        *******************************
                 Menu Principal
        *******************************
          
            1. Clientes
            2. Oficinas
            3. Empleados
            4. Pedidos
            5. Pagos
            6. Productos
            0. Salir
          
          """)
        
        try: 
            opcion = int(input("\nSeleccione una de las opciones: "))
        
            if opcion>=0 and opcion<7:
                if opcion == 1:
                    menuCliente()
                elif opcion == 2:
                    menuOficina()
                elif opcion == 3:
                    menuEmpleado()
                elif opcion == 4:
                    menuPedido()
                elif opcion == 5:
                    menuPago()
                elif opcion == 6:
                    menuProducto()
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
            

    


#Filtrar los pedidos entregados 

    # peticion = requests.get("http://154.38.171.54:5007/pedidos?estado=Entregado&fechaEntrega_ne.null") #Colocar un ? significa que se va agregar un cambio / url del profesor
    # data = json.dumps(peticion.json(), indent = 4)





    # peticion = requests.get("http://154.38.171.54:5008/productos") #Colocar un ? significa que se va agregar un cambio / url del profesor
    # data = json.dumps(peticion.json(), indent = 4)







    # with open("storage/producto.json", "r") as f:
    #     fichero = f.read()
    #     data = json.loads(fichero)
    # for i, val in enumerate(data):
    #     data[i]["id"] = (i+1)
    # data = json.dumps(data, indent=4).encode("utf-8")
    # with open("storage/producto.json", "wb+") as f1:
    #     f1.write(data)
    #     f1.close()
        


#def menu():
#    contador = 1
#    print("Menu Principal")
#    for nombre, objeto in sys.modules.items():
#        if nombre.startswith("modules"):
#            modulo = getattr(objeto, "name", None)
#            if(modulo != "modules"):
#                print(f"""{contador}. {modulo.split("get")[-1]} """)
#                contador += 1


#menu()

#El primer archivo, está importando el segundo y el segundo al tercero
#De esta forma, tenemos acceso al contenido de los tres archivos. 

#print(cliente.getAllClientName())
#print(cliente.getOneClientCodigo(20))
#print(cliente.getAllClientCreditCiudad(5000, "Humanes"))
#print(cliente.getAllClientPaisRegionCiudad("France", None, "Paris"))

#print(tabulate(cliente.getAllClientPaisRegionCiudad("Australia"),tablefmt="rounded_grid"))

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



#PUNTO 13: Listado con todos los pagos que se realizaron en 2008
#          mediante Paypal. ORDENE RESULTADO DE MAYOR A MENOR. 
#print(tabulate(pago.getAllPago2008(), tablefmt = "rounded_grid"))



#PUNTO 14: Listado con TODAS las formas de pago. 
#          NO DEBEN APARECER FORMAS DE PAGO REPETIDAS. 
#print(tabulate(pago.getAllFormasPago(), tablefmt = "rounded_grid"))







#                           OJO: PUNTO 15 NO SE PUEDE HACER - MODULO DE producto.py ESTÁ INCOMPLETO Y VACÍO.
        

#PUNTO 15: Listado de productos de GAMA ORNAMENTALS y que tienen más
#          de 100 unidades en stock. 
#          DEBE ORDENAR EL LISTADO: precio de venta, mostrar en primer lugar
#          de mayor precio. 