#!/usr/bin/env python
# coding: utf-8
# importaciones de librerias


from models import Usuario, Registro, Producto
from utils import limpiarPantalla

#menu=menu_admi()
ruta_archivo = "./archivos/vendedor.txt"
ruta_archivo1 = "./archivos/registroVenta.txt"
ruta_archivo2 = "./archivos/producto.txt"
ruta_archivo3 = "./archivos/imprimircal.txt"

def menu_vendedor():   #este lugar se creo el submenu para el vendedor y sus opciones de venta
     while True:
        print("╔════════════════════════════════╗")
        print("║ Menú vendedor                  ║")
        print("╠════════════════════════════════╣")
        print("║[1] Emitir factura o boleta     ║")
        print("║[2] ver ventas                  ║")
        print("║[3] ver precios                 ║")
        print("║[4] salir                       ║")
        print("╚════════════════════════════════╝")
        
        op = input("Seleccione una opción: ")
        match (op):   #utilizamos un match para crear una lista para el vendedor y asi poder unir las funciones a esta
            case "1": 
                limpiarPantalla()
                registro_venta()# primera funcion para crear una factura o boleta
            case "2": 
                limpiarPantalla()
                imprimirVenta(ruta_archivo1)# segunda funcion para ver las ventas
            case "3":
                limpiarPantalla()
                nombre = input("ingrese nombre: ")
                fila = str(precio(nombre))
                print(f"{fila}")# en esta funcion podemos ver los precios que el administrador nos brinda
            case "4":
                limpiarPantalla()
                break # esta opcion es para que el vendedor pueda salir del submenu
            
            case _:
                print("ERROR!! opcion incorrecta") # aqui el sistema dira que hubo un error si se pone otra opcion 
                                                   #aparte de las 4 que podemos incluir



def crearUsuario(): # esta opcion sirbe para crear un usuario y contraseña para el vendedor
    dni = input("DNI: ")
    password = input("Password: ")
    nombres_apellidos = input("Nombres y Apellidos: ")
    direccion = input("Dirección: ")
    telefono = input("Telefono: ")
    email = input("E-mail: ")
    vendedor = Usuario(
        dni, password, nombres_apellidos, direccion, telefono, email
    )

    archivoUsuario = open(ruta_archivo, "a")
    archivoUsuario.write(str(vendedor))
    archivoUsuario.close


def buscarUsuario(dni): # esta funcion sirbe para ubicar ala cuenta del vendedor
    archivoUsuarios = open(ruta_archivo, "r")
    for linea in archivoUsuarios.readlines():
        fila = linea.split(";")
        # print(atributo)
        if fila[0] == dni:
            return True
    return False


def validarAcceso(dni, password):
    archivoUsuarios = open(ruta_archivo, "r")
    for linea in archivoUsuarios.readlines():
        fila = linea.split(";")
        # print(atributo)
        if fila[0] == dni and fila[1] == password:
            limpiarPantalla()
            menu_vendedor()
        else:
            print("ERROR!! de contraseña o DNI")


def imprimirRegistro(ruta):
    archivoProducto = open(ruta_archivo, "r")
    print("DNI       \tContraseña\t\tNombre y apellido       \t\tDirección       \tTelefono    \tE-mail")
    for linea in archivoProducto.readlines():
        atributo = linea.split(";")
        print(
            "{}\t{}\t{}\t\t{}\t{}\t\t{}".format(
                atributo[0], atributo[1], atributo[2], atributo[3], atributo[4], atributo[5] 
            )
        )
    archivoProducto.close()

def registro_venta():
    tipo_comb = input("Indique tipo de comprobante:  ")
    n_venta = input("ingrese numero de venta:  ")
    n_documento = input("Ingrese numero de documento o RUC: ")
    razon_s = input("Ingrese razon social o nombre:  ")
    #establecimiento = "AV. las americas #69"
    #tipo_m = "soles"
    producto = input("Ingrese producto: ")
#--------------------------------------------------------------------------
    precio=float(input("precio: "))
    cantidad=float(input("cantidad: "))
    total = calcular(precio,cantidad)
#-------------------------------------------------------------------------
    venta = Registro(
        tipo_comb, n_venta, n_documento, razon_s, producto, precio, cantidad,total
    )

    archivoUsuario = open(ruta_archivo1, "a")
    archivoUsuario.write(str(venta))
    archivoUsuario.close()

def precio(nombre):   #esto sirbe para sacar los precios finales sacando el igv y otras cosas.
    precio = None
    archivoPrecio = open(ruta_archivo2, "r")
    for linea in archivoPrecio.readlines():
        fila = linea.split(";")
        # print(atributo)
        if nombre == fila[1]:
            precio = Producto(fila[0],fila[1],fila[2])
            break
    archivoPrecio.close()

    return precio

def calcular(precio:float,cantidad:float):
    total = precio * cantidad
    igv = total * 0.18
    subtotal = total - igv
    return subtotal, igv, total
    #print("El subtotal de la venta es: ", subtotal)
    #print("EL IGV: ", igv)
    #print("El total de la venta", total)

#---------------------------------------------------------------
def imprimirVenta(ruta): # esta funcion sirbe para poder mostrar los precios que da el admin.
    archivoProducto = open(ruta_archivo1, "r")
    print("Tipo comprobante       \tNro de venta\t\tRazon social       \t\tProducto       \tPrecio   \tcantidad \ttotal")
    for linea in archivoProducto.readlines():
        atributo = linea.split(";")
        print(
            "{}\t{}\t{}\t\t{}\t{}\t\t{}\t{}".format(
                atributo[0], atributo[1], atributo[2], atributo[3], atributo[4], atributo[5], atributo[6]
            )
        )
    archivoProducto.close()  


    


