#!/usr/bin/python3
# Ejercicio 5 de fundamentos en python

"""
Crea un script que muestre todos los numeros 
entre dos numeros que diga el usuario
"""

contador = 0
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

num2 -= 1

for contador in range (num1, num2):
    num1 += 1
    print(num1)