#!/usr/bin/env python3
# Gestion de archivos con python

# Importar el modulo que permite gestionar ficheros


from io import open
import pathlib # Para manejar la ruta absoluta
import shutil # Modulo para copiar, mover y eliminar archivos


# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero.txt"
archivo = open(ruta, "a+")

# Escribir
archivo.write("Soy un texto introducido desde un script en python \n")

# Cerrar
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
# contenido = archivo_lectura.read()
# print (contenido)

# Leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    print(frase)

# Copiar

ruta_original = str(pathlib.Path().absolute()) + "/fichero.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)

# Mover Archivo

ruta_original = str(pathlib.Path().absolute()) + "/fichero.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_movido.txt"

shutil.move(ruta_original, ruta_nueva)


# Eliminar Archivos

import os

os.remove(ruta_nueva)

# Comprobar si un ficero existe
import os.path

comprobar_ruta = (os.path.abspath("./") + "/fichero.txt") # ruta absoluta

print (comprobar_ruta) # Imprimir ruta absoluta

if os.path.isfile(os.path.abspath("./") + "/fichero.txt"):
    print("El fichero existe")
else:
    print("El fichero no existe")

