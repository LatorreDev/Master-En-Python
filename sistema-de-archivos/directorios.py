#!/usr/bin/env python3
# Trabajar con directorios usando modulos

import os, shutil

# Crear carpeta
if not os.path.isdir("./micarpeta"):
    os.mkdir("./micarpeta")
    print("Carpeta creada")
else:
    print("Ya existe el directorio")

# Eliminar
# if os.path.isdir("./micarpeta"):
#    os.rmdir("./micarpeta")
#    print("Carpeta eliminada")

# Copiar
ruta_original = "./micarpeta"
ruta_nueva = "./micarpetacopiada"

shutil.copytree(ruta_original, ruta_nueva)

# Eliminar
# os.rmdir("./micarpetacopiada")

# Listar contenido de una carpeta
print ("contenido de mi carpeta")

contenido = os.listdir("./micarpeta")

for fichero in contenido:
    print(f"Fichero: {fichero}")

