print("verificación de acceso")

edad=int(input("Introduce tu edad, por favor: "))

if edad <18:
    print("No puedes pasar")

elif edad>100:  #Elif= else no se acompaña del if más cercano, sino de ambos. ELIF= y si además.
    print("Edad incorrecta")
    print("Vuelve a introducir tu edad, por favor: ")

else: # Else=Y si no es verdad. Cada else debe ir acompañado de su correspondiente if o el if más cercano, if puede ir sin ningún else y es posible tener solo un if. Else debe ir emparejado con un if siempre.

#Si nuestro código tiene elif e if, entonces else funciona con los dos condicionales que tiene en la parte superior, es decir, entra en el else cuando nada de lo anterior se ha cumplido, no cuando el if más cercano no se ha cumplido, sino nada de lo anterior.
    print("Puedes pasar")


#Otro ejemplo

nota_calif=float(input("¿Cuál es tu calificación?:"))

if nota_calif <5:
    print("Insuficiente. Reprobado")

if nota_calif<6:
    print("Suficiente. Has aprobado")

if nota_calif<7:
    print("Bien. Has aprobado")

if nota_calif<9:
    print("Notable. Felicidades")
else:
    print("Sobresaliente")

#Está claro que si nada de lo anterior es cierto, pues entonces tendrá un sobresaliente. Esté programa funcionará mal, ya que el else se está acompañando del último if, es decir del anterior. Si tenemos cualquier nota que no sea 9 o 10, pues me va a sacar la nota correspodiente e imprimirá insuficiente, suficiente y bien, luego... sobresaliente.

#La forma correcta sería:

calif=float(input("¿Cuál es tu calificación?:"))

if calif <5: #Si calif es menor a 5 imprime:
    print("Insuficiente. Reprobado")

elif calif<6: #Si calif no es menor a 5. De otro modo si calif es menor que 6 imprime:
    print("Suficiente. Has aprobado")

elif calif<7: #Si calif no es menor a 6. De otro modo si calif es menor que 7 imprime:
    print("Bien. Has aprobado")

elif calif<9: #Si calif no es menor a 7. De otro modo si calif es menor que 9 imprime:
    print("Notable. Felicidades")

else:         #Si calif no es menor a 5,6,7 y 9. De otro modo imprime:
    print("Sobresaliente")