from funciones import *
import math

def leySnell(x, n2):
    return (1.00029*x/n2); #indice de refraccioin del aire (1.00029)


def graficadora_refraccion(data):
    p_x = [];
    p_y = [];

    # Ingresando los datos del archivo de texto
    for i in range(1, len(data)):
        p_x.append(math.sin(math.pi/180*float(data[i][0])));
        p_y.append(math.sin(math.pi/180*float(data[i][1])));

    # Guardando los datos en numpy arrays
    x = np.array(p_x);
    y = np.array(p_y);

    # Hallando el resultado (res) de n2 que mejor se ajusta con los datos
    res, cov = curve_fit(leySnell,x,y);

    # Calculando el índice de refracción del material
    print("Indice de refraccion del cristal en forma de D: " + str(res[0]));

    # Datos dispersos
    plt.scatter(p_x, p_y, color="black", label="Datos");
    plt.xlabel("sin( Angulo_incidente° )");
    plt.ylabel("sin( Angulo_refractado° )");

    #Recolectando los valores del eje x
    x0 = np.linspace(min(x), max(x), 1000)

    plt.title("Grafica de angulos de refraccion (Parte 1)")
    plt.plot(x0, leySnell(x0,res[0]), color="r", label="Ajuste")

    plt.legend()
    plt.show()


print("Caso 1:")
print("="*20)
print()

# Leer datos desde el archivo creado
refraccion1_datos = read("refraccion1_data.txt")

# Imprimiendo los datos del archivo creado
print(tabulacion(refraccion1_datos))

# Graficando la primera refraccion
graficadora_refraccion(refraccion1_datos);


print("Caso 2:")
print("="*20)
print()

# Leer datos desde el archivo creado
refraccion2_datos = read("refraccion2_data.txt")

# Imprimiendo los datos del archivo creado
print(tabulacion(refraccion2_datos))

# Graficando la primera refraccion
graficadora_refraccion(refraccion2_datos);