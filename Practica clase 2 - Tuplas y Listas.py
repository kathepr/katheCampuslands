

productos = tuple(("Colca Cola", "Pepsi Cola"))
productos = list(productos)
productos.append("Colombiana")   #.append = método de agregación
print (productos)
print ("Se agregó Colombiana usando .append")
print (" ")

productos .insert(1,"Postobon")  #.insert = especifico la posición en la que deseo agregarlo.
productos = tuple(productos)
print (productos)
print ("Pepsi apararece: ", productos.count("Pepsi Cola"), " vez")#.count = Contar la cantidad de apariciones de un elemento

print (" ")     # 0    1    2    3    4    5    6    7
letras = tuple (("a", "e", "i", "o", "g", "l", "i", "u")) #.index = Encuentra la primera coincidencia y apartir de ahí cuenta para encontrar la segunda coincidencia.
posicion = letras.index("i")                              # El valor final, tiene en cuenta todos los datos y va a ofrecer la posición de la última coincidencia. 
print ("La posición de 'i' es: ", posicion)