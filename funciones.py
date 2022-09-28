import numpy as np
import math
def read(nombre):
  with open(nombre, "r") as document:
    data = document.readlines();
    for x in data:
      x = x.split(";")
      pass
  return data


def frecuencia(m):
  f = np.sqrt(500/m)/(2*np.pi)
  return f