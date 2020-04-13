#!/usr/bin/python3
# Ejercicio 9 de fundamentos de python

"""
Script para perdir un numero al usuario indefinitamente hasta
que el usuario ingrese 1111.
"""

num = 0

while num != 1111:
    num = int(input("Dame un numero: "))
    print (f"el numero ingresado es: {num}")