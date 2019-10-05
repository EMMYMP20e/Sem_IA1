import math
import sympy
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits import mplot3d

# Méndez Pérez Emmanuel
# I7039 D04
# Práctica 6
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


def grafica(num, vX):
    if num == 1:
        grafica1(vX)
    elif num == 2:
        grafica2(vX)
    else:
        grafica3(vX)


def rand():  # Genera vector de números random
    return random.uniform(0, 1), random.uniform(0, 1)


POBLACION = 50
RANGO = 50
GENERACIONES = 100
F = np.array([1.2, 1.2])  # Factor de Amplificación
CR = 0.6  # Constante de recombinación
D = 2  # Dimensiones


X = np.zeros((2, POBLACION))  # Individuos
U = np.zeros((2, POBLACION))  # Vector Prueba
V = np.zeros((2, POBLACION))  # Vector Mutado

xl = np.array([-5, -5])  # límite inferior
xu = np.array([5, 5])  # Límite superior


def inicializa():
    for i in range(POBLACION):
        X[:, i] = xl+(xu-xl)*rand()  # Inicializa individuos aleatoriamente


def generaRandoms(i):  # Números aleatorios tal que r1 != r2 != r3 != i
    while True:
        r1 = random.randint(0, POBLACION-1)
        r2 = random.randint(0, POBLACION-1)
        r3 = random.randint(0, POBLACION-1)
        if r1 != r2 and r1 != r3 and r2 != r3 and r1 != i and r2 != i and r3 != i:
            return r1, r2, r3


def mejorPosicion(num):  # Encuentra individuo con mejor posición
    best = 0
    for i in range(POBLACION):
        if f(num, X[0, i], X[1, i]) < f(num, X[0, best], X[1, best]):
            best = i
    return best


def algoritmoDE(num):
    for k in range(GENERACIONES):
        for i in range(POBLACION):
            r = generaRandoms(i)
            # vi = xr1 + F*(xr2 - xr3)
            V[:, i] = X[:, r[0]] + F*(X[:, r[1]] - X[:, r[2]])
            for j in range(D):
                ra = random.uniform(0, 1)
                if ra <= CR:
                    U[j, i] = V[j, i]  # Uij  = Vij
                else:
                    U[j, i] = X[j, i]  # Uij = Xij
            if f(num, U[0, i], U[1, i]) < f(num, X[0, i], X[1, i]):  # Si f(Ui) < f(xi)
                X[:, i] = U[:, i]   # Xi = Ui
        if(k % 25 == 0):
            grafica(num, X)  # Grafíca cada 25 Generaciones


inicializa()
algoritmoDE(1)
best = mejorPosicion(1)
print "Griewank function: "
# Imprime la mejor posición global de la última generación
print("X: ", X[0, best], "Y: ", X[1, best],
      "F(x,y): ", f(1, X[0, best], X[1, best]))

inicializa()
algoritmoDE(2)
best = mejorPosicion(2)
print "Sphere function: "
# Imprime la mejor posición global de la última generación
print("X: ", X[0, best], "Y: ", X[1, best],
      "F(x,y): ", f(2, X[0, best], X[1, best]))

inicializa()
algoritmoDE(3)
best = mejorPosicion(3)
print "Rastrigin function: "
# Imprime la mejor posición global de la última generación
print("X: ", X[0, best], "Y: ", X[1, best],
      "F(x,y): ", f(3, X[0, best], X[1, best]))
