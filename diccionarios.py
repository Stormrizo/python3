#Clave:valor - key:value

midiccionario={"Alemania":"Berlín", "Francia":"París", "Reino Unido": "Londres", "España": "Madrid"} # Empiezan con llaves {key:value}

print(midiccionario["Francia"]) # Acceder al valor de la clave no olvidar comillas ""

print(midiccionario["España"])

print(midiccionario)

#Operaciones con diccionarios

#Agregar elementos

midiccionario["Italia"]="Lisboa"

print(midiccionario)

midiccionario["Italia"]="Roma"

print(midiccionario)

#Elimar elementos

del midiccionario["Reino Unido"]

print(midiccionario)

#Crear diccionario con diferentes tipos de variables, str, int, float, tuple

my_dicc={"Real madrid":14, "f(x)":45, "Mosqueteros":3}

print(my_dicc)

#Utilizar una tupla para asignar las claves a cada uno de los valores

#Creamos una tupla

mitupla=["España", "Francia", "Reino Unido", "Alemania"]

#Diccionario que tome a la tupla para asignar las claves a cada uno de los valores realizamos lo siguiente  

tdicc={mitupla[0]: "Madrid", mitupla[1]:"París", mitupla[2]:"Londres", mitupla[3]:"Berlín"}

print(tdicc)

#Imprimir algún elemento en concreto o valor concreto de la diccionario anterior

#Por medio de tupla

print(midiccionario[mitupla[1]])

#Por medio de key:"clave"

print(midiccionario["Francia"])


#Diccionario que almacene una tupla completa, almacene en su interior junto con otros valores una tupla entera de valores

#Declaramos el diccionario y en anillos agregamos el valor de tupla []  key:value

adicc={23:"Jordan", "Nombre":"Michael", "Equipo": "Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}

print(adicc)


#Acceder al equipo que jugó Jordan

print(adicc["Equipo"])

# acceder a los anillos ganados en las temporadas

print(adicc["anillos"])

# Guardar un diccionario en otro diccionario {{"key": value=[]}}

bdicc={23:"Jordan", "Nombre":"Michael", "Equipo": "Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}


print(bdicc["anillos"])

#Método keys()=devuelve las claves, método values()=devuelve los valores

print(bdicc.keys())

print(bdicc.values())

#longitud del diccionario len()

print(len(bdicc))