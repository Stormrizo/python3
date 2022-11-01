#Debemos calcular el valor aproximado de pi con el método de Montecarlo, para ello vamos a importar el paquete random, ya sea con math.random o con el módulo numpy as np, de esta manera podremos obtener números de manera aleatoria, esto porque los necesitamos la mayor cantidad de números para poder plasmar adecuadamente el método (por medio del uso de bucles).

import numpy as np

#Necesitamos crear una fución que recree el método de Montecarlo...

#Supongamos que dibujamos un cuadrado de lado l, dentro de este mismo estará contenido un círculo de radio igual a l/2.

#Sabemos que el área del círculo es (/pi*(r**2)) y el área del cuadrado es (l**2), expresando el área del círculo en términos de l, tenemos:

#                                  (\pi*)((l**2)/4)
  
# y la del cuadrado es:
 
#                                      (l**2)
 
# Ahora si realizamos una relación de proporcionalidad del área del círculo entre el área del cuadrado obtenemos que : 

#                                    (área del círculo)/(área del cuadrado) = \pi/4


#Aislamos a \pi y obtenemos:

#                                    4*((área del círculo)/(área del cuadrado)) = \pi

#Obtemos que \pi sería igual a 4 veces la razón entre el área círculo sobre el área del cuadrado.

# Si el área del círculo se relaciona con las bolitas que caen dentro de este, podremos definirla como n y para el cuadrado como las bolitas que caen fuera del círculo como N, sabemos que n<N dado que el círculo está circunscrito dentro del cuadrado. 

#En resumen, si las bolitas caen dentro del círculo serán casos favorables, si no caen dentro serán caso no favorables, es decir que caen en la región del cuadrado.


#Comienzo, definimos las variables a usar

#Fijemos el valor del radio del círculo en 1
#Entonces necesitamos que todo las bolitas estén dentro del radio del círculo para que sean considerados como casos favorables. 
#Como es un plano, necesitamos coordenadas(x,y), entonces necesitamos generar dos números aleatorios "p" y "q" entre 0 (el origen (0,0) ) y 1 (límite).
#Calculamos la fórmula de la circunferencia de radio 1 con los números aleatorios:

#                                          p**2 + q**2 =r**2, la llamaremos caso favorable
#Si la variable caso favorable es menor o igual que 1:

#                                           valor favorable<=1 

#No será favorable si la variable caso favorable es mayor que 1:

#                                           valor favorable>1 


#Con estos datos podemos emplear la fórmula anterior para conocer el valor aproximado de /pi

#                             4*n/N = \pi



#Ciclo del experimento de pi

#Variables que necesitamos:
N=1000 # Casos favorables o totales 
rep=700 #veces que se va a volver a realizar el experimento

for j in range(rep):
  valor=0 #Empezamos los lanzamientos en un valor de 0
  x=np.random.uniform(0,1,N).tolist() #Valor de la abscisa cuando la bolita cae en la circunferencia de radio 1
  y=np.random.uniform(0,1,N).tolist() #Valor de la ordenada cuando la bolita cae en la circunferencia, entre el origen y 1, tendremos n casos favorables, es decir 1000 coordenadas.
  
  #Vamos a usar la ecuación ordinaria de la circunferencia para verificar si el caso favorable está dentro del circulo... si el resultado es mayor que 1, entonces no es favorable y si es menor o igual que 1 está dentro del círculo.

  for m in range(N):
    cf=(x[m]**2)+(y[m]**2)
    if cf <= 1:
      valor +=1 #Si el caso favorable es menor o igual que uno, vamos a ir sumando casos

  float_v=float(valor) #Necesitamos convertir la variable valor a decimales.
  valor_de_pi= (4)*(float_v)/(N)

print(valor_de_pi)


 



