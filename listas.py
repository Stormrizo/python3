milista=["María", "Pepe", "Martha", "Antonio"]

print(milista)

print(milista[0:3]) #acceder desde el primer elemento hasta el 2

print(milista[0:2]) #Los primeos dos elementos

print(milista[2:0]) # Accede a los dos últimos elementos milista=["María [0]", "Pepe [1]", "Martha[2]", "Antonio[3]"]

milista.append("Carlos") # Append agrega el elemento al final de nuestra lista

milista.insert(2,"Paco") # Insert pide dos argumentos, el primer argumento es el índice y el segundo el elemento a agregar

print(milista[:])

milista.extend(["Mobil", 3, "delta", "DW"]) #Con Extend agregamos varios elementos a una lista

print(milista[:])


print(milista.index("Carlos")) #¿Qué índice tiene Carlos (!= posición )?

print("Ernesto" in milista) #¿Ernesto se encuentra en mi lista?


milista.remove("Mobil") #remove elimina elementos

print(milista[:])

milista.pop() #elimina el último elemento de la lista

print(milista[:])