from funciones import *

# Leer datos desde el archivo creado
data = read("datos.txt")

# Imprimiendo los datos del archivo creado
print(tabulacion(data))

# Ajuste de la gráfica
print("Los parámetros del ajuste fueron:")
print("Eje x: Masa (kg)")
print("Eje y: Frecuencia (Hz)")
print()
print("El tipo de ajuste utilizado corresponde a la función de la frecuencia:")
print("frecuencia = w/2*pi")
print("Siendo la frecuencia angular (w) = La raíz cuadrada de la constante de resorte (k) sobre masas del oscilador (m)")
print("Resultando --> f(m) = sqrt(k)/(2*pi*sqrt(m))")


# Mostrando la gráfica y descargando la imagen
scatter(data)
