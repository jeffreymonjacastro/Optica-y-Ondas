from funciones import *
import numpy as np
import matplotlib.pyplot as plt
from math import *

data = read("datos.txt")
imagen = []

for x in range(600):
    imagen.append([])
    for y in range(600):
        f = frecuencia(1 if y == 0 else y)
        dibujar = x == round(f)
        imagen[x].append([0, 0, 0] if dibujar else [255, 255, 255])
        pass
    pass

imagen.reverse()

imagen = np.array(imagen)

plt.imshow(imagen)

plt.show()
