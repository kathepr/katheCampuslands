import json
import requests
from tabulate import tabulate
import modules.getPedido as datosPedido
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




def postPedido():

#Expresiones regulares para cada dato:
    codigoPR = re.compile(r'^\d+$')
    fechaPedidoR= re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$')
    fechaEsperadaR= re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$')
    fechaEntregaR= re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$')
    estadoR= re.compile(r'^[a-zA-Z]+$')
    comentarioR= re.compile(r'^[^\n]+$')
    codigoClienteR= re.compile(r'^[0-9]+$')


#Obtener los datos del usuario:    
    codigo_pedido = int(validar_input(codigoPR, "Ingrese el código del pedido: ")),
    fecha_pedido = validar_input(fechaPedidoR, "Ingrese la fecha (año - mes - día): "),
    fecha_esperada = input(fechaEsperadaR, "Ingrese la fecha esperada (año-mes-día): "),
    fechaEntrega = input(fechaEntregaR, "Ingrese la fecha de entrega (año-mes-día): "),
    estado = validar_input(estadoR, "Ingrese estado del pedido: "),
    comentario = validar_input(comentarioR, "Ingrese comentarios: "),
    codigo_cliente = int(validar_input(codigoClienteR, "Ingrese el código del cliente: ")),
    

    pedido = {

        "codigo_pedido": codigo_pedido,
        "fecha_pedido": fecha_pedido,
        "fecha_esperada": fecha_esperada,
        "fechaEntrega": fechaEntrega,
        "estado": estado,
        "comentario": comentario,
        "codigo_cliente": codigo_cliente

        }
    
    url = "http://154.38.171.54:5007/pedidos"
    data = json.dumps(pedido)
    peticion = requests.post(url,data)
    print("\nPedido Guardado")




def deletePedido(id):
    peticion = requests.delete(f"http://154.38.171.54:5007/pedidos/{id}")
    if peticion.status_code == 200:
        print("\nPedido Eliminado")


def updatePedido(id):


#Expresiones regulares para cada dato:
    codigoPR = re.compile(r'^\d+$')
    fechaPedidoR= re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$')
    fechaEsperadaR= re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$')
    fechaEntregaR= re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}+$')
    estadoR= re.compile(r'^[a-zA-Z]+$')
    comentarioR= re.compile(r'^[^\n]+$')
    codigoClienteR= re.compile(r'^[0-9]+$')


#Obtener los datos del usuario:    
    codigo_pedido = int(validar_input(codigoPR, "Ingrese el código del pedido: ")),
    fecha_pedido = validar_input(fechaPedidoR, "Ingrese la fecha (año - mes - día): "),
    fecha_esperada = input(fechaEsperadaR, "Ingrese la fecha esperada (año-mes-día): "),
    fechaEntrega = input(fechaEntregaR, "Ingrese la fecha de entrega (año-mes-día): "),
    estado = validar_input(estadoR, "Ingrese estado del pedido: "),
    comentario = validar_input(comentarioR, "Ingrese comentarios: "),
    codigo_cliente = int(validar_input(codigoClienteR, "Ingrese el código del cliente: ")),
    

    pedidoActualizado = {

        "codigo_pedido": codigo_pedido,
        "fecha_pedido": fecha_pedido,
        "fecha_esperada": fecha_esperada,
        "fechaEntrega": fechaEntrega,
        "estado": estado,
        "comentario": comentario,
        "codigo_cliente": codigo_cliente
        }
    
    url = (f"http://154.38.171.54:5007/pedidos/{id}")
    data = json.dumps(pedidoActualizado)
    peticion = requests.put(url,data)
    if peticion.status_code == 200:
        print("\nPedido Actualizado")



def menu():
    while True:
        print("""
        ***********************************
            ADMINISTRAR DATOS DE PEDIDOS:
        ***********************************
              
        1. Guardar un pedido nuevo
        2. Eliminar un pedido
        3. Actualizar pedido
        0. Regresar
        
        
        """)
        
        try: 
            opcion = int(input("\nSelecione una de las opciones: "))
            if opcion >=0 and opcion<=3:
                if(opcion == 1):
                    print(tabulate(postPedido(), headers="keys", tablefmt="github"))
                elif(opcion == 2):
                    id = input("Ingrese el ID del pedido que desea eliminar: ")
                    print(tabulate(deletePedido(id), headers="keys", tablefmt="github"))
                elif opcion == 3:
                    id = input("Ingrese el ID del pedido que desea actualizar: ")
                    print(tabulate(updatePedido(id), headers="keys", tablefmt = "github"))    
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
            

    