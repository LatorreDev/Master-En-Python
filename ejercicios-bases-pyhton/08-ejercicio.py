#!/usr/bin/python3
# Ejercicio 8 de fundamentos de python.

"""
Script para saber cuanto es el X porciento de X numero
"""

num1 = int(input("Ingrese el numero base: "))
num2 = int(input("Ingrese el porcentaje a saber: "))

if num1 or num2 == 0:
    print("Use un numero diferente de 0")

print(f"El {num2}% de {num1} es: {num1 * num2 / 100}")