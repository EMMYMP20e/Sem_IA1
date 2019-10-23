import math
import sympy
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits import mplot3d

# Méndez Pérez Emmanuel
# I7039 D04
# Práctica 8
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

POBLACION = 30
GENERACIONES = 20

X = np.zeros((2, POBLACION))  # Individuos

xl = np.array([-10, -10])  # límite inferior
xu = np.array([10, 10])  # Límite superior


def promedioX(j):   #
    sum = 0
    for k in range(POBLACION):
        sum += X[j, k]
    return sum/POBLACION


def rand():  # Genera vector de números random
    return random.uniform(0, 1), random.uniform(0, 1)


def randTf():  # Genera vector de números random {1,2} factor de enseñanza
    return random.randint(1, 2), random.randint(1, 2)


def mejorPosicion(num):  # Encuentra individuo con mejor posición
    best = 0
    for i in range(POBLACION):
        if f(num, X[0, i], X[1, i]) < f(num, X[0, best], X[1, best]):
            best = i
    return best


def inicializa():
    for i in range(POBLACION):
        X[:, i] = xl+(xu-xl)*rand()  # Inicializa fuentes aleatoriamente


def faseEnsenanza(num, i):
    t = mejorPosicion(num)
    Xt = np.array(X[:, t])  # Selección del maestro
    Tf = randTf()  # Tf = random [0,1]
    c = np.array([0, 0])
    for j in range(D-1):
        promXj = promedioX(j)  # xj
        r = random.uniform(0, 1)  # random [0,1]
        c[j] = X[j, i]+r*(Xt[j]-Tf[j]*promXj)  # cij = xij + r*(xtj-Tfxj)
    if f(num, c[0], c[1]) < f(num, X[0, i], X[1, i]):  # Si f(ci) < f(xi)
        X[:, i] = c  # xi = ci


def faseAprendizaje(num, i):
    while(True):
        k = random.randint(0, POBLACION-1)  # Número aleatorio  tal que i!=k
        if k != i:
            break
    c = np.array([0, 0])
    if f(num, X[0, i], X[1, i]) < f(num, X[0, k], X[1, k]):  # Si f(xi) < f(xk)
        for j in range(D-1):
            r = random.uniform(0, 1)  # r = random [0,1]
            c[j] = X[j, i]+r*(X[j, i]-X[j, k])  # cij = xij + r*(xij-xkj)
    else:
        for j in range(D-1):
            r = random.uniform(0, 1)  # r = random [0,1]
            c[j] = X[j, i]+r*(X[j, k]-X[j, i])  # cij = xij + r*(xkj-xij)
    if f(num, c[0], c[1]) < f(num, X[0, i], X[1, i]):   # Si f(ci) < f(xi)
        X[:, i] = c  # xi = ci


def algoritmoTLBO(num):
    inicializa()
    for j in range(GENERACIONES):
        if(j % 10 == 0):
            print "Generacion: ", j
            grafica(num, X)  # Grafíca cada 25 Generaciones
        for i in range(POBLACION):
            faseEnsenanza(num, i)
            faseAprendizaje(num, i)


algoritmoTLBO(1)
b = mejorPosicion(1)
print "Generacion: 20"
print "Griewank function: "
# Imprime la mejor posición global de la última generación
print("X: ", X[0, b], "Y: ", X[1, b],
      "F(x,y): ", f(1, X[0, b], X[1, b]))
grafica(1, X)


algoritmoTLBO(2)
b = mejorPosicion(2)
print "Generacion: 20"
print "Sphere function: "
# Imprime la mejor posición global de la última generación
print("X: ", X[0, b], "Y: ", X[1, b],
      "F(x,y): ", f(2, X[0, b], X[1, b]))
grafica(2, X)

algoritmoTLBO(3)
b = mejorPosicion(3)
print "Generacion: 20"
print "Rastrigin function: "
# Imprime la mejor posición global de la última generación
print("X: ", X[0, b], "Y: ", X[1, b],
      "F(x,y): ", f(3, X[0, b], X[1, b]))
grafica(3, X)
