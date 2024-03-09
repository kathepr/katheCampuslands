from tabulate import tabulate

import storage.oficina as of

#Devuelve un listado con codigo de oficina y la ciudad donde hay oficinas


#FUNCION 1:
def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina: #El of, corresponde al alias del modulo storage oficina
        codigoCiudad.append({
            "Código de la Oficina": val.get("codigo_oficina"),
            "Ciudad": val.get ("ciudad")
        })
    return codigoCiudad




#FUNCION 2:
def getAllCiudadTelefono (pais):
    ciudadTelefono = []
    for val in of.oficina:
        if(val.get("pais")== pais):
            ciudadTelefono.append({
            "Ciudad": val.get("ciudad"),
            "Telefono": val.get("telefono"),
            "Oficinas": val.get("codigo_oficina"),
            "Pais": val.get("pais")
        })
    return ciudadTelefono



def menu():
    print("""

                            ****************************************
                                    Reportes de las Oficinas
                            ****************************************
   
           1. Obtener información del código y la ciudad donde se encuentran todas las oficinas
           2. Obtener información de la ciudad y telefono de las oficinas por pais (ejemplo: España)




    """)

    opcion = int(input("\nSeleccione una de las opciones "))
    if opcion == 1:
        print(tabulate(getAllCodigoCiudad(), headers = "keys", tablefmt = "rounded_grid"))
    elif opcion ==2:
        pais = input("Ingrese el pais correspondiente al listado de oficinas que desea consultar: ")
        print(tabulate(getAllCiudadTelefono(pais), headers = "keys", tablefmt = "rounded_grid"))
    else:
        print("\nEsa opción NO existe")