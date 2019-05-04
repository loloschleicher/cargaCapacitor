
# Ejercicio 2

import json
import matplotlib.pyplot as plt

# Cargar datos desde json
with open("datos.json", "r") as datos:
    valores = json.load(datos)
datos.close()

#convertir dict a list
valoresX = []
valoresY = []

#convertir string a float
for x, y in valores.items():
    valoresX.append(float(x))
    valoresY.append(float(y))

# plot valores experimentales
plt.plot(valoresX, valoresY, ".")
plt.axis([0, max(valoresX), 0, max(valoresY)])
plt.show()


def valorIncognitas():

    for i in range(len(valoresX)):
        yModelo = 0.8080754572468457*valoresX[i] + 3.3621494232662332
        print("valor: " + str(yModelo))
        error = valoresY[i] - yModelo
        print("error: " + str(error) + "\n")

def grafica():
    arrayYmodelo = []
    for i in range(len(valoresX)):
        yModelo = 0.8080754572468457*valoresX[i] + 3.3621494232662332     
        arrayYmodelo.append(yModelo)
    
    plt.plot(valoresX,arrayYmodelo, '-')
    
    plt.plot(valoresX, valoresY, ".")
    plt.axis([0, max(valoresX), 0, max(valoresY)])
    plt.show()

valorIncognitas()
grafica()