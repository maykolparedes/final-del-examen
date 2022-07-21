import time

from models import Producto

ruta_archivo = "./archivos/producto.txt"


def crearProducto():
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    precio = input("Precio: ")

    combustible = Producto(codigo, nombre, precio)

    archivoProducto = open(ruta_archivo, "a")
    archivoProducto.write(str(combustible))
    archivoProducto.close

def cambiar_precio(ruta, filas, columna, nuevo_dato):
    contenido = list()
    with open(ruta, "r+") as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila - 1].split(";")
            columnas[columna] = nuevo_dato
            contenido[fila - 1] = ";".join(columnas) + "\n"
    with open(ruta, "w") as archivo:
        archivo.writelines(contenido)
