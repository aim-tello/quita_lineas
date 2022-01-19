# Programa que lee un archivo de texto (file1) y usa las líneas
# de file1 para buscar en otro archivo (file2) y borrarlas si corresponden con
# los patrones de file1
# Andres Cruz acruzt91@gmail.com

import Util as util

# Se buscan ambos archivos
file1 = util.busca_archivo(" que contenga lo que se va a borrar")
file2 = util.busca_archivo(" donde se va a borrar")

# Inicializa las listas
lineas_a_borrar_ordenadas = []
lineas_de_donde_borrar_ordenadas = []

# Lee los archivos  y ordena las listas
print("Abriendo archivos")
with open(file1, "r") as f:
    lineas_a_borrar_ordenadas = util.ordena_archivo(f)

with open(file2, "r") as g:
    lineas_de_donde_borrar_ordenadas = util.ordena_archivo(g)

# Convierte la listas ordenadas en conjuntos para poder hacer la diferencia
print("Convirtiendo en conjuntos")
conjunto_lineas_a_borrar = set(lineas_a_borrar_ordenadas)
conjunto_lineas_de_donde_borrar = set(lineas_de_donde_borrar_ordenadas)

# Hace la diferencia de los dos conjuntos
print("Realizando la diferencia")
diferencia = conjunto_lineas_de_donde_borrar - conjunto_lineas_a_borrar
lista_diferencia = list(diferencia)
lista_diferencia.sort()
# Escribe el resultado a un archivo de salida
# TODO- Hacer que el nombre del archivo sea editable
print("Escribiendo a archivo")
with open('/tmp/output.txt', 'w') as out_file:
    out_file.write("\n".join([str(linea) for linea in lista_diferencia]))
