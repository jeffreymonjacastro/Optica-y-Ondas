from funciones import *
import math

print("Item 1:")
print("="*20)
print()

data = read("imagenes_data.txt")

print("Primera tabla - recolección de datos")
print(tabulacion(data))

print()

altura_objeto = 4.2
print(f"Altura del objeto: {altura_objeto} cm")

print()

distancia_objeto = []
distancia_imagen = []
tamanio_imagen = []

# Ingresando los datos del archivo de texto
for i in range(1, len(data)):
    distancia_objeto.append(float(data[i][0]))
    distancia_imagen.append(float(data[i][1]))
    tamanio_imagen.append(float(data[i][2]))

amplificacion_alturas = []
amplificacion_distancias = []

for i in range(len(distancia_objeto)):
    amplificacion_alturas.append(tamanio_imagen[i]/altura_objeto)
    amplificacion_distancias.append(distancia_imagen[i]/distancia_objeto[i])

variacion_amplificador = []

for i in range(len(distancia_objeto)):
    variacion_amplificador.append(abs((amplificacion_alturas[i] - amplificacion_distancias[i])/amplificacion_distancias[i])*100)

data[0].append("m = y'/y")
data[0].append("m = s'/s")
data[0].append("Diferencia (%)")


for i in range(1, len(data)):
    data[i].append(round(amplificacion_alturas[i-1],2))
    data[i].append(round(amplificacion_distancias[i-1],2))
    data[i].append(str(round(variacion_amplificador[i-1],2)) + "%")


print()

print("Segunda tabla - Amplificación de la imagen")
print(tabulacion(data))
print()

print(f"Promedio de las diferencias: {round(sum(variacion_amplificador)/len(variacion_amplificador),2)}%")

print()

# Guaardando la tabla
tabla_imagenes = open("tabla_imagenes.txt", 'w')

for i in range(len(data)):
    datos = []

    for j in range(len(data[0])):
        datos.append(str(data[i][j]))

    cadena = ";".join(datos)

    tabla_imagenes.write(cadena + "\n")

tabla_imagenes.close()


print("Item 2 y 3:")
print("="*20)
print()

# 1/s + 1/s' = 1/f
# 1/s = 1/f - 1/s'

def funcionObjetoImagen(x, A, B):
    return A*x + B

def graficadoraDistanciaImagen(data):
    p_x = []
    p_y = []

    # Ingresando los datos del archivo de texto
    for i in range(1, len(data)):
        p_y.append(1/float(data[i][0]))
        p_x.append(1/float(data[i][1]))

    # Guardando los datos en numpy arrays
    x = np.array(p_x)
    y = np.array(p_y)

    # Hallando el resultado (res)
    resultado, covarianza = curve_fit(funcionObjetoImagen,x,y)

    # Datos dispersos
    plt.scatter(p_x, p_y, color="black", label="Datos")
    plt.xlabel("1/s'")
    plt.ylabel("1/s")

    #Recolectando los valores del eje x
    x0 = np.linspace(min(x), max(x), 1000)

    plt.title("Grafica de distancia Objeto-Imagen")
    plt.plot(x0, funcionObjetoImagen(x0, resultado[0], resultado[1]), color="g", label="Ajuste")

    plt.legend()
    plt.show()

    return x, y, resultado[0], resultado[1]

# Hallando los resultados
xi, yi, pend, focal = graficadoraDistanciaImagen(data)

print(f"La ecuación del ajuste es: y= {pend}x + {focal}")


# Calculando el R2

def f(x):
    return pend * x + focal

yRaya = sum(yi) / len(yi)
ySombrero = f(xi)

R2 = np.linalg.norm(ySombrero - yRaya, 2) ** 2 / np.linalg.norm(yi - yRaya, 2) ** 2

print(f"R2 = {R2}")

