
import json 
import requests

#CON ESTO ESTAMOS tratando de obtener recursos (datos, archivos, etc.) de esa dirección web
#obtener = requests.get("http://172.16.100.114:3000")
#print(obtener.json())




#CON ESTO GUARDAMOS DATOS NUEVOS EN LA BASE DE DATOS:
# empleadoNuevo = {
#     "codigo": 888,
#     "nombre": "Monica",
#     "apellido": "Ruiz"
# }
# obtener = requests.post("http://172.16.100.114:5006", data=json.dumps(empleadoNuevo))
# print(obtener)




#CON ESTO ELIMINAMOS DATOS:  AL FINAL COLOCAMOS UN SLASH Y EL NÚMERO ID DEL EMPLEADO QUE QUEREMOS QUITAR
eliminar = requests.delete("http://172.16.100.114:5006/4")
print(eliminar)