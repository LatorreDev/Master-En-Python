#!/usr/bin/python3
# Funciones predefinidas en python3

nombre=input("Ingrese su nombre: ")

print(type(nombre))


# Detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Es un string")
else:
    print("No es un string")
if not isinstance(nombre, float):
    print ("La variable no es un decimal")

# Limpiar espacios

frase = "     mi contenido      "
print(frase)
print(frase.strip())

# Eliminar variables

year = 2020
print(year)
del year # Borra la variable

# Comprobar variables vacias

texto = " ff "

if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print(f"la variables contiene {len(texto)} caracteres")

# Encontrar caracteres

frase = "La vida es una caca"

print(frase.find("caca"))

# Reemplazar palabras en un string

nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# Mayusculas a minusculas

print(nombre)
print(nombre.lower())
print(nombre.upper())
