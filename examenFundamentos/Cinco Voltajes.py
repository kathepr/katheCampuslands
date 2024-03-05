voltaje1=(int(input("\nIngrese el primer voltaje: ")))
voltaje2=(int(input("Ingrese el segundo voltaje: ")))
voltaje3=(int(input("Ingrese el tercer voltaje: ")))
voltaje4=(int(input("Ingrese el cuarto voltaje: ")))
voltaje5=(int(input("Ingrese el quinto voltaje: ")))

promedio = (voltaje1 + voltaje2 + voltaje3 + voltaje4 + voltaje5)//5

if promedio > 220:
    print("\nALTO VOLTAJE")

else:
    print("\nVOLTAJE CORRECTO")