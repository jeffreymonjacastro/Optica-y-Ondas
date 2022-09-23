import numpy as np

# Definir Constantes
k = 500

# Pedir valor de masa (en gramos) para tensar la cuerda
mGramos = input("Ingrese un valor entero entre 500 y 1000: ")
m = int(mGramos) * (10 ** (-3))

# Calcular los parametros del oscilador
w = np.sqrt(k/m)
f = w/(2*np.pi)

print("La frecuencia de oscilación del sistema es: ", f)
