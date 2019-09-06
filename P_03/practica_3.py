import math
import sympy
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits import mplot3d

# Méndez Pérez Emmanuel
# I7039 D04
# Práctica 3
# Desarrollado en Python 2.7


def f(x, y):  # f(x,y) = x*e^(-x^2-y^2)
    return x*math.pow(math.e, -1*math.pow(x, 2)-(math.pow(y, 2)))


def f2(x, y):  # f(x,y) = (x-2)^2+(y-2)^2
    return math.pow(x-2, 2)+math.pow(y-2, 2)


RANGO = 50
# -POBLACION = 10

# Grafica primera función-----------------------------------------

# x,y son arreglos de 50 números en el rango (-2,2)


def grafica1(px, py):
    x = np.linspace(-2, 2, RANGO)
    y = np.linspace(-2, 2, RANGO)

    # Regresa una matriz coordenada de los vectores x,y
    X, Y = np.meshgrid(x, y)
    # vectorize Permite que la función f(x) reciba como parámetros los vectores x,y
    Z = np.vectorize(f)
    ax = plt.axes(projection='3d')
    # Dibuja la gráfica de f(x,y)
    ax.contour3D(X, Y, Z(X, Y), RANGO, cmap='binary')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    for i in range(POBLACION):
        ax.scatter3D(px[i], py[i], f(px[i], py[i]))
    plt.show()


def grafica2(px, py):
    x = np.linspace(-2, 6, RANGO)
    y = np.linspace(-2, 6, RANGO)

    # Regresa una matriz coordenada de los vectores x,y
    X, Y = np.meshgrid(x, y)
    # vectorize Permite que la función f(x) reciba como parámetros los vectores x,y
    Z = np.vectorize(f2)
    ax = plt.axes(projection='3d')
    # Dibuja la gráfica de f(x,y)
    ax.contour3D(X, Y, Z(X, Y), RANGO, cmap='binary')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    for i in range(POBLACION):
        ax.scatter3D(px[i], py[i], f2(px[i], py[i]))
    plt.show()


def inicializacion(xl, xu):
    x = np.zeros(POBLACION)
    y = np.zeros(POBLACION)
    for i in range(POBLACION):
        x[i] = xl+(xu-xl)*random.uniform(0, 1)
        y[i] = xl+(xu-xl)*random.uniform(0, 1)
    return x, y


# -X, Y = inicializacion(-2, 2, POBLACION)
# Aptitud------------------------------------------------
def aptitudF1():
    for i in range(POBLACION):
        fxi = f(X[i], Y[i])
        if fxi >= 0:
            apt[i] = 1/(1+fxi)
        else:
            apt[i] = 1+math.fabs(fxi)

# Aptitud------------------------------------------------


def aptitudF2():
    for i in range(POBLACION):
        fxi = f2(X[i], Y[i])
        if fxi >= 0:
            apt[i] = 1/(1+fxi)
        else:
            apt[i] = 1+math.fabs(fxi)

# -aptitudF1()
# Seleccion----------------------------------------------


def seleccion():
    aptTotal = 0
    for i in range(POBLACION):
        aptTotal += apt[i]
    pi = np.zeros(POBLACION)
    for i in range(POBLACION):
        pi[i] = apt[i]/aptTotal
    r = random.uniform(0, 1)
    pSum = 0
    for i in range(POBLACION):
        pSum = pSum+pi[i]
        if pSum >= r:
            seleccion = i
            return seleccion
    return seleccion


def cruza():
    cont = 0
    for i in range(POBLACION/2):
        while True:
            select1 = seleccion()
            select2 = seleccion()
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
def mutacion(xl, xu):
    pm = 0.01
    for i in range(POBLACION):
        ra = random.uniform(0, 1)
        if ra < pm:
            X[i] = xl+(xu-xl)*random.uniform(0, 1)
        ra = random.uniform(0, 1)
        if ra < pm:
            Y[i] = xl+(xu-xl)*random.uniform(0, 1)

# -mutacion(-2,2,POBLACION)


POBLACION = 200


X, Y = inicializacion(-2, 2)

apt = np.zeros(POBLACION)
for i in range(100):
    aptitudF1()
    cruza()
    mutacion(-2, 2)
    #if(i % 20 == 0):
        # grafica1(X,Y)
aptitudF1()
mejor = 0
im = 0
for i in range(POBLACION):
    if apt[i] > mejor:
        mejor = apt[i]
        im = i
print "Mayor aptitud: "
print 'x= ', X[im], 'y= ', Y[im], 'f(x,y)= ', f(X[im], Y[im])

grafica1(X, Y)
# Muestra gráfica

X, Y = inicializacion(-2, 6)

apt = np.zeros(POBLACION)

for i in range(100):
    aptitudF2()
    cruza()
    mutacion(-2,6)
    if(i%20==0):
        grafica2(X,Y)
aptitudF2()
mejor = 0
im = 0
for i in range(POBLACION):
    if apt[i] > mejor:
        mejor = apt[i]
        im = i
print "Mayor aptitud: "
print 'x= ', X[im], 'y= ', Y[im], 'f(x,y)= ', f2(X[im], Y[im])

grafica2(X, Y)