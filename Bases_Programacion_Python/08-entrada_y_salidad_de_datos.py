#!/usr/bin/python3
# Entrada y salidad de datos en python

# Entrada de datos
nombre = input("Cual es tu nombre?: ")
edad = input("Cual es tu edad?: ")
# Salida de datos
print(f"saludos, {nombre}, veo que tienes {edad} años")

# En caso de querer concatenar distintos tipos de datos como un int y un str
# Se debe hacer conversion de tipo

print(f"saludos, {nombre}, veo que tienes {int(edad) + 2} años")