import math
import sympy
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits import mplot3d

# Méndez Pérez Emmanuel
# I7039 D04
# Práctica 5
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


def rand():  # Genera vector de números random
    return random.uniform(0, 1), random.uniform(0, 1)


def randn():  # Random de [-2,2]
    return random.uniform(-2, 2), random.uniform(-2, 2)


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
    ax.contour3D(x, y, Z(x, y), 30, cmap='binary')

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


RANGO = 50

D = 2
W = np.array([0.6, 0.6])  # Factor de inercia
C1 = np.array([2, 2])  # Factor de aprendizaje cognitivo
C2 = np.array([2, 2])  # Factor de aprendizaje social
POBLACION = 100
GENERACIONES = 1000

X = np.zeros((2, POBLACION))  # Partículas
V = np.zeros((2, POBLACION))  # Velocidades
Xb = np.zeros((2, POBLACION))  # Mejores posiciones

xl = np.array([-5, -5])  # límite inferior
xu = np.array([5, 5])  # Límite superior


def inicializa():
    for i in range(POBLACION):
        X[:, i] = xl+(xu-xl)*rand()  # Inicializa partículas aleatoriamente
        Xb[:, i] = X[:, i]  # Inicialización de las mejores posiciones
        V[:, i] = randn()  # Velocidades aleatorias


def mejorPosicionF1():
    mejorGlobal = 0
    best = [Xb[0, mejorGlobal], Xb[1, mejorGlobal]]
    for i in range(POBLACION):
        if f1(X[0, i], X[1, i]) < f1(Xb[0, i], Xb[1, i]):  # Si f(xi) < f(xbi)
            Xb[:, i] = X[:, i]  # xbi=xi
        if f1(Xb[0, i], Xb[1, i]) < f1(best[0], best[1]):
            mejorGlobal = i
            best = [Xb[0, i], Xb[1, i]]  # Elegir partícula con mejor posición
    return mejorGlobal


def mejorPosicionF2():
    mejorGlobal = 0
    best = [Xb[0, mejorGlobal], Xb[1, mejorGlobal]]
    for i in range(POBLACION):
        if f2(X[0, i], X[1, i]) < f2(Xb[0, i], Xb[1, i]):  # Si f(xi) < f(xbi)
            Xb[:, i] = X[:, i]  # xbi=xi
        if f2(Xb[0, i], Xb[1, i]) < f2(best[0], best[1]):
            mejorGlobal = i
            best = [Xb[0, i], Xb[1, i]]  # Elegir partícula con mejor posición
    return mejorGlobal


def mejorPosicionF3():
    mejorGlobal = 0
    best = [Xb[0, mejorGlobal], Xb[1, mejorGlobal]]
    for i in range(POBLACION):
        if f3(X[0, i], X[1, i]) < f3(Xb[0, i], Xb[1, i]):  # Si f(xi) < f(xbi)
            Xb[:, i] = X[:, i]  # xbi=xi
        if f3(Xb[0, i], Xb[1, i]) < f3(best[0], best[1]):
            mejorGlobal = i
            best = [Xb[0, i], Xb[1, i]]  # Elegir partícula con mejor posición
    return mejorGlobal


def optimizacionParticulas():
    for i in range(POBLACION):
        # vi = w*vi + r1*c1(xbi-xi) + r2*c2(xg-xi)
        V[:, i] = W*V[:, i]+rand()*C1*(Xb[:, i]-X[:, i]) + rand()*C2*(X[:, best]-X[:, i])
        X[:, i] = X[:, i]+V[:, i]  # xi = xi + vi


# PSO para Griewank function--------------------------------------------------------
inicializa()
for i in range(GENERACIONES):
    # Encuentra mejor posición de partículas y mejor posición global
    best = mejorPosicionF1()
    optimizacionParticulas()
best = mejorPosicionF1()
print "Griewank function: "
# Imprime la mejor posición global de la última generación
print("X: ", Xb[0, best], "Y: ", Xb[1, best],"F1(x,y): ", f1(Xb[0, best], Xb[1, best]))
grafica1(X)

# PSO para Sphere function-----------------------------------------------------------
inicializa()
for i in range(GENERACIONES):
    # Encuentra mejor posición de partículas y mejor posición global
    best = mejorPosicionF2()
    optimizacionParticulas()
best = mejorPosicionF2()
print "Sphere function: "
# Imprime la mejor posición global de la última generación
print("X: ", Xb[0, best], "Y: ", Xb[1, best],"F2(x,y): ", f2(Xb[0, best], Xb[1, best]))
grafica2(X)

# PSO para Rastrigin function--------------------------------------------------------
inicializa()
for i in range(GENERACIONES):
    # Encuentra mejor posición de partículas y mejor posición global
    best = mejorPosicionF3()
    optimizacionParticulas()
best = mejorPosicionF3()
print "Rastrigin function: "
# Imprime la mejor posición global de la última generación
print("X: ", Xb[0, best], "Y: ", Xb[1, best],"F3(x,y): ", f3(Xb[0, best], Xb[1, best]))
grafica3(X)
