import numpy as np
import math
import matplotlib.pyplot as plt

dataX = np.loadtxt('datos.dat')
dataY = np.loadtxt('y.dat')

def valoresCoeficientes(dataX, dataY):
    nX = len(dataX)
    nY = len(dataY)
    XiporYi = np.multiply(dataX,dataY)
    sumaXiporYi = np.sum(XiporYi)
    sumaXi = np.sum(dataX)
    sumaYi = np.sum(dataY)
    cuadradoSumaXi = sumaXi * sumaXi
    sumaXiCuadrado = 0
    i = 0
    for i in range(len(dataX)):
         sumaXiCuadrado += dataX[i] * dataX[i]
    yPromedio = sumaYi / nY
    xPromedio = sumaXi / nX
    aUno = ((nX * sumaXiporYi) - (sumaXi * sumaYi)) / ((nX * sumaXiCuadrado) - (cuadradoSumaXi))
    aCero = yPromedio - (aUno*xPromedio)
    return aUno,aCero

def graficaPreliminar():
    plt.plot(dataX,dataY, '.')
    plt.show()


print(valoresCoeficientes(dataX, dataY))
graficaPreliminar()