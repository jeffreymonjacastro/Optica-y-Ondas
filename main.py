from funciones import *
import numpy as np
import matplotlib.pyplot as plt
from math import *
import imageio

data = read("datos.txt")
imagen = []
grosor = 2
escala_y = 400

for y in range(600):
	imagen.append([])
	for x in range(1200):
		imagen[y].append([255,255,255])
		if y < round(escala_y*frecuencia(x-grosor)+grosor):
			imagen[y][x] = [0,0,0]
		pass
		if y < round(escala_y*frecuencia(x+grosor)-grosor):
			imagen[y][x] = [255,255,255]
		pass
		if ((x>=-grosor and x <= grosor) and y>=round(escala_y*frecuencia(x-grosor))):
			imagen[y][x] = [0,0,0]
		pass

	pass

print(tabulacion(data))

print(frecuencia(float(data[1][0])*1000))


for x in range(len(data)-1):
	dibujar_Punto(int(escala_y*frecuencia(float(data[x+1][0])*1000)),int(float(data[x+1][0])*1000), imagen, grosor*4, [255,0,0])
	pass

imagen.reverse()

imagen = np.array(imagen)

plt.imshow(imagen)
plt.show()


guardar_imagen("imagen.png", imagen)