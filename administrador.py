import os
#from main import inicio
from productos import crearProducto, cambiar_precio
from vendedor import crearUsuario, menu_vendedor, imprimirRegistro, imprimirVenta


#iniciar = inicio()
def limpiarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

#------------------------------------------------------------------------------------
ruta_archivo1 = "./archivos/registroVenta.txt"
ruta_archivo = "./archivos/producto.txt"
ruta = "./archivos/vendedor.txt"
def menu_admi():
    while True:
        print("╔════════════════════════════════╗")
        print("║ Menú administrador             ║")
        print("╠════════════════════════════════╣")
        print("║[1] Actualizar precios          ║")
        print("║[2] agregar productos           ║")
        print("║[3] Ver ventas diarias          ║")
        print("║[4] Menú vendedor               ║")
        print("║[5] Crear cuenta (vendedor)     ║")
        print("║[6] Mostar lista de vendedores  ║")
        print("║[7] salir                       ║")
        print("╚════════════════════════════════╝")
        
        op = input("Seleccione una opción: ")
        match (op):
            case "1": 
                limpiarPantalla()
                n_precio = input("Ingrese actualize precio: ")
                nfila = int(input("ingrese fila de registro: "))
                nfila = list(map(int, str(nfila)))
                cambiar_precio(ruta_archivo, nfila, 2, n_precio)
            case "2": 
                limpiarPantalla()
                crearProducto()
            case "3":
                limpiarPantalla()
                imprimirVenta(ruta_archivo1)
            case "4":
                limpiarPantalla()
                menu_vendedor()
            case "5":
                limpiarPantalla()
                crearUsuario()
            case "6":
                limpiarPantalla()
                imprimirRegistro(ruta)
            case "7":
                limpiarPantalla()
                #inicio()
                break
            case _:
                print("ERROR!! opcion incorrecta")

#-------------------------------------------------------------------

