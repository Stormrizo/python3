#Estructuras de control de flujo
# Existen dos grandes grupos
# Condicionales y bucles
# A su vez cada uno de estos grupo tiene varias estructuras diferentes

#Empezaremos viendo los condicionales

# Instrucción: if

#¿Qué es el flujo de ejecución de un programa? - Es el orden con el que se ejecutan cada una de las instrucciones, es el orden que sigue el programa a la hora de leer y ejecutar esas instrucciones
# El orden en este fluio de ejecución es generalmente  de arriba a abajo. Aunque se puede ver alterado por diversas causas, una de ellas es debido a estructuras de control de flujo, modifican el orden natural de arriba hacia abajo en la ejecución de las instruciones de un programa


#Definiremos una función a la cual recibirá parámetro una nota y se encargará de decir si el alumno en función de la nota que recibe está aprobado o no

#Evaluar si la nota que le he hemos pasado como parámetro a la  función es inferior a 5, en caso sea verdad, debemos cambiar el valor de valoración de "aprobado" a "reprobado"                   
    
def evaluacion(nota):
    valoracion="aprobado"      #creamos una variable llamada valoracion y vamos a igualarla a "aprobado" 
    if nota <5: 
        valoracion="reprobado"
    return valoracion

print(evaluacion(7))

#Este sería el funcionamiento básico de un condicional if

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
      valoracion="reprobado"
    return valoracion 
  
print(evaluacion(4))

# Ahora, vanos a complicar un poco más este ejemplo. Vamos a introducir un código que nos permita introducir una nota por teclado, esa nota introducida por teclado entra dentro de la variable y se ejecuta la función.

print("Programa de evaluación de notas de alumnos")

#Vamos con la instrucción input( ), cuando el flujo de ejecución llegue a ella el programa se detendrá y se quedará a la espera de que introduzcamos un valor por teclado.

nota_alumno=float(input("Introduce tú calificación, por favor:")) #float() acepta valores decimales (flotantes), cualquier cosa que nosotros introduzcamos a tráves de una instrucción input es considerado como cadena de texto o string (str), es por eso que siempre debemos considerar valores númericos, ya sea float() o int(), en dado cado necesitamos usar números como valores de entrada.

#TAmbién la función input puede admitir parámetros para imprimir un mensaje, es muy habitual que dentro de la instrucción input se introduzca un mensaje, i.e. input("Introduce los valores de entrada:"), es decir, se consigue que antes del cursor parpadeante, salga este mensje, para que al usuario se le indique qué tipo de dato se espera.

#Cuando trabajamos con un condicional if y con funciones  es el término ámbito, es muy importante sabes que una variable solamente es accesible solamente dentro de un ámbito. Hay que tener claro donde comienza y donde termina esa función.

def calif(nota):
    valoracion="Felicidades, has aprobado gracias a tu esfuerzo y suerte"
    if nota<5:
          valoracion="Reprobado, no te preocupes, puedes recursar la materia y volver a intentar... tú puedes"
    return valoracion

print(calif(nota_alumno))  #siempre debemos dar la instrucción de impresión para que el programa se ejecure y finalice

