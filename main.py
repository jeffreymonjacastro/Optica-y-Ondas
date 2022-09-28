from funciones import *
import numpy as np
import matplotlib.pyplot as plt
from math import *

data = read("datos.txt")
imagen = []
grosor = 1
escala = 400

for y in range(600):
	imagen.append([])
	for x in range(1200):
		imagen[y].append([255,255,255])
		if y < round(escala*frecuencia(x-grosor)+grosor):
			imagen[y][x] = [0,0,0]
		pass
		if y < round(escala*frecuencia(x+grosor)-grosor):
			imagen[y][x] = [255,255,255]
		pass
		if ((x>=-grosor and x <= grosor) and y>=round(escala*frecuencia(x-grosor))):
			imagen[y][x] = [0,0,0]
		pass

	pass


imagen.reverse()

imagen = np.array(imagen)

plt.imshow(imagen)
plt.show()
