from funciones import *
import math

def leySnell(x, n1, n2):
    return (n1*x/n2);


def graficadora_refraccion1(data):
    p_x = [];
    p_y = [];

    # Ingresando los datos del archivo de texto
    for i in range(1, len(data)):
        p_x.append(math.sin(float(data[i][0])));
        p_y.append(math.sin(float(data[i][1])));

    x = np.array(p_x);
    y = np.array(p_y);

    res, cov = curve_fit(leySnell,x,y);

    print(res);
    print(cov);

# Leer datos desde el archivo creado
refraccion1_datos = read("refraccion1_data.txt")


print("Caso 1:")
print("="*20)
print()

# Imprimiendo los datos del archivo creado
print(tabulacion(refraccion1_datos))

graficadora_refraccion1(refraccion1_datos);

