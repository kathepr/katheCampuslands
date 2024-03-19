import json
import requests
    #json-server storage/producto.json -b 5502


# OJO REVISAR GET  GAMAS. 

def getAllGama():
    peticion = requests.get(f"http://154.38.171.54:5008/productos?gama=Ornamentales&cantidadEnStock_gte=100&_sort=-precio_venta") #Colocar un ? significa que se va agregar un cambio                                                                                                     # & para añadir otra condicion. 
    data = json.loads(peticion.text)
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre





#peticion = requests.get(f"http://154.38.171.54:5008/productos?gama={gama}&cantidadEnStock_gte={stock} &_sort=-precio_venta") #Colocar un ? significa que se va agregar un cambio                                                                                                     # & para añadir otra condicion. 
#data = json.dumps(peticion.json(), indent = 4)                                                                               #URL del profesor