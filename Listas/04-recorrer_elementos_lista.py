#!/usr/bin/python3
# Recorrer y mostrar una lista

# Funcion para crear una linea divisoria
def linea_div():
    print("**************************************")

linea_div()
print("\tListado peliculas")
linea_div()
# Lista
peliculas = ["Batman", "Spiderman", "El senor de los anillos", "Megamente", "Jumanji"]

# Agregar elementos a una lista
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Ingrese la nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula) # Metodo append agrega elementos al final de una lista

# Recorrer lista
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1} {pelicula}") # El +1 nos permite sumas 1 en el print del indice
    # y mostrar una numeracion "natural"
