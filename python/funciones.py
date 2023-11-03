def guardar_frase(frase, nombre_archivo):
    """
    Función que guarda una frase en un archivo.

    @param: string      frase.
    @param: string      nombre_archivo.
    """

    # Abrimos el archivo en modo de escritura.
    archivo = open(nombre_archivo, "w")

    # Escribimos la frase en el archivo.
    archivo.write(frase)

    # Cerramos el archivo.
    archivo.close()


def leer_archivo(nombre_archivo):
    """
    Función que lee el contenido de un archivo.

    @param: string      nombre_archivo.
    """

    # Abrimos el archivo en modo de lectura.
    archivo = open(nombre_archivo, "r")

    # Leemos el contenido del archivo.
    contenido = archivo.read()

    # Cerramos el archivo.
    archivo.close()

    return contenido


def menu():
    """
    Función que muestra un menú con las opciones disponibles.
    """

    # Imprimimos un mensaje de bienvenida.
    print("Bienvenido al menú.")

    # Mostramos el menú.
    print("1. Guardar frase")
    print("2. Leer archivo")
    print("3. Acerca de ")
    print("0. Salir")

    # Solicitamos la opción al usuario.
    opc = input("Introduce una opción: ")

    # Validamos la opción del usuario.
    while opc not in ["0", "1", "2","3"]:
        print("Opción no válida.")
        opc = input("Introduce una opción: ")

    # Ejecutamos la opción seleccionada.
    if opc == "1":
        # Guardamos la frase.
        frase = input("Introduce la frase a guardar: ")
        nombre_archivo = input("Introduce el nombre del archivo: ")
        guardar_frase(frase, nombre_archivo)
    elif opc == "2":
        # Leemos el archivo.
        nombre_archivo = input("Introduce el nombre del archivo: ")
        contenido = leer_archivo(nombre_archivo)
        print(contenido)
    elif opc=="3":
        #acerca de 
        print("Nombre: Programa de edicion ")
        print("Version: 3")
        print("Autor:Pablo Mondragon ")
        
    else:
        # Salimos del programa.
        print("Gracias por usar el menú.")


if __name__ == "__main__":
    menu()
