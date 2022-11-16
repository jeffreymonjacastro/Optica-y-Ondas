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
    print("Indice de refraccion del cristal en forma de D: " + str(round(res[0],2)))

    # Datos dispersos
    plt.scatter(p_x, p_y, color="black", label="Datos");
    plt.xlabel("sin( Angulo_incidente° )");
    plt.ylabel("sin( Angulo_refractado° )");

    #Recolectando los valores del eje x
    x0 = np.linspace(min(x), max(x), 1000)

    # Ploteando la curva de ajuste
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
print()

# Resultados
print("La ecuación de la curva de ajuste parte de la Ley de Snell: sen(θr) = (n1*sen(θi))/n2")
print("Resultando: y = 1.00029*x/n2")
print("- x se refiere al sen(θi)\n- y se refiere al sen(θr)\n- n2 se refiere al índice de refracción del cristal")
print()

print("Comparación:")
print("La ecuación de la curva de ajuste encaja muy aproximadamente a los datos obtenidos en el laboratorio. Además, tiene coherencia con la teoría, ya que según la Ley de Snell...")
print()

# Graficando la primera refraccion
graficadora_refraccion(refraccion1_datos)