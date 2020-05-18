#!/usr/bin/python3
# Funciones y metodos predefinidos para listas en python

cantantes = ["Freddy Mercury", "Bruce Dickinson", "Simone Simmons", "Brian Johnson"]
numeros = [1, 2, 5, 8, 3, 4]

# Ordenar
print(numeros)
numeros.sort()
print(numeros)

# Anadir elementos al final
cantantes.append("Serj Tankian")
print(cantantes)

# Anadir elementos en una posicion especifica
cantantes.insert(1, "Tarja Turunen")
print(cantantes)

# Eliminar elementos dentro de una lista por posicion
cantantes.pop(1)
print(cantantes)

# Eliminar elementos por nombre
cantantes.remove("Simone Simmons")
print(cantantes)

# Dar la vuelta a una lista
print(numeros)
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print("Freddy Mercury" in cantantes)

# Cantidad de elementos dentro de una lista
print(len(cantantes))

# Cuantas veces aparece un numero dentro de una lista
print(numeros.count(2))

# Saber el indice de un elemento
print(cantantes.index("Bruce Dickinson"))

# Unir Lista
cantantes.extend(numeros)
print(cantantes)
