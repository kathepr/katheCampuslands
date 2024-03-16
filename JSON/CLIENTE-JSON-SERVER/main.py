
import json
import requests

#CON ESTO ESTAMOS tratando de obtener recursos (datos, archivos, etc.) de esa dirección web
#obtener = requests.get("http://172.16.100.114:3000")
#print(obtener.json())


# #CON ESTO GUARDAMOS DATOS NUEVOS EN LA BASE DE DATOS:
empleadoNuevo = {
    "codigo": 888,
    "nombre": "Monica",
    "apellido": "Ruiz"
}
obtener = requests.post("http://172.16.100.114:5507", data=json.dumps(empleadoNuevo))
print(obtener)
#Se utiliza para convertir (serializar) un objeto de Python en una cadena JSON




#CON ESTO ELIMINAMOS DATOS:  AL FINAL COLOCAMOS UN SLASH Y EL NÚMERO ID DEL EMPLEADO QUE QUEREMOS QUITAR
# eliminar = requests.delete("http://172.16.100.114:5006/4")
# print(eliminar)


#DECODIFICANDO EN JSON
# plantilla = '[{"nombre": "Miguel"}, {"nombre": "Jhon"}, ["Hola mundo"]]'
# platilla = json.loads(plantilla)  # Decodificar 
# print(platilla[1].get("nombre"))
#Se utiliza para cargar (parsear) una cadena JSON y convertirla en un objeto de Python





# example = list([
#     dict({"nombre": "Miguel"}),
#     dict({"nombre": "Jhon"}),
#     list(["Hola mundo"])
# ])

# example = json.dumps(example, indent = 4)
# print(example)