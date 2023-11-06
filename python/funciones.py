#-------------guardar_frase----------------------#

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

#-------------leer_archivo----------------------#

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
#-------------Intercambiar_textos----------------------#

def Intercambiar_textos():
    """
    Función que intercambia el contenido de los textos que uno selecione.

    @return: None.
    """

    # Solicitamos el nombre del primer archivo.
    nombre_archivo_1 = input("Introduce el nombre del primer archivo: ")

    # Solicitamos el nombre del segundo archivo.
    nombre_archivo_2 = input("Introduce el nombre del segundo archivo: ")

    # Leemos el contenido del primer archivo.
    contenido_archivo_1 = leer_archivo(nombre_archivo_1)

    # Leemos el contenido del segundo archivo.
    contenido_archivo_2 = leer_archivo(nombre_archivo_2)

    # Guardamos el contenido del segundo archivo en el primer archivo.
    guardar_frase(contenido_archivo_2, nombre_archivo_1)

    # Guardamos el contenido del primer archivo en el segundo archivo.
    guardar_frase(contenido_archivo_1, nombre_archivo_2)

    print("El contenido de los archivos se ha intercambiado correctamente.")
    
#-------------menu----------------------#

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
    print("4. Intercambiar ")
    print("0. Salir")

    # Solicitamos la opción al usuario.
    opc = input("Introduce una opción: ")

    # Validamos la opción del usuario.
    while opc not in ["0", "1", "2","3","4"]:
        print("Opción no válida.")
        opc = input("Introduce una opción: ")

    # Ejecutamos la opción seleccionada.
    if opc == "1":
        # Guardamos la frase.
        frase = input("Introduce la frase a guardar: ")
        nombre_archivo = input("Introduce el nombre del archivo: ")
        guardar_frase(frase, nombre_archivo)
        menu()
    elif opc == "2":
        # Leemos el archivo.
        nombre_archivo = input("Introduce el nombre del archivo: ")
        contenido = leer_archivo(nombre_archivo)
        print(contenido)
        menu()
    elif opc=="3":
        #acerca de 
        print("Nombre: Programa de edicion ")
        print("Version: 4")
        print("Autor:Pablo Mondragon ")
        menu()
    elif opc == "4":
        # Intercambiamos los textos.
        Intercambiar_textos()
        menu()
        
    else:
        # Salimos del programa.
        print("Gracias por usar el menú.")

#-------------despligue----------------------#

menu()