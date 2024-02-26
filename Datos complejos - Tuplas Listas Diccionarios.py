information = tuple(("Miguel", 23 , "Calle", 1.63))
casa = tuple (("departamento", "finca"))
print (information)

# La tupla se llama information. Y contine Miguel que está en posición 0, 
# 23 en posición 1, calle en posición 2, 1.63 en posición 3

#Si quiero acceder a mi edad, lo puedo hacer con el indice 1. 
# Esto puede ser como una matriz unidimensional - una tabla en la que se guardan datos
#Las tuplas se usan para datos constantes, cosas que nunca cambian. 

print (f"""El usuario {information[0]} tiene una {casa [1]} en estados unidos""") #La f del comienzo, convierte todo a string.

print (information [1])
print (information[1:3]) 
print (information[1:-2]) 
#También se puede acceder a una porción de la tupla, indicando (opcionalmente) desde el índice de inicio hasta el índice de fin: 