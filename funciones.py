import numpy as np
import mathplotlib.pyplot as plt



def read(nombre):
  with open(nombre, "r") as document:
    data = document.readlines();
    for x in data:
      x = x.split(";")
      pass
  return data


def f(n):
    if n == 0:
        return 15
    f = np.sqrt(500 / n) / (2 * np.pi)
    return f


def scatter(data):
    X = []
    Y = []

    for i in range(1, len(data)):
      X.append(float(data[i][0]))
      Y.append(float(data[i][2]))

    # Ajuste
    x = np.arange(0.5, 1.01, 0.1)
    y = [f(i) for i in x]
    plt.plot(x, y, color="b")

    # Datos dispersos
    plt.scatter(X, Y, color="black")
    plt.title("Frecuencia vs masa")
    plt.xlabel("Masa")
    plt.ylabel("Frecuencia")

    # Guardar la gráfica
    plt.savefig("grafica.png")
    plt.show()


scatter(data)