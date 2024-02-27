productos = tuple((
    "Coca-Cola", # posicion 0
    "Pepsi",     # posicion 1
    "Sprite",    # posicion 2
    "Fanta", 
    "7UP", 
    "Mountain Dew", 
    "Dr Pepper", 
    "Schweppes", 
    "Mirinda", 
    "Lift"))

precios = tuple((
    4500,        # posicion 0
    3750,        # posicion 1    
    3000,        # posicion 2
    3600, 
    5250, 
    6000, 
    5400, 
    3900, 
    4200, 
    4800))

print ("******************************")
print ("Menú de selección de productos")
print ("******************************\n")

#    for i in productos: #Recorra esta lista 1 a 1. 
#    print(i)            #Muestre 1 a 1 los productos de la lista.


for i,val in enumerate(productos): #recorrer la tupla y sacarle su valor y la posicion donde está ese valor#

    print (f"""{i}. {val} ${precios[i]}""")

#    print (i, val, precios[i])

print ("\n")
opcion = int(input("¿Que opción desea? "))
print (f"""Usuario, usted selecciono el producto {productos[opcion]} con un valor de $ {precios[opcion]}""") 
print ("\n")

dinero=int(input("Ingrese la cantidad de dinero disponible: "))
if dinero>=precios[opcion]:
    vueltos = dinero - precios[opcion]
    print(f"Usuario, usted compró el {productos[opcion]} con un valor de $ {precios[opcion]}, sus vueltos son ${vueltos}")
else:
    vueltos = dinero - precios[opcion]
    print(f"Usuario el producto que desea comprar {productos[opcion]} con un valor de ${precios[opcion]}, le falta un total de ${-vueltos} ")



