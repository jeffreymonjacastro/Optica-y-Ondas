from funciones import *


def graficadora_refraccion1(data, type):
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
        p_x.append(1/((float(data[i][0]))**2))
        p_y.append(float(data[i][1]))

    elif type == "cuadratica":
        for i in range(1, len(data)):
            p_x.append(float(data[i][0]))
            p_y.append(float(data[i][1]))

    x = np.array(p_x)
    y = np.array(p_y)

    # Buscando la curva de ajuste
    if type == "lineal":
        res, cov = curve_fit(cauchy_lineal,x,y)

    elif type == "cuadratica":
        res, cov = curve_fit(cauchy_cuadratica,x,y)

    # Datos dispersos
    plt.scatter(p_x, p_y, color="black", label="Datos")
    plt.xlabel("Longitud de onda (λ)")
    plt.ylabel("Índice de refracción (n)")

    #Recolectando los valores del eje x
    x0 = np.linspace(min(x), max(x), 100)

    # Ploteando la gráfica de ajuste
    if type == "lineal":
        plt.title("Índice de refracción (n) vs Longitud de onda (λ)")
        plt.plot(x0, cauchy_lineal(x0,res[0],res[1]), color="b", label="Ajuste")

    elif type == "cuadratica":
        plt.title("Índice de refracción (n) vs 1/Longitud de onda (λ)")
        plt.plot(x0, cauchy_cuadratica(x0,res[0],res[1]), color="r", label="Ajuste")

    plt.legend()
    plt.show()

    # Imprimiendo el tipo de ajuste
    if type == "lineal":
        print("El ajuste de la función de Cauchy (n vs λ)")
        print("y =", res[0], " +", res[1], "x")

    elif type == "cuadratica":
        print("El ajuste de la función de Cauchy (n vs 1/λ**2)")
        print("y =", res[0], " +", res[1], "1/x**2")


# Leer datos desde el archivo creado
refraccion1_datos = read("refraccion1_data.txt")


print("Caso 1:")
print("="*20)
print()

# Imprimiendo los datos del archivo creado
print(tabulacion(refraccion1_datos))

