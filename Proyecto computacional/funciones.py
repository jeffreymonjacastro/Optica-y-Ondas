import numpy as np
import matplotlib.pyplot as plt


def tabulacion(base_datos, esp=2):
    """
    Función para imprimir la base de datos de las masas y las frecuencias
    """

    # Definimos listas para añadir la cantidad de caracteres de
    # todos los elementos y de cada columna
    lis_max = [esp for x in range(len(base_datos[0]))]
    for x in range(len(base_datos)):
        for i in range(len(base_datos[0])):
            if len(base_datos[x][i]) >= lis_max[i] - esp:
                lis_max[i] = len(base_datos[x][i]) + esp

    # Ahora automatizamos hacer la cadena de .format

    tabulador = ""
    for fil in range(len(base_datos)):
        for colu in range(len(lis_max)):
            tabulador += ("{:<" + str(lis_max[colu]) + "} ").format(base_datos[fil][colu])
        tabulador += ("\n" if fil != 0 else "\n" + ((len(tabulador) - 3) * "-") + "\n")
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


def obtener_k(m, f):
    # Supuestamente
    sum_k = 0
    for i in range(10):
        sum_k += 4*m[i]*(np.pi**2)*(f[i]**2)

    k = sum_k/10
    return k


def f(m, k):
    """
    Función frecuencia sqrt(k/m)/2*pi
    """

    if m == 0:
        return 15


    func = np.sqrt(k / m) / (2 * np.pi)
    return func


def scatter(data):
    """
    Función para plotear la gráfica frecuencia vs masa
    Extrae los datos de la masa y la frecuencia y los plotea con matplotlib
    Establece la recta de ajuste f(m) - Función f(m)
    Guarda la gráfica con el nombre "gráfica.png"
    """

    p_x = []
    p_y = []

    # Ingresando los datos del archivo de texto
    for i in range(1, len(data)):
        p_x.append(float(data[i][0]))
        p_y.append(float(data[i][2]))

    # Función de ajuste
    sum_k = obtener_k(p_x, p_y)



    print(sum_k)

    #Recolectando los valores del eje x
    x = np.arange(min(p_x), max(p_x)+0.1, 0.001)

    # Recolectandos los valores del eje y
    y = [f(i, sum_k) for i in x]


    # print()
    # for i in range(10):
    #     print(f(p_x[i],sum_k))
    #
    # Ploteando la gráfica de ajuste
    plt.plot(x, y, color="b", label="Ajuste")

    # Datos dispersos
    plt.scatter(p_x, p_y, color="black", label="Datos")
    plt.title("Frecuencia vs masa")
    plt.xlabel("Masa (kg)")
    plt.ylabel("Frecuencia (Hz)")
    plt.legend()

    # Guardar la gráfica
    plt.savefig("grafica de frecuenia vs masa.png")
    plt.show()
