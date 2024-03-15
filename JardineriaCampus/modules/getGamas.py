#import json
import requests


def getAllGama():
    #json-server storage/gama_producto.json -b 5502: En el computador del campus
    #En mi computador se saca la terminal sin colocar -b
    #json-server storage/producto.json 5502
    #El puerto en mi computador es: http://127.0.0.1:5502

    peticion = requests.get("http://172.16.102.108:5502")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre