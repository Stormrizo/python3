#Vamos a ver concretamente como funciona el condicional if cuando se acompaña de una instrucción else y de una instrucción elif

#Programa de control de acceso para mayoría de edad
#Else se puede traducir como "¿Y si no es verdad?"
#If puede traducirse como un "sí condicional" que verdaderamente es su significado.

print("Verificación de acceso")

contador=0

edad_usuario=int(input("Introduce tu edad, por favor:")) #input admite valores enteros en este caso

#Evaluamos la edad para saber si eres mayor de edad o no

while edad_usuario<0: #Mientras que la edad sea negativa

    if edad_usuario<0: #si se cumple que la edad sea negativa
        contador+=1     #Contador valdrá 1
    
    if contador == 3: #si el contador vale 3. Finaliza el bucle while/ programa con la instrucción brake
          print("Has excedido el número máximo de intentos") #Se imprime que se ha excedido los intentos
          break; #Finaliza el bucle

    print("No puedo interpretar tu edad. La edad mínima de acceso es de 25 años y la edad máxima es de 65. No podemos admitir personas menores de 25 y de la tercera edad por cuestiones de salud.") #Mientras que la edad sea negativa se imprime el texto

    edad_usuario=int(input("vuelve a introducir tu edad, por favor:")) #Mientras que la edad sea neg se vuelve a preguntar


#Si dejamos el programa aquí, funciona, lo que ocurre es que no hemos dado una instrucción qué debe hacer si la condición es falsa, es decir que sea mayor de edad.

#Entonces

while edad_usuario>110:

    if edad_usuario>110:
        contador+=1
  
    if contador == 3: #si el contador vale 3. Finaliza el bucle while/ programa con la instrucción brake
        print("Has excedido el número máximo de intentos") 
        break;
  
    print("No puedo interpretar tu edad. La edad mínima de acceso es de 25 años y la edad máxima es de 65. No podemos admitir personas menores de 25 y de la tercera edad por cuestiones de salud.") #Mientras que la edad sea negativa se imprime el texto
  
    edad_usuario=int(input("vuelve a introducir tu edad, por favor:")) #Mientras que la edad sea neg se vuelve a preguntar 




if 0<=edad_usuario<12:
        print("No puedes pasar, no eres mayor de edad y eres demasiado joven. La edad mínima de acceso es de 25 años y la edad máxima es de 65.  No podemos admitir personas menores de 25 y de la tercera edad por cuestiones de salud. Lo sentimos")

elif 12<=edad_usuario<15:
        print("No puedes pasar, no eres mayor de edad. La edad mínima de acceso es de 25 años y la edad máxima es de 65.  No podemos admitir personas menores de 25 y de la tercera edad por cuestiones de salud. Lo sentimos")
    
elif 15<=edad_usuario<=17:
        print("Podrías pasar con la supervición de un adulto, ya que no eres mayor de edad. La edad mínima de acceso es de 25 años y la edad máxima es de 65.  No podemos admitir personas menores de 25 y de la tercera edad por cuestiones de salud. Lo sentimos")

elif 18<=edad_usuario<=24:
        print("Eres mayor de edad, sin embargo no podemos darte acceso, a menos que estés acompañado de alguien mínimo de 25 años. La edad mínima de acceso es de 25 años y la edad máxima es de 65.  No podemos admitir personas menores de 25 y de la tercera edad por cuestiones de salud. Realmente lo sentimos :(")

elif 25<=edad_usuario<=65:
    print("Puede pasar. La edad mínima de acceso es de 25 años y la edad máxima es de 65. No podemos admitir personas menores de 25 y de la tercera edad por cuestiones de salud... disfrute y evite el exceso.")

elif 66<edad_usuario<109:
    print("No puede pasar. La edad mínima de acceso es de 25 años y la edad máxima es de 65. No podemos admitir personas menores de 25 y de la tercera edad por cuestiones de salud. Realmente lo sentimos :(")

