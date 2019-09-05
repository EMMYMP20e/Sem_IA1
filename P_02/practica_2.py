import math
import sympy
import random
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

# Méndez Pérez Emmanuel
# I7039 D04
# Práctica 2
# Desarrollado en Python 2.7

ERROR = 0.001
RANGO = 50


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


# Grafica primera función-----------------------------------------

# x,y son arreglos de 50 números en el rango (-2,2)
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

# Búsqueda Aleatoria-----------------------------------------------

xl = [-2, -2]  # Límites inferiores
xu = [2, 2]  # Límites superiores
fBest = float('inf')

for i in range(100):

    x = xl[0]+(xu[0]-xl[0])*random.uniform(0, 1)  # X <- Xi + (Xu-Xl)r
    y = xl[1]+(xu[1]-xl[1])*random.uniform(0, 1)

    fVal = f(x, y)

    if fVal < fBest:
        fBest = fVal
        xBest = x
        yBest = y

# Grafíca el punto Mínimo encontrado
ax.scatter3D(xBest, yBest, f(xBest, yBest))
print ("Funcion 1:")
print ("	Busqueda aleatoria")
print (" x:", xBest, " y: ", yBest, " f(x,y):", f(xBest, yBest))
plt.show()  # Muestra gráfica

# Resultados:
#(' x:', -0.5121974700021013, ' y: ', -0.05982611772968527, ' f(x,y):', -0.39259746373329585)
#(' x:', -0.8604350112217509, ' y: ', 0.189919218167236, ' f(x,y):', -0.3958440697282326)
# (' x:', -0.6993258254191606, ' y: ', -0.03755987472658129, ' f(x,y):', -0.42822527909253405


# Vuelve a graficar primera función-----------------------------------------


# x,y son arreglos de 50 números en el rango (-2,2)
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

# Gradiente Descendiente--------------------------------------------------

# x,y son arreglos de 50 números en el rango (-2,2)
x = np.linspace(-1, 2, RANGO)
y = np.linspace(-1, 2, RANGO)

h = 0.1
diferencia = 1
i = 0
# Termina de iterar hasta que la diferencia de
while diferencia > ERROR and i < RANGO-1:  # resultados sea menor a .001 o se termine de iterar el arreglo
    gradX = fdx(x[i], y[i])  # Calculo de gradiente ▼f(xi)
    gradY = fdy(x[i], y[i])
    x[i+1] = x[i]-(h*gradX)  # xi+1 = xi - h▼f(xi)
    y[i+1] = y[i]-(h*gradY)
    # Calcula la diferencia del resultado obtenido con el anterior
    diferencia = math.fabs(x[i+1]-x[i])
    x[i] = x[i+1]  # xi = xi+1
    y[i] = y[i+1]
    i += 1
ax.scatter3D(x[i], y[i], f(x[i], y[i]))  # Grafíca el punto Mínimo encontrado
print ("	Gradiente Descendiente")
print (" x:", x[i], " y:", y[i], " f(x,y):", f(x[i], y[i]))
plt.show()  # Muestra gráfica

# Resultado:
#(' x:', -0.7114087963902055, ' y:', -0.11867197591511408, ' f(x,y):', -0.4228686923541326)


# Grafica segunda función-----------------------------------------

# x,y son arreglos de 50 números en el rango (-2,6)
x = np.linspace(-2, 6, RANGO)
y = np.linspace(-2, 6, RANGO)


X, Y = np.meshgrid(x, y)  # Regresa una matriz coordenada de los vectores x,y
# vectorize Permite que la función f(x) reciba como parámetros los vectores x,y
Z = np.vectorize(f2)
ax = plt.axes(projection='3d')
# Dibuja la gráfica de f(x,y)
ax.contour3D(X, Y, Z(X, Y), RANGO, cmap='binary')
ax.set_ylabel('y')
ax.set_zlabel('z')


# Búsqueda Aleatoria-----------------------------------------------

xl = [-2, -2]  # Límites inferiores
xu = [6, 6]  # Límites superiores
fBest = float('inf')

for i in range(100):

    x = xl[0]+(xu[0]-xl[0])*random.uniform(0, 1)  # X <- Xi + (Xu-Xl)r
    y = xl[1]+(xu[1]-xl[1])*random.uniform(0, 1)

    fVal = f2(x, y)

    if fVal < fBest:
        xBest = x
        yBest = y
        fBest = fVal

# Grafíca el punto Mínimo encontrado
ax.scatter3D(xBest, yBest, f2(xBest, yBest))
print ("Funcion 2:")
print ("	Busqueda aleatoria")
print (" x:", xBest, " y: ", yBest, " f2(x,y):", f2(xBest, yBest))
plt.show()  # Muestra gráfica

# Resultados:
#(' x:', 2.2190775751048175, ' y: ', 2.123763602832196, ' f2(x,y):', 0.06331241329981252)
#(' x:', 1.8752656046518545, ' y: ', 1.7784477914043446, ' f2(x,y):', 0.06464405051648026)
#(' x:', 1.704647488191612, ' y: ', 2.3904430710795275, ' f2(x,y):', 0.23967889798553688)


# Vuelve a graficar segunda función-----------------------------------------

x = np.linspace(-2, 6, RANGO)
y = np.linspace(-2, 6, RANGO)


X, Y = np.meshgrid(x, y)
Z = np.vectorize(f2)
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z(X, Y), RANGO, cmap='binary')
ax.set_ylabel('y')
ax.set_zlabel('z')


# Gradiente Descendiente------------------------------------------

h = 0.1
diferencia = 1
i = 0
while diferencia > ERROR and i < RANGO-1:
    gradX = f2dx(x[i], y[i])  # Calculo de gradiente ▼f(xi)
    gradY = f2dy(x[i], y[i])
    x[i+1] = x[i]-(h*gradX)  # xi+1 = xi - h▼f(xi)
    y[i+1] = y[i]-(h*gradY)
    # Calcula la diferencia del resultado obtenido con el anterior
    diferencia = math.fabs(x[i+1]-x[i])
    x[i] = x[i+1]  # xi = xi+1
    y[i] = y[i+1]
    i += 1
ax.scatter3D(x[i], y[i], f2(x[i], y[i]))  # Grafíca el punto Mínimo encontrado
print ("	Gradiente Descendiente")
print (" x:", x[i], " y:", y[i], " f2(x,y):", f2(x[i], y[i]))
plt.show()  # Muestra gráfica

# Resultado:
#(' x:', 1.996038591874287, ' y:', 1.996038591874287, ' f2(x,y):', 3.138550867693165e-05)
