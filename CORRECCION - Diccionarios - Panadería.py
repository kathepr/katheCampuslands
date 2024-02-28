#Crear diccionario de pan dulce con sus respectivos valores

Salado={"Baguete":4000,
          "Croissant":2500,
          "Pan Integral":6000,
          "Pan de Yuca":1500,
          "Pan de Bono":1200,
          "Almojabana":1000,
          "Pastel de Pollo":5000,
          "Pan de ajo":2500,
          "Palito de queso":800,
          "Empanada":2000
          }

Postres={"Torta de Chocolate":25000,
         "Cheesecake de fresa": 30000,
         "Tarta de limón":20000,
         "Tiramisú":18000,
         "Trufas":2000,
         "Brownies":5000,
         "Rollo de Canela":4000,
         "Merengues":2500,
         "Crepe de nutella":15000,
         "Alfajor": 5000
         }

Bebidas={"Tinto":2000,
         "Aguapanela":2000,
         "Milo":2500,
         "Jugo de naranja": 8000,
         "Limonada": 6000,
         "Cerveza Aguila":8000,
         "Agua sin gas": 3000,
         "Chocolate caliente": 3500,
         "Té caliente":3500,
         "Té helado":3500
         }

items_Salado =(f"{Salado.keys()} {Salado.values()}")
keys_Salado = list(Salado.keys())
valor_Salado= list(Salado.values())


items_Postres =(f"{Postres.keys()} {Postres.values()}")
list_Postres = list(Postres.keys())
valor_Postres= list(Postres.values())

items_Bebidas =(f"{Bebidas.keys()}{Bebidas.values()}")
list_Bebidas = list(Bebidas.keys())
valor_Bebidas= list(Bebidas.values())



print("\n******************************************************")
print("\tBienvenido a la Panadería de Kathe")
print("******************************************************\n")

print("\tCATEGORÍA DE PRODUCTOS\n")
print("1. Panadería Salada")
print("\033[2m2. Postres (CATEGORIA EN CONSTRUCCIÓN)\033[0m")
print("\033[2m3. Bebidas (CATEGORÍA EN CONSTRUCCIÓN)\033[0m")

print("\n")
opcion=int(input("Ingrese la categoría que desea consultar: "))


#CONDICIONAL PARA OPCION 1 - PANADERIA SALADA
if opcion==1:
    print("\n*********************************")
    print ("\n\tPANADERIA SALADA\n")
    print("*********************************\n")
    for i,_ in enumerate (keys_Salado):  #Se colocó guión bajo porque no vamos a utilizar ese valor de la lista. 
        
        print(f"{i}.{keys_Salado[i]} = ${valor_Salado[i]}")

    opcion = int(input("\n¿Qué opción desea? "))
    print (f"\nUsted ha seleccionado '{keys_Salado[opcion]}', este producto tiene un valor de ${valor_Salado[opcion]}")

    #CREACIÓN DE PROMOCIONES PARA PANADERIA SALADA: 
    if opcion ==3:
        print("\n\t        **********************************************")
        print (f"                PROMO   ¡Hoy te llevas el doble de {keys_Salado[opcion]}!      ")
        print("\t       **************************************************")
    elif opcion ==8:  
        print("\n\t       **********************************************************")
        print (f"              PROMO   ¡Hoy te llevas {keys_Salado[opcion]} + un jugo de naranja!      ") 
        print("\t     ****************************************************************") 
    
    #PREGUNTAR POR NÚMERO DE UNIDADES A COMPRAR
    unidad=int(input(f"\n¿Cuantas unidades de {keys_Salado[opcion]} desea comprar? "))

    #PREGUNTAR CON CUANTO DINERO PAGA EL CLIENTE:  
    dinero = int(input("Ingrese la cantidad de dinero disponible: ")) 
    PagoTotal = valor_Salado[opcion] * unidad
    vueltos = dinero - PagoTotal

    if dinero>=PagoTotal:
        
        if opcion == 3:
            unidad_promo= unidad*2
            print (f"\nGracias a la promo usted se lleva {unidad_promo} unidades de {keys_Salado[opcion]} por {PagoTotal}, sus vueltos son {vueltos}")

        elif opcion ==8:
            print (f"\nGracias a la promo usted se lleva {unidad} unidades de {keys_Salado[opcion]} + un jugo de naranja por ${PagoTotal}, sus vueltos son ${vueltos}")

        else:    
            print(f"\nUsted compró {unidad} unidades de {keys_Salado[opcion]}, las cuales costaron {PagoTotal} y sus vueltos son: ${vueltos}")


    else:
        print(f"\nUsted desea {unidad} unidades de {keys_Salado[opcion]}, las cuales cuestan ${PagoTotal}, le falta un total de ${-vueltos} ")  

#DESPEDIDA:
print ("Gracias por su compra. ¡Lindo día!")  
    
    