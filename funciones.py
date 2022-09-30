import numpy as np
import math
import imageio

def tabulacion(base_datos, esp=2):

    # Definimos listas para añadir la cantidad de caracteres de
    # todos los elementos y de cada columna
    lis_max = [esp for x in range(len(base_datos[0]))]
    for x in range(len(base_datos)):
      for i in range(len(base_datos[0])):
        if len(base_datos[x][i]) >= lis_max[i]-esp:
          lis_max[i] = len(base_datos[x][i])+esp

    # Ahora automatizamos hacer la cadena de .format

    tabulador = ""
    for fil in range(len(base_datos)):
        for colu in range(len(lis_max)):
            tabulador += ("{:<" + str(lis_max[colu]) + "} ").format(base_datos[fil][colu])
        tabulador += ("\n" if fil != 0 else "\n" + ((len(tabulador) - 3) * "-") + "\n")
    pass

  
    # Por ultimo reemplazamos los datos para que sea tabulado
    return tabulador
pass

def read(nombre):
  with open(nombre, "r") as document:
    data = document.read().split("\n");
    for x in range(len(data)):
      data[x] = data[x].split(";")
      pass
  return data


def frecuencia(m):
  if m==0:
    return frecuencia(m+1)
  f = np.sqrt(abs(500/m))/(2*np.pi)
  return (f)



def dibujar_Punto(x, y, matriz, grosor, color):
  for i in range(2*grosor+1):
    for j in range(2*grosor+1):
      matriz[x-grosor+i][y-grosor+j] = color;
      pass
    pass
  pass

def guardar_imagen(ruta, lista_3d):
    """
    La función guardar_imagen recibe una lista de 3
    dimensiones con el mapa de bits de la imagen
    y retorna la imagen en formato Dbmp.

    """
    return imageio.imwrite(ruta, np.array(lista_3d, dtype='uint8'))
pass