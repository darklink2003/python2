import time

def es_numero(texto=""):
    
    """
    Función que devuelve si un texto representa un número o no.
    https://www.w3schools.com/python/ref_string_isnumeric.asp
    -1 para no es número, y 1 para sí es número.
    @param: texto   Representa o no un número, incluso valida el vacío.
    @return: Real   1 o -1.
    """
    
    salida = 1
    
    if texto.isnumeric() == False:
        salida = -1 
        
    return salida


def imprimir_color_amarillo(mensaje):
    """
    https://python-para-impacientes.blogspot.com/2016/09/dar-color-las-salidas-en-la-consola.html
    Función que imprime un mensaje del usuario en color amarillo.
    Cuándo se trata de funciones para manipular el aspecto, es posible permitirles las impresiones internas.
    @param: string      Mensaje del usuario.
    """
    print("\x1b[1;33m" + mensaje) 

def guardar_saludo():
    """
    Función para guardar datos en un archivo de texto.
    Se podrìa mejorar cambiando como un parámetro el nombre del archivo
    y el saludo o contenido.
    """
    f = open ('saludo.txt','w')
    f.write('Hola ADSO. \n')
    f.write('¿Cómo están?.')
    f.close()

    
def guardar_archivo_html():
    """
    Función para guardar datos en un archivo de html.
    https://programminghistorian.org/es/lecciones/trabajar-con-archivos-de-texto
    """
    f = open ('sistema.html','w')
    f.write('<div style=\"border: solid 1px;\">hola mundo</div>')
    f.close()
    
def guardar_archivo_html_v2(saludo):
    """
    Función en versión 2 para guardar datos en un archivo de html.
    @param: string      Texto del usuario para guardar.
    """
    
    texto_css = " border: solid 1px; ";
    texto_css += " color: red; ";
    texto_css += " background-color: yellow; ";
    
    f = open ('sistema.html','w')
    f.write(' <div style=\" ' + texto_css + ' \"> ' + saludo + ' </div> ')
    f.close()
    
def leer_archivo():
    """
    Lee un archivo de texto y lo muesra por pantalla.
    """
    f = open ('sistema.html','r')
    mensaje = f.read()
    print(mensaje)
    f.close()

def presentacion():
    """
    Muestra un mensaje, detiene por tres segundos la ejecución, y luego continúa.
    https://realpython.com/python-sleep/
    """
    print("Hola a todos, demostrativo básico de funciones Python.")
    time.sleep(3)

#--------------------- Ejecución y lamado de funciones ---------------
#print("Inicio de programa.")
#print( "Es número:", es_numero( "hola hola" ) )
#print( "Es número:", es_numero( "35" ) )
#imprimir_color_amarillo("Hola")
#guardar_saludo()
#guardar_archivo()
guardar_archivo_html_v2( input( "Digita un texto." ) )
leer_archivo()
#presentacion()
