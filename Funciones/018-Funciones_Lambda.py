#!/usr/bin/python3
# Funciones Lambda en python

"""
Una funcion lambda es una funcion anonima, es decir
que no tiene nombre completo o parametros, sirven para tareas
simples y pequenas, pero que pueden ser repetitivas

Debe estar definida en una sola linea
"""

get_Year = lambda year: f"The year is {year}"

print(get_Year(2020))