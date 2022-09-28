def read(nombre):
  with open(nombre, "r") as document:
    data = document.readlines();
    for x in data:
      x = x.split(";")
      pass
  return data

# HELOOOOOOOOOOOOO

print(read("datos.txt"))
