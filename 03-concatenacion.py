#!/usr/bin/python3
# Concatenacion en python

# Basicamente es poder unir dos variables

nombre = "David"
apellidos = "Latorre"
web = "latorredev.com"

print(nombre + " " + apellidos + " " + " - " + web)

# Se puede concatenar de otras forma.

print(f"{nombre} {apellidos} - {web}")

# Otra forma
print ("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))