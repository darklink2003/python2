#crea una funcion que guarde en un archivo cualquier frase, con cualquier nombre en python

def guardar_frase(frase, nombre_archivo):
      """
    Función que crea una frase y modifica un documento txt 
    
    @param: string      frase.
    @param: string      nombre_archivo.
    """

  # Abrimos el archivo en modo de escritura.
  archivo = open(nombre_archivo, "w")

  # Escribimos la frase en el archivo.
  archivo.write(frase)

  # Cerramos el archivo.
  archivo.close()

  return archivo

#-----------------------Despliegue----------------------------------#

# Ejemplo de uso:
frase=input("Digite una frase ")
nombre_archivo =input("Digite el nombre del archivo ")

archivo = guardar_frase(frase, nombre_archivo)

print(f"La frase se guardó en el archivo {nombre_archivo}.")



