import json
import requests

def getAllGama():
    #json-server storage/gama_producto.json -b 5502
    peticion = requests.get(http://172.16.100.114:5502)
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append({
            
        })