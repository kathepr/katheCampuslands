#Crear diccionario de pan dulce con sus respectivos valores
menu = { 
    "Salado":{
            "Baguete": 4000,
            "Croissant":2500,
            "Pan Integral":6000,
            "Pan de Yuca":1500,
            "Pan de Bono":1200,
            "Almojabana":1000,
            "Pastel de Pollo":5000,
            "Pan de ajo":2500,
            "Palito de queso":800,
            "Empanada":2000
            },

    "Postres":{
            "Torta de Chocolate":25000,
            "Cheesecake de fresa": 30000,
            "Tarta de limón":20000,
            "Tiramisú":18000,
            "Trufas":2000,
            "Brownies":5000,
            "Rollo de Canela":4000,
            "Merengues":2500,
            "Crepe de nutella":15000,
            "Alfajor": 5000
         },  
    "Bebidas":{"Tinto":2000,
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
}


print("\n******************************************************")
print("\tBienvenido a la Panadería de Kathe")
print("******************************************************\n")

print("\tCATEGORÍA DE PRODUCTOS\n")
print("1. Panadería Salada")
print("2. Postres")
print("3. Bebidas")

print("\n")
categoria = (int(input("Ingrese la categoría que desea consultar ")))

keys_menu = list(menu.keys())   # Se trajo las keys del menú (salado, postres)

productos = menu[keys_menu[categoria - 1]]
keys_productos=list(productos.keys())

for i, producto in enumerate(keys_productos):
    print(f"{i+1}.{producto} = ${productos[producto]}")

opcion = int(input("¿Que producto desea? "))
precio = productos[keys_productos[opcion-1]]

cantidad = int(input("¿Cuantas unidades quiere? "))

dinero = int(input("¿Con cuanto dinero paga? "))

pago_total = cantidad * precio
vueltos = dinero - pago_total

if dinero>=pago_total:
        
    print(f"\nUsted compró {cantidad} unidades de {keys_productos[opcion-1]}, las cuales costaron {pago_total} y sus vueltos son: ${vueltos}")

else:
    print(f"\nUsted desea {cantidad} unidades de {keys_productos[opcion-1]}, las cuales cuestan ${pago_total}, le falta un total de ${-vueltos} ")  


print ("Gracias por su compra. ¡Lindo día! ")  