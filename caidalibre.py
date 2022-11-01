#Este programa se basa en el cálculo de la suma de la energía cinética y la energía potencial de un objeto, se quiere demostrar que la energía se conserva en cada momento de la caída de la bola.

#Tomaremos sólo tres valores como el dominio de la función, es decir sólo tendremos 3 parámetros, dado que la velocidad es posible calcularla expresandola en términos de estos parámetros:
#
# 
#                          v=(2(h)*9.8)**(1/2) 
 
import math
import numpy as np

gra_pos=9.81
gra_neg=-9.81

def lista_EMvariable(m,h_i,h_n):
  """
  Función que toma como parámetros a la masa, y las alturas de un edificio
  Out=Se devulven resultados de la energía cinética y potencial de un objeto arrojado desde una altura h
  """
  h=h_n-h_i  #h_{n} altura al final, #altura al inicio
  En_C=str((1/2)*(m)*((2*(-h)*(9.81))))
  En_P=str((m)*(9.81)*(h+h_i)) 
  energia_total=float(En_C)+float(En_P)
  energias_sistema={En_P, En_C} #en forma de diccionario
  lista_energia=[-h, En_C,En_P,energia_total]
  print(lista_energia)

for g in np.arange(0,1001,10):  #Arrelo desde 0 hasta 100 en 10 en 10, va de 10, 20, 30, 40, 50, 60,..., 100
  lista_EMvariable(50,1000,g)