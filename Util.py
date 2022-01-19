# Clase que define las funciones de utilería que se necesitan
# importa tkinter para poder usar filedialog
import tkinter as tk
# importa filedialog para pedir la ruta de los archivos
from tkinter import filedialog
from tkinter import Tk


def busca_archivo(mensaje):
    Tk().withdraw()
    filename = filedialog.askopenfilename(title="Selecciona un archivo" + mensaje,
                                          filetypes=[("Text files",
                                                      "*.txt")])
    return filename


def ordena_archivo(archivo):
    lineas_del_archivo = archivo.read().splitlines()
    lineas_del_archivo.sort()
    return lineas_del_archivo


if __name__ == "__main__":
    archivo = busca_archivo("ejemplo")
    with open(archivo, "r") as f:
        ordenadas = ordena_archivo(f)
        print(len(ordenadas))
