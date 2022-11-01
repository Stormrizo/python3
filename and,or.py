#El operador lógico and = y sí además
#El operador lógico or = o sí no

#Progama que evalúe si un alumno tiene derecho a beca o no tiene derecho a beca

#Lo que va a evaluar el programa son 3 cosas, distancia de la escuela hasta su hogar > 40km, si tiene más hermanos > 2 hermanos en el centro, evaluar el salario familiar <=20000


print("Título: Programa de becas año 2023")

#Guardar en variables los tres parámetros que vamos a solicitar

dist= float(input("Introduce la distancia aproximada que hay de tú hogar a la escuela, por favor:"))
km=input("Introduce si es en kilómetros (km) o metros (m - divide por 1000 si deseas convertirlo a km), por favor:")


bros= int(input("Introduce la cantidad de hermanos en el centro: "))
m=int(input("Introduce cuántos hermanos (hombres) tienes, por favor: "))
f=int(input("Introduce cuántas hermanos (mujeres) tienes, por favor: "))


sal=int(input("Introduce el ingreso anual promedio bruto:"))
bdfu=(input("Introduce la divisa:"))


#Verificar si se cumplen los requisitos:

if dist>40 and bros>2 or sal<=75000:
  print("Con la información proporcionada tenemos los siguientes datos")
  print(f"La distancia del hogar a la escuela es de {dist} {km}")
  print(f"La cantidad de hermanos en el centro es de {bros} de los cuales {m} son hombres y {f} son mujeres")
  print(f"El salario anual promedio es de {sal} {bdfu}")
  print(f"Con la información proporcionada eres candidato a obtener una beca. ¡Felicidades!")

else:
  print("Con la información proporcionada tenemos los siguientes datos")
  print(f"La distancia del hogar a la escuela es de {dist} {km}")
  print(f"La cantidad de hermanos es de {bros} de los cuales {m} son hombres y {f} son mujeres")
  print(f"El salario anual promedio es de {sal} {bdfu}")
  print(f"Lo sentimos con la información proporcionada no eres candidato a obtener una beca.")

