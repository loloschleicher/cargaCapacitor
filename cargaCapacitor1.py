


import json 
import math
import matplotlib.pyplot as plt
#Cargar datos desde json
with open("datos.json", "r") as datos:
    valores = json.load(datos)
datos.close()

# Ejercicio 1 
#cantidad de valores
n = len(valores)
#sumatoria en x
sumX = 0.0
#sumatoria en y
sumY = 0.0
#sumatoria de x*y
sumXY = 0.0
#sumatoria de x^2
sumX2 = 0.0

# hallar sumatorias
for x, y in valores.items():
    sumX = sumX + float(x)
    sumY = sumY + float(y)
    sumXY = sumXY + (float(x) * float(y))
    sumX2 = sumX2 + math.pow(sumX, 2)

# calcular ajuste por minimos cuadrados
#chapra 17.1.2 fig 17.6 pag 470
a1 = ( (n* sumXY) - (sumX * sumY) ) / ((n * sumX2) - math.pow(sumX, 2) )

# chapra 17.1.2 fig 17.7 pag 470
a0 = ( sumY / n ) - ( a1 * ( sumX / n ) )

print("\n\nEjercicio 1:")
print("valor del coeficiente a0: ", a0)
print("valor del coeficiente a1: ", a1)


    
#convertir dict a list
valoresX = []
valoresY = []

#convertir string a float
for x, y in valores.items():
    valoresX.append(float(x))
    valoresY.append(float(y))
    
def graficaPreliminar():
    print("\n \nEjercicio2: \nGrafica Preliminar De Los Datos")
    plt.plot(valoresX, valoresY, ".")
    plt.axis([0, max(valoresX), 0, max(valoresY)])
    plt.show()
# plot valores experimentales


def valorIncognitas():
    print("\n\nValores de las incognitas y errores \nTiempo           ValorReal           ValorTeorico                Error")

    for i in range(len(valoresX)):
        yModelo = 0.8080754572468457*valoresX[i] + 3.3621494232662332
        error = valoresY[i] - yModelo
        print (str(valoresX[i]) + "         " + str(valoresY[i]) + "        " + str(yModelo) + "        " + str(error))


#ejercicio 3
def graficaSuperpuesta():
    print("\n\nEjercicio 3: \nGrafica De Los Datos Experimentales y de los valores Obtenidos por la ecuacion linealizada")
    arrayYmodelo = []
    for i in range(len(valoresX)):
        yModelo = 0.8080754572468457*valoresX[i] + 3.3621494232662332     
        arrayYmodelo.append(yModelo)
    
    plt.plot(valoresX,arrayYmodelo, '-')
    
    plt.plot(valoresX, valoresY, ".")
    plt.axis([0, max(valoresX), 0, max(valoresY)])
    plt.show()
    
#Ejercicio 4
def interpolacionLineal():
    print("\n\nEjercicio 4:\nInterpolacion lineal de Newton")
    R = 12000
    C = 0.00022
    x = R * C
    xCero = 2.6262626e+00
    xUno = 2.7272727e+00
    fXcero = 6.1825397e+00
    fXUno = 6.4982541e+00
    fX = fXcero + ((fXUno - fXcero) / (xUno - xCero)) * (x - xCero)
    print("Valor del parametro incognita: " + str(fX))

graficaPreliminar()
valorIncognitas()
graficaSuperpuesta()
interpolacionLineal()
