import json
import requests
    #json-server storage/producto.json -b 5009: en el computador del campus
    #En mi computador se saca la terminal sin colocar -b
    #json-server storage/producto.json 5009
    #El puerto en mi computador es: http://127.0.0.1:5502

def getAllGama():
    peticion = requests.get("http://127.0.0.1:5502")#Este es el puerto de mi computador
    #peticion = requests.get("http://172.16.102.108:5502")#Campuslands
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre