import json
import requests
    #json-server storage/producto.json -b 5502

peticion = requests.get(f"http://154.38.171.54:5008/productos?gama={gama}&cantidadEnStock_gte={stock} &_sort=-precio_venta") #Colocar un ? significa que se va agregar un cambio                                                                                                     # & para añadir otra condicion. 
data = json.dumps(peticion.json(), indent = 4)                                                                               #URL del profesor


def getAllGama():
    #peticion = requests.get("http://[::1]:5502")#Este es el puerto de mi computador
    peticion = requests.get("http://172.16.102.108:5502")#Campuslands
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre