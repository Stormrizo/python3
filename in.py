#Operador in

#Verificaremos si un programa en el cual vamos a imaginarnos que se trata de un alumno que cursará una asignatura y tiene que escoger una asignatura optativa, opcional y se le va a dar entre esas asiganturas un listado, del cual no se puede salir

#Si el alumno escoge una de las que se le ofrece en el listado, entonces el programa funciona adecuadamente y se le informa de la asigantura que ha escogido, si el alumno no escoge una de las que está en el listado, el programa le dirá que la asignatura no está contemplada.

#Empezamos...

print("Título: asinaturas optativas año 2023 FCFM- Física")

#Imprimiremos el listado de las asinaturas optativas

print("Licenciatura en Física - Espacios vectoriales, Cálculo diferencial en varias variables")


opcion=input("Escribe la asignatura escogida:")

asignatura=opcion.lower() #aQUÍ VERIFICAMOS QUE LOS VALORES DE ENTRADA SE TRANSFORMEN EN minusculas, así cualquier palabra escrita eroneamente con una mezcla de letras mayúsculas y minúsculas será correcta.

if asignatura in ("espacios vectoriales", "cálculo diferencial en varias variables"):
    print(f"La asignatura elegida es {asignatura}")

else: 
    print("La asignatura escogida no está contemplada")

#Recordemos que python es un lenguaje case sensitive, lo que significa que distingue entre mayúsculas y minúsculas

