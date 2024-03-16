import json
import requests
    #json-server storage/producto.json -b 5502

def getAllGama():
    peticion = requests.get("http://192.168.68.114:5502")#Este es el puerto de mi computador
    #peticion = requests.get("http://172.16.102.108:5502")#Campuslands
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre