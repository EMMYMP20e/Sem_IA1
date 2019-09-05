import math
import sympy
import random
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

# Méndez Pérez Emmanuel
# I7039 D04
# Práctica 3
# Desarrollado en Python 2.7


def f(x, y):  # f(x,y) = x*e^(-x^2-y^2)
    return x*math.pow(math.e, -1*math.pow(x, 2)-(math.pow(y, 2)))


def fdx(x, y):  # fdx(x,y)=(1-2x^2)*e^(-x^2-y^2)
    return (1-2*math.pow(x, 2))*math.pow(math.e, (-1*math.pow(x, 2)-1*(math.pow(y, 2))))


def fdy(x, y):  # fdy(x,y)=-2*x*y*e^(-x^2-y^2)
    return -2*x*y*math.pow(math.e, (-1*math.pow(x, 2)-1*(math.pow(y, 2))))


def f2(x, y):  # f(x,y) = (x-2)^2+(y-2)^2
    return math.pow(x-2, 2)+math.pow(y-2, 2)


def f2dx(x, y):  # f'(x,y) = 2*(x-2)
    return 2*(x-2)


def f2dy(x, y):  # f'(x,y) = 2*(y-2)
    return 2*(y-2)

RANGO=50
# -POBLACION_1 = 10

# Grafica primera función-----------------------------------------

# x,y son arreglos de 50 números en el rango (-2,2)
def grafica1(px,py):
    x = np.linspace(-2, 2, RANGO)
    y = np.linspace(-2, 2, RANGO)

    X, Y = np.meshgrid(x, y)  # Regresa una matriz coordenada de los vectores x,y
    # vectorize Permite que la función f(x) reciba como parámetros los vectores x,y
    Z = np.vectorize(f)
    ax = plt.axes(projection='3d')
    # Dibuja la gráfica de f(x,y)
    ax.contour3D(X, Y, Z(X, Y), RANGO, cmap='binary')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    for i in range(POBLACION_1):
        ax.scatter3D(px[i],py[i],f(px[i],py[i]))
    plt.show()


def inicializacion(xl, xu, poblacion):
    x = np.zeros(poblacion)
    y = np.zeros(poblacion)
    for i in range(poblacion):
        x[i] = xl+(xu-xl)*random.uniform(0, 1)
        y[i] = xl+(xu-xl)*random.uniform(0, 1)
    return x, y


# -X, Y = inicializacion(-2, 2, POBLACION_1)
# Aptitud------------------------------------------------
def aptitudF1():
    for i in range(POBLACION_1):
        fxi = f(X[i], Y[i])
        if fxi >= 0:
            apt[i] = 1/(1+fxi)
        else:
            apt[i] = 1+math.fabs(fxi)

# -aptitudF1()
# Seleccion----------------------------------------------


def seleccionF1():
    aptTotal = 0
    for i in range(POBLACION_1):
        aptTotal += apt[i]
    pi = np.zeros(POBLACION_1)
    for i in range(POBLACION_1):
        pi[i] = apt[i]/aptTotal
    r = random.uniform(0, 1)
    pSum = 0
    for i in range(POBLACION_1):
        pSum = pSum+pi[i]
        if pSum >= r:
            seleccion = i
            return seleccion
    return seleccion


def cruza(poblacion):
    cont = 0
    for i in range(POBLACION_1/2):
        while True:
            select1 = seleccionF1()
            select2 = seleccionF1()
            if select1 != select2:
                break
        padre1 = [X[select1], Y[select1]]
        padre2 = [X[select2], Y[select2]]
        pc = random.randint(1, 2)
        #print 'pc= ',pc
        if pc == 1:
            X[cont] = padre1[0]
            Y[cont] = padre2[1]
            cont += 1
            X[cont] = padre2[0]
            Y[cont] = padre1[1]
            cont += 1
        else:
            X[cont] = padre1[0]
            Y[cont] = padre1[1]
            cont += 1
            X[cont] = padre2[0]
            Y[cont] = padre2[1]
            cont += 1


# -cruzaF1()
def mutacion(xl, xu, poblacion):
    pm = 0.01
    for i in range(poblacion):
        ra = random.uniform(0, 1)
        if ra < pm:
            X[i] = xl+(xu-xl)*random.uniform(0, 1)
        ra = random.uniform(0, 1)
        if ra < pm:
            Y[i] = xl+(xu-xl)*random.uniform(0, 1)

# -mutacion(-2,2,POBLACION_1)


POBLACION_1 = 200

X, Y = inicializacion(-2, 2, POBLACION_1)

apt = np.zeros(POBLACION_1)
for i in range(100):
    print i
    
    aptitudF1()
    '''print 'antes'
    for i in range(POBLACION_1):
        print X[i],Y[i]'''
    cruza(POBLACION_1)
    '''print 'despues'
    for i in range(POBLACION_1):
        print X[i],Y[i]'''
    mutacion(-2, 2, POBLACION_1)
    if(i%20==0):
        grafica1(X,Y)
grafica1(X,Y)
  # Muestra gráfica
