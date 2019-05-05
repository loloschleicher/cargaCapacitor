from colorama import init, Fore, Back, Style
from scipy.interpolate import lagrange
import json 
import math
import matplotlib.pyplot as plt
import numpy as np


#Cargar datos desde json
with open("datos.json", "r") as datos:
    valores = json.load(datos)
datos.close()





#EJERCICIO 1
def valoresCoeficientes():
    print(f"\n\n{Fore.RED}Ejercicio1:{Style.RESET_ALL}")
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
     
    for x, y in valores.items():
        sumX = sumX + float(x)
        sumY = sumY + float(y)
        sumXY = sumXY + (float(x) * float(y))
        sumX2 = sumX2 + math.pow(float(x), 2)

    a1 = ( (n* sumXY) - (sumX * sumY) ) / ((n * sumX2) - math.pow(sumX, 2) )
    a0 = ( sumY / n ) - ( a1 * ( sumX / n ) )
    print("valor del coeficiente a0: ", a0)
    print("valor del coeficiente a1: ", a1)  
    return a0,a1




#EJERCICIO 2
valoresX = []
valoresY = []

for x, y in valores.items():
    valoresX.append(float(x))
    valoresY.append(float(y))
    
def graficaPreliminar():
    print(f"\n \n{Fore.RED}Ejercicio2:{Style.RESET_ALL} \nGrafica Preliminar De Los Datos")
    plt.plot(valoresX, valoresY, ".")
    plt.xlabel("Tiempo")
    plt.ylabel("Voltaje")
    plt.show()

def valorIncognitas(func):
    print("\n\nValores de las incognitas y del error \nTiempo           ValorReal           ValorTeorico ")
    a0, a1 = func()
    Sr = 0
    for i in range(len(valoresX)):
        yModelo = a1*valoresX[i] + a0
        Sr += math.pow(yModelo - a0 - (a1*valoresX[i]), 2)
        print (str(valoresX[i]) + "         " + str(valoresY[i]) + "        " + str(yModelo))
    error = math.sqrt(Sr/(len(valoresY) - 2))
    print("\nEL error es de " + str(error))


   
    
        
#EJERCICIO 3
def graficaSuperpuesta(func):
    print(f"\n\n{Fore.RED}Ejercicio 3:{Style.RESET_ALL} \nGrafica De Los Datos Experimentales y de los valores Obtenidos por la ecuacion linealizada")
    a0, a1 = func()
    arrayYmodelo = []
    for i in range(len(valoresX)):
        yModelo = a1*valoresX[i] + a0     
        arrayYmodelo.append(yModelo)
    
    plt.plot(valoresX,arrayYmodelo, '-', label="Datos teoricos")
    
    plt.plot(valoresX, valoresY, ".", label="Datos reales")
    plt.xlabel("Tiempo")
    plt.ylabel("Voltaje")
    plt.legend()

    plt.show()





#EJERCICIO 4
def interpolacionLineal():
    print(f"\n\n{Fore.RED}Ejercicio 4:{Style.RESET_ALL}\nInterpolacion lineal de Newton")
    R = 12000
    C = 0.00022
    x = R * C
    xCero = 2.6262626e+00
    xUno = 2.7272727e+00
    fXcero = 6.1825397e+00
    fXUno = 6.4982541e+00
    fX = fXcero + ((fXUno - fXcero) / (xUno - xCero)) * (x - xCero)
    print("Valor del parametro incognita: " + str(fX))





#EJERCICIO 5
def ajusteSinCuadradoMin():
    print(f"\n\n{Fore.RED}Ejercicio 5:{Style.RESET_ALL}")
    #plt.plot(valoresX, valoresY, ".")
    #lag_pol = lagrange(valoresX, valoresY)
    #print(lag_pol)

    p = np.polynomial.Chebyshev.fit(valoresX, valoresY, 90)
    
    #x = np.linspace(valoresX[0], valoresX[11])
    plt.plot(valoresX, valoresY, 'r.', label="Datos Experimentales")
    t = np.linspace(0, 10, 10)
    #plt.xlabel("T")
    #plt.ylabel("V")
    #plt.plot(x, lag_pol(x),  "-")
    plt.plot(t, p(t), '-', lw=2, label="Curva adaptada") 
    plt.xlabel("Tiempo")
    plt.ylabel("Voltaje")
    plt.show()
    



valoresCoeficientes()
graficaPreliminar()
valorIncognitas(valoresCoeficientes)
graficaSuperpuesta(valoresCoeficientes)
interpolacionLineal()
ajusteSinCuadradoMin()