voltaje1=(int(input("\nIngrese el primer voltaje: ")))
voltaje2=(int(input("Ingrese el primer voltaje: ")))
voltaje3=(int(input("Ingrese el primer voltaje: ")))

promedio = (voltaje1 + voltaje2 + voltaje3)//3

if promedio > 220:
    print("\nPELIGRO")

elif promedio < 220 and promedio > 115:
    print("\nALTO VOLTAJE")

else:
    print("\nVOLTAJE CORRECTO")