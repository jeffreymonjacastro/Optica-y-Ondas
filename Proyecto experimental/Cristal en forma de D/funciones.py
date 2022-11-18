import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def tabulacion(base_datos, esp=2):
    """
    Función para imprimir la base de datos de las masas y las frecuencias
    """

    # Definimos listas para añadir la cantidad de caracteres de
    # todos los elementos y de cada columna
    lis_max = [esp for x in range(len(base_datos[0]))]

    for i in range(len(base_datos)):
        for j in range(len(base_datos[0])):
            if len(base_datos[i][j]) >= lis_max[j] - esp:
                lis_max[j] = len(base_datos[i][j]) + esp

    # Ahora automatizamos hacer la cadena de .format

    tabulador = ""
    for i in range(len(base_datos)):
        for j in range(len(lis_max)):
            tabulador += ("{:<" + str(lis_max[j]) + "} ").format(base_datos[i][j])
        tabulador += ("\n" if i != 0 else "\n" + ((len(tabulador) - 3) * "-") + "\n")
    pass

    # Por ultimo reemplazamos los datos para que sea tabulado
    return tabulador


def read(nombre):
    """
    Función para leer los datos de un archivo de texto
    """

    with open(nombre, "r") as document:
        data = document.read().split("\n")
        for x in range(len(data)):
            data[x] = data[x].split(";")
            pass
    return data



