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
  if m==0:
    return frecuencia(m+1)
  f = np.sqrt(abs(500/m))/(2*np.pi)
  return (f)

def masa(f):
  if f==0:
    return frecuencia(f+1)
  m = 500/((f*2*np.pi)**2)
  return m