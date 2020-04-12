#!/usr/bin/python3
# Ejercicio 7 de los fundamentos de python

"""
Mostrar los numeros impares entre el rango
de 2 numeros que decida el usuario
"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

for contador in range ((num1 + 1), (num2)):
    if(contador%2==1):
        print(contador)