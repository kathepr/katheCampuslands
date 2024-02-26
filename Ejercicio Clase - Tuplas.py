nombre= input ("Escriba su nombre: ")
edad = input ("Escriba su edad: ")
altura = input ("Ingrese su estatura: ")
information = tuple((nombre, edad, altura))

print (f"""El usuario {information[0]} tiene {information[1]} años y mide {information[2]} cms """)

calle = input ("Ingrese su dirección: ")
barrio = input ("Ingrese su barrio: ")
ciudad = input ("Ingrese la ciudad: ")
direccion = tuple ((calle, barrio, ciudad))

print (f"""Vive en {direccion[0]}, en el barrio {direccion[1]}, en la ciudad {direccion[2]}""")


colegio = input ("Ingrese el nombre del colegio al que perteneció: ")
pregrado = input ("Ingrese sus estudios de pregrado: ")
universidad_pre = input ("Ingrese la universidad en la que realizó sus estudios de pregrado: ")
postgrado = input ("Ingrese sus estudios de postgrado: ")
universidad_post = input ("Ingrese la universidad en la que realizó sus estudios de postgrado:")
educacion = tuple (colegio, pregrado, universidad_pre, postgrado, universidad_post)

print (f"""Asistió al colegio {colegio[0]}""")


trabajo= input ("Ingrese el lugar de trabajo de su último empleo: ")
fecha = input ("Ingrese la fecha en la que ingresó al último empleo: ")
laboral = tuple((trabajo,fecha))



