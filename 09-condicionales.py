#!/usr/bin/python3
# condicinales en python

# Una estructura de control nos permite ejecutar un grupo de instrucciones u
# otro dependiendo de las condiciones que se cumplan

# Condicional if
print("######### Ejemplo 1 ##############")

color = input("Adivina mi color favorito: ")


if color == "rojo":
    print("Color correcto")
else:
    print("Color incorrecto") 

# Operadores de comparacion
"""
== Igual a
!= Diferente
< Mayor que
> Menor que
<= Mayor o igual que
>= Menor o igual que
"""

# Ejemplo

year = int(input("En que año estamos?: "))

if year >= 2021:
    print("Estamos en 2021 o un año posterior")
else:
    print("Estamos en un año anterior a 2021")

# if anidados

nombre = input("Cual es tu nombre?: ")
ciudad = input("cual es tu ciudad?: ")
continente = input("Cual es tu conteniente?: ")
edad = int(input("Cual es tu edad?: "))
mayoria_de_edad = 18

if edad >= mayoria_de_edad:
    print("El usuario es mayor de edad")

    if continente == "America":
        print("El usuario es de America")

        if ciudad == "Bogota":
            print("El usuario es de Bogota")
        else: 
            print("El usuario no es de Bogota")
    else:
        print("El usuario no es de America")

else:
    print("El usuario no es mayor de edad")

# Elif

dia = int(input("Que numero de la semana (De 1 a 7 )es hoy?: "))

if dia == 1:
    print("Hoy es Lunes")
elif dia == 2:
    print("Hoy es Martes")
elif dia == 3:
    print("Hoy es Miercoles")
elif dia == 4:
    print("Hoy es Jueves")
elif dia == 5:
    print("Hoy es Viernes")
elif dia == 6:
    print("Hoy es Sabado")
else:
    print("Hoy es Sabado o Domingo")

# operadores logicos

"""
and Y
or O
negacion !
no not
"""

edad_minima = 28
edad_maxima = 65
edad_oficial = int(input("Cual es tu edad?: "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No estas en edad de trabajar")