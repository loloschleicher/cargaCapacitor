

def interpolacionLineal():
    R = 12000
    C = 0.00022
    x = R * C
    xCero = 2.6262626e+00
    xUno = 2.7272727e+00
    fXcero = 6.1825397e+00
    fXUno = 6.4982541e+00
    fX = fXcero + ((fXUno - fXcero) / (xUno - xCero)) * (x - xCero)
    return fX

print(interpolacionLineal())