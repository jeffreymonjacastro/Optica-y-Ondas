from funciones import *
import math

def leySnell(x, A, B):
    return A*x + B


def graficadora_refraccion(data):
    p_x = []
    p_y = []

    # Ingresando los datos del archivo de texto
    for i in range(1, len(data)):
        p_x.append(math.sin(math.pi/180*float(data[i][0])))
        p_y.append(math.sin(math.pi/180*float(data[i][1])))

    x = np.array(p_x)
    y = np.array(p_y)

    resultado, covarianza = curve_fit(leySnell,x,y)

    # Datos dispersos
    plt.scatter(p_x, p_y, color="black", label="Datos")
    plt.xlabel("sin( Angulo_incidente° )")
    plt.ylabel("sin( Angulo_refractado° )")

    #Recolectando los valores del eje x
    x0 = np.linspace(min(x), max(x), 1000)


    plt.title("Grafica de angulos de refraccion (Parte 1)")
    plt.plot(x0, leySnell(x0,resultado[0], resultado[1]), color="r", label="Ajuste")

    plt.legend()
    plt.show()

    return resultado[0], resultado[1]


# Leer datos desde el archivo creado
refraccion2_datos = read("refraccion2_data.txt")


print("Caso 2:")
print("="*20)
print()

# Imprimiendo los datos del archivo creado
print(tabulacion(refraccion2_datos))

pend, indep = graficadora_refraccion(refraccion2_datos)

print(f"La función es: y = {pend}x + {indep}")

print(f"El índice de refracción del medio es: {pend}")