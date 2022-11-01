#Concatenación de operadores de comparación.

edad=7

#Condicional que evalúe si en función de la edad introduida es una edad correcta o incorrecta

if edad<100: #Controlamos que la edad sea menor que 100
    print("Edad correcta")

else:
  print("Edad incorrecta")


otra_edad=723

#Condicional que evalúe si en función de la edad introduida es una edad correcta o incorrecta

if otra_edad<100: #Controlamos que la edad sea menor que 100
    print("Edad correcta")

else:
  print("Edad incorrecta")

#Aquí ocurre algo incorrecto, la edad negativa noss dice que es correcta, sin embargo a pesar de que cumple la condición de if, esto está mal, a pesar de que el flujo de ejecución vaya correcto.

otra_edad2=-723

#Condicional que evalúe si en función de la edad introduida es una edad correcta o incorrecta

if otra_edad2<100: #Controlamos que la edad sea menor que 100
    print("Edad correcta")

else:
  print("Edad incorrecta")

#¿Cómo podemos solucionar este problema? R= se puede evitar añadiendo un condicional elif, lo único que ocurre es que si queremos abreviar código, pues tenemos alternativas con la concatenación de operadores de comparación.

#Por ejemplo

otra_edad3=-723

#Consiste en que dentro del condicional if utilizar varias veces el operador de comparación:

if 0<otra_edad3<100: #Controlamos que la edad sea acotada; positiva y menor que 100
    print("Edad correcta")

else:
  print("Edad incorrecta")


#Otro ejemplo:

#Creamos un  programa que evalúa varios salarios de personas en una empresa

salario_presidente = int(input("Introduce el salario del presidente:"))
mensual= input("¿Cada cuánto se recibe la nómina en esta empresa (mensuales, quincenales, semanales...etc)?:")
usd_mxn= input("¿En que divisa recibe la nómina el administrativo (USD, MXN, Euro, Rupias...etc)?:")
print(f"El salario del presidente es {salario_presidente} {usd_mxn} {mensual}")

salario_director=int(input("Introduce el salario del CEO:"))
mensual= input("¿Cada cuánto se recibe la nómina en esta empresa (mensuales, quincenales, semanales...etc)?:")
usd_mxn= input("¿En que divisa recibe la nómina el administrativo (USD, MXN, Euro, Rupias...etc)?:")
print(f"El salario del presidente es {salario_director} {usd_mxn} {mensual}")

salario_jefe_area=int(input("Introduce el salario del jefe de área:"))
mensual= input("¿Cada cuánto se recibe la nómina en esta empresa (mensuales, quincenales, semanales...etc)?:")
usd_mxn= input("¿En que divisa recibe la nómina el administrativo (USD, MXN, Euro, Rupias...etc)?:")
print(f"El salario del presidente es {salario_jefe_area} {usd_mxn} {mensual}")

salario_administrativo=int(input("Introduce el salario del administrativo:"))
mensual= input("¿Cada cuánto se recibe la nómina en esta empresa (mensuales, quincenales, semanales...etc)?:")
usd_mxn= input("¿En que divisa recibe la nómina el administrativo (USD, MXN, Euro, Rupias...etc)?:")
print(f"El salario del administrativo es {salario_administrativo} {usd_mxn} {mensual}")

#Ahora veremos la concatenación de varias variables, la construcción del condicional, veremos si los sueldos tienen cierta lógica:

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")

else:
    print("Algo falla en esta empresa.") 







