import json

def postProducto(producto):
    import requests
    peticion = requests.post("http://172.16.100.114:5009", data = json.dumps(producto))
    res = peticion.json()
    return res
