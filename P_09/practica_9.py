import math
import sympy
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits import mplot3d

# Méndez Pérez Emmanuel
# I7039 D04
# Práctica 9
# Desarrollado en Python 2.7


def f1(x, y):  # Griewank function
    sum = 0
    prod = 1
    xi = x
    sum = sum+((math.pow(xi, 2))/4000)
    prod = prod*math.cos((xi/math.sqrt(1)))
    xi = y
    sum = sum+((math.pow(xi, 2))/4000)
    prod = prod*math.cos((xi/math.sqrt(2)))
    r = sum-prod+1
    return r


def f2(x, y):  # Sphere function
    sum = 0
    xi = x
    sum = sum + math.pow(xi, 2)
    xi = y
    sum = sum + math.pow(xi, 2)
    return sum


def f3(x, y):  # Rastrigin Function
    sum = 0
    xi = x
    sum = sum + (math.pow(xi, D) - 10*math.cos(2*math.pi*xi))
    xi = y
    sum = sum + (math.pow(xi, 2) - 10*math.cos(2*math.pi*xi))
    r = 10*D + sum
    return r


def f(num, x, y):
    if num == 1:
        return f1(x, y)
    elif num == 2:
        return f2(x, y)
    else:
        return f3(x, y)


def grafica1(vX):
    # a,b son arreglos de 50 números en el rango (-2,2)
    a = np.linspace(-10, 10, RANGO)
    b = np.linspace(-10, 10, RANGO)
    #x=np.zeros((2, RANGO))

    x, y = np.meshgrid(a, b)
    # vectorize Permite que la función f(x,y) reciba como parámetros los vectores x,y
    Z = np.vectorize(f1)
    ax = plt.axes(projection='3d')
    # Dibuja la gráfica de f(x,y)
    ax.contour3D(x, y, Z(x, y), 20, cmap='binary')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    for i in range(POBLACION):
        # Dibuja la población en la gráfica
        ax.scatter3D(vX[0, i], vX[1, i], f1(vX[0, i], vX[1, i]))
    plt.show()


def grafica2(vX):
    # a,b son arreglos de 50 números en el rango (-2,2)
    a = np.linspace(-10, 10, RANGO)
    b = np.linspace(-10, 10, RANGO)
    #x=np.zeros((2, RANGO))

    x, y = np.meshgrid(a, b)
    # vectorize Permite que la función f(x,y) reciba como parámetros los vectores x,y
    Z = np.vectorize(f2)
    ax = plt.axes(projection='3d')
    # Dibuja la gráfica de f(x,y)
    ax.contour3D(x, y, Z(x, y), 30, cmap='binary')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    for i in range(POBLACION):
        # Dibuja la población en la gráfica
        ax.scatter3D(vX[0, i], vX[1, i], f2(vX[0, i], vX[1, i]))
    plt.show()


def grafica3(vX):
    # a,b son arreglos de 50 números en el rango (-2,2)
    a = np.linspace(-10, 10, RANGO)
    b = np.linspace(-10, 10, RANGO)
    #x=np.zeros((2, RANGO))

    x, y = np.meshgrid(a, b)
    # vectorize Permite que la función f(x,y) reciba como parámetros los vectores x,y
    Z = np.vectorize(f3)
    ax = plt.axes(projection='3d')
    # Dibuja la gráfica de f(x,y)
    ax.contour3D(x, y, Z(x, y), 30, cmap='binary')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    for i in range(POBLACION):
        # Dibuja la población en la gráfica
        ax.scatter3D(vX[0, i], vX[1, i], f3(vX[0, i], vX[1, i]))
    plt.show()


def grafica(num, vX):
    if num == 1:
        grafica1(vX)
    elif num == 2:
        grafica2(vX)
    else:
        grafica3(vX)


RANGO = 50
D = 2


POBLACION = 50
GENERACIONES = 150

X = np.zeros((2, POBLACION))  # Individuos (flores)

xl = np.array([-10, -10])  # límite inferior
xu = np.array([10, 10])  # Límite superior

LAMBDA = 1.5  # Parámetro de ajueste del paso

SIGMA2 = 0.6966  # Varianza

p = 0.8  # Probabilidad de polinización global y local


def rand():  # Genera vector de números random
    return random.uniform(0, 1), random.uniform(0, 1)


def mejorPosicion(num):  # Encuentra individuo con mejor posición
    best = 0
    for i in range(POBLACION):
        if f(num, X[0, i], X[1, i]) < f(num, X[0, best], X[1, best]):
            best = i
    return best


def inicializa():
    for i in range(POBLACION):
        X[:, i] = xl+(xu-xl)*rand()  # Inicializa flores aleatoriamente


def VueloDeLevy():
    u = np.random.normal(0, SIGMA2)  # u~N(0,sigma2)
    v = np.random.normal(0, 1)  # v~N(0,1)
    l = u/(math.pow(math.fabs(v), (1/LAMBDA)))  # L=u/(|v|^1/lambda)
    return l


def AlgoritmoFPA(num):
    inicializa()
    for a in range(GENERACIONES):
        if(a % 75 == 0):
            print "Generacion: ", a
            grafica(num, X)  # Grafíca cada 75 Generaciones
        g = mejorPosicion(num)  # Selección del mejor global
        for i in range(POBLACION):
            r = random.uniform(0, 1)
            if r < p:
                L = VueloDeLevy()
                yi = X[:, i] + L*(X[:, i]-X[:, g])  # yi = xi + L(xi-xg)
            else:
                e = random.uniform(0, 1)
                while(True):
                    j = random.randint(0, POBLACION-1)
                    k = random.randint(0, POBLACION-1)
                    if k != i and k != j and j != i:  # j!=k!=i
                        break
                yi = X[:, i] + e*(X[:, j]-X[:, k])  # yi = xi +e(xj-xk)
            if f(num, yi[0], yi[1]) < f(num, X[0, i], X[1, i]):  # si f(yi)<f(xi)
                X[:, i] = yi  # xi=yi


AlgoritmoFPA(1)
b = mejorPosicion(1)
print "Generacion: 150"
print "Griewank function: "
# Imprime la mejor posición global de la última generación
print("X: ", X[0, b], "Y: ", X[1, b],
      "F(x,y): ", f(1, X[0, b], X[1, b]))
grafica(1, X)


AlgoritmoFPA(2)
b = mejorPosicion(2)
print "Generacion: 150"
print "Sphere function: "
# Imprime la mejor posición global de la última generación
print("X: ", X[0, b], "Y: ", X[1, b],
      "F(x,y): ", f(2, X[0, b], X[1, b]))
grafica(2, X)


AlgoritmoFPA(3)
b = mejorPosicion(3)
print "Generacion: 150"
print "Rastrigin function: "
# Imprime la mejor posición global de la última generación
print("X: ", X[0, b], "Y: ", X[1, b],
      "F(x,y): ", f(3, X[0, b], X[1, b]))
grafica(3, X)
