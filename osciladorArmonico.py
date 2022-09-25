import matplotlib
import numpy as np


"""
Experimento (8 puntos)
  1. Ejecute el archivo osciladorArmonico.py.
  2. Ingrese un número entero entre 500 y 1000 y presione “Enter”. El número ingresado será la masa, en gramos, del oscilador armónico.
  3. Anote la frecuencia a la que oscila el sistema a 2 decimales.
  4. Repetir los pasos del 1 al 3 para 10 diferentes valores de masa. Todos los valores deben ser distintos y deben diferir entre ellos en por lo menos 10 gramos.
  5. Guarde sus datos en un archivo de texto.
  6. Elabore un programa que:
    a. Lea el archivo de texto generado en el paso 5. 
    b. Grafique la frecuencia de oscilación del sistema vs la masa del oscilador armónico.
    c. Aplique un ajuste. El tipo de ajuste utilizado queda a su criterio y será parte de la evaluación.
    d. Imprima en la línea de comandos los parámetros del ajuste y el tipo de ajuste utilizado.
    e. Guarde el gráfico en formato png con un nombre descriptivo de forma automática (su código debe realizar este paso).
"""

def tabulacion(base_datos, esp=2):

    # Definimos listas para añadir la cantidad de caracteres de
    # todos los elementos y de cada columna
    lis_max = [esp for x in range(len(base_datos[0]))]
    for x in range(len(base_datos)):
      for i in range(len(base_datos[x])):
        if len(base_datos[x][i]) > lis_max[i]-esp:
          lis_max[i] = len(base_datos[x][i])+esp

    # Ahora automatizamos hacer la cadena de .format

    tabulador = ""
    for fil in range(len(base_datos)):
        for colu in range(len(lis_max)):
            tabulador += ("{:<" + str(lis_max[colu]) + "} ").format(
                base_datos[fil][colu])
        tabulador += ("\n" if fil != 0 else "\n" + ((len(tabulador) - 3) * "-") + "\n")
    pass

  
    # Por ultimo reemplazamos los datos para que sea tabulado
    return tabulador
pass


data = [["masa(kg)", "w", "Frecuencia(Hz)"]]

for x in range(int(input("Cuantos datos va a ingresar: "))):

  # Definir Constantes
  k = 500

  # Pedir valor de masa (en gramos) para tensar la cuerda
  mGramos = input("\nIngrese un valor entero entre 500 y 1000: ")
  m = int(mGramos) * (10 ** (-3))

  # Calcular los parametros del oscilador
  w = np.sqrt(k/m)
  f = w/(2*np.pi)

  data.append([str(m),str(w),str(f)]);
  print("La frecuencia de oscilación del sistema es: ", f)
  print()

  pass

#Escribir datos

with open("datos.txt", "w") as dataFile:
  for x in data:
    for y in x:
      dataFile.write(y+";")
      pass
    dataFile.write("\n")
    pass

print("Datos guardados con exito!\n")
print(tabulacion(data))