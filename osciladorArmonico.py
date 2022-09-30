from funciones import *

"""
Experimento (8 puntos)
  1. Ejecute el archivo osciladorArmonico.py.
  2. Ingrese un número entero entre 500 y 1000 y presione “Enter”. El número ingresado será la masa, en gramos, del oscilador armónico.
  3. Anote la frecuencia a la que oscila el sistema a 2 decimales.
  4. Repetir los pasos del 1 al 3 para 10 diferentes valores de masa. Todos los valores deben ser distintos y deben diferir entre ellos en por lo menos 10 gramos.
  5. Guarde sus datos en un archivo de texto.
  6. Elabore un programa que:0
    a. Lea el archivo de texto generado en el paso 5. 
    b. Grafique la frecuencia de oscilación del sistema vs la masa del oscilador armónico.
    c. Aplique un ajuste. El tipo de ajuste utilizado queda a su criterio y será parte de la evaluación.
    d. Imprima en la línea de comandos los parámetros del ajuste y el tipo de ajuste utilizado. (THIS)
    e. Guarde el gráfico en formato png con un nombre descriptivo de forma automática (su código debe realizar este paso).
"""


# PLANTILLA
data = [["masa(kg)", "w", "Frecuencia(Hz)"]]

for x in range(int(input("Cuantos datos va a ingresar: "))):
    # Definir Constantes
    k = 500

    # Pedir valor de masa (en gramos) para tensar la cuerda
    mGramos = input("\nIngrese un valor entero entre 500 y 1000: ")
    m = float(mGramos)/1000

    # Calcular los parametros del oscilador
    w = np.sqrt(k/m)
    f = w/(2*np.pi)

    w = round(w,2)
    f = round(f,2)

    data.append([str(m),str(w),str(f)]);
    print("La frecuencia de oscilación del sistema es: ", f)
    print()

    pass

#Escribir datos
with open("datos.txt", "w") as dataFile:
    for x in data:
        for y in x:
            dataFile.write(y+(";"if y != x[len(x)-1] else ""))
            pass
        dataFile.write("\n"if x!=data[len(data)-1] else "")
    pass

print("Datos guardados con exito!\n")
print(tabulacion(data))

# Mostrando la gráfica y descargando la imagen
scatter(data)

# El ajuste utilizado fue:
