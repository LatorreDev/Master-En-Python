#!/usr/bin/python3
# Tipos de datos en python

# Tipo de dato None, indica que no tiene nada
nada = None
print(nada)
print(type(nada))

# Linea divisoria
print ("---------------------------------------")

# Tipo de dato String o cadena
cadena = "Hola, esta es una cadena"
print(cadena)
print(type(cadena))

# Linea divisoria
print ("---------------------------------------")

# Tipo de dato entero
entero = 42
print(entero)
print(type(entero))

# Linea divisoria
print ("---------------------------------------")

# Tipo de dato flotante, numero decimal
flotante = 7.7
print(flotante)
print(type(flotante))

# Linea divisoria
print ("---------------------------------------")

# Tipo de dato booleano, indica si es verdadero o falso
booleano = True
print(booleano)
print(type(booleano))

# Linea divisoria
print ("---------------------------------------")

# Tipo de dato lista, se declara con llaves cuadradas
lista = [10,20,30,40]
print(lista)
print(type(lista))

# Linea divisoria
print ("---------------------------------------")

# Tipo de dato tupla, una lista cuyos valores no pueden cambiar, se declara con parentesis
tupla=("master", "en", "python")
print(tupla)
print(type(tupla))

# Linea divisoria
print ("---------------------------------------")

# Tipo de dato diccionario, permite tener una collecion de datos con clave y valor, se declara con corchetes
# Sirve para los JSON
diccionario = {
    "nombre" : "David",
    "apellido" : "Latorre",
    "web" : "latorredev.com"
}
print(diccionario)
print(type(diccionario))

# Linea divisoria
print ("---------------------------------------")

# Hay otros tipos de datos mas especificos y confusos como range, byte, byte array, memoryview, etc.

# imprimir tipo de variable
# print(type(nombre_de_variable))