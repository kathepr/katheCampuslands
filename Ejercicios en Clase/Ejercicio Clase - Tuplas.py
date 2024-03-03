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
universidad_post = input ("Ingrese la universidad en la que realizó sus estudios de postgrado: ")
educacion = tuple ((colegio, pregrado, universidad_pre, postgrado, universidad_post))

print (f"""Asistió al colegio {educacion[0]}. Estudió {educacion[1]} en la universidad {educacion[2]}.
       Tiene los siguientes estudios de post-grado {educacion[3]} y los cursó en la institución: {educacion[4]}""")


trabajo= input ("Ingrese el nombre de la empresa de su último empleo: ")
cargo = input ("Ingrese el cargo que tenía en la empresa: ")
laboral = tuple((trabajo, cargo))

print (f"""Su último trabajo fue en {laboral[0]}, en el que ocuó el cargo de {laboral[1]}.""")

