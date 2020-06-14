#!/usr/bin/python3
# Modulos en python

"""
Modulos: son funcionalidades ya hechas para reutilizar.
En python existen muchos, los puedes consultar aqui:

https://docs.python.org/3.8/installing/index.html

Podemos conseguir modulos que ya vienen en el lenguaje
Descargar otros de internet o crear nuestros propios modulso
"""

# import my_module --- llama el modulo
# from my_module import * --- Importa todas las funciones dentro del modulo
from my_module import holaMundo # Se importa solo funcion holaMundo

print(holaMundo("David"))

# Modulo de fechas
import datetime


print(datetime.date.today()) # Imprime la fecha de hoy

fecha_completa = datetime.datetime.now()

print(fecha_completa) # Fecha completa
print(fecha_completa.year) # Solo el año
print(fecha_completa.month) # Solo el mes
print(fecha_completa.day) # Solo el dia

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print(f"Mi fecha personalizada es: {fecha_personalizada}")
print(datetime.datetime.now().timestamp()) # Fecha formato UNIX

# Modulo matematicas
import math

print("Raiz cuadrada de 10: ", math.sqrt(10))
print ("Numero pi: ", float(math.pi))

# Modulo Random
import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15, 67))
