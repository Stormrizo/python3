mitupla=("Juan", 3,"tertulia")

print(mitupla[2]) #Acceder al elemento 2 de la tupla

milista=list(mitupla) #convertir tupla a lista con el comando list(). De lista a tupla es con tuple()

print(mitupla)

print(milista)

print("Sebas" in mitupla) #¿Está "Sebas" en mitupla? - booleano

print(mitupla.count("a")) #Método para saber cantidad de un elemento con el comando count()

print(len(mitupla)) #Longitud de la tupla o lista con el comando len()

tupla_unitaria=("Pedro",) #Tupla unitaria , es una tupla con un único elemento y la sintáxis va acompañada de una coma

print(len(tupla_unitaria))

#Las tuplas también se pueden escribir sin parentésis: (opcionales)

mytuple="Sebas", 3, 45, 76 #Empaquetado de tupla

print(mytuple)


#Desempaquetado de tupla:

nombre, dia, mes, año = mytuple

print(nombre)
print(dia)
print(mes)
print(año)
