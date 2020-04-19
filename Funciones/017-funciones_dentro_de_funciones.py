#!/usr/bin/python3
# Funciones dentro de funciones en python

def getNombre(nombre):
    texto = f"el nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("David", "Latorre"))