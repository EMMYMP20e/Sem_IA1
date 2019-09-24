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

# Grafica primera función-----------------------------------------
def grafica1(px, py):
    x = np.linspace(-2, 2, RANGO)    # x,y son arreglos de 50 números en el rango (-2,2)
    y = np.linspace(-2, 2, RANGO)

    X, Y = np.meshgrid(x, y)    # Regresa una matriz coordenada de los vectores x,y
    
    Z = np.vectorize(f)     # vectorize Permite que la función f(x,y) reciba como parámetros los vectores x,y
    ax = plt.axes(projection='3d')  # Dibuja la gráfica de f(x,y)
    
    ax.contour3D(X, Y, Z(X, Y), RANGO, cmap='binary')   # Dibuja la gráfica de f(x,y)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    for i in range(POBLACION):
        ax.scatter3D(px[i], py[i], f(px[i], py[i]))     # Dibuja la población en la grafica
    plt.show()


# Grafica segunda función-----------------------------------------
def grafica2(px, py):
    x = np.linspace(-2, 6, RANGO)   # x,y son arreglos de 50 números en el rango (-2,6)
    y = np.linspace(-2, 6, RANGO)
    
    X, Y = np.meshgrid(x, y)    # Regresa una matriz coordenada de los vectores x,y
    
    Z = np.vectorize(f2)    # vectorize Permite que la función f2(x,y) reciba como parámetros los vectores x,y
    ax = plt.axes(projection='3d')
    
    ax.contour3D(X, Y, Z(X, Y), RANGO, cmap='binary')   # Dibuja la gráfica de f(x,y)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    for i in range(POBLACION):
        ax.scatter3D(px[i], py[i], f2(px[i], py[i]))    # Dibuja la población en la grafica
    plt.show()

# Inicializacion---------------------------------------------------
def inicializacion():
    x = np.zeros(POBLACION)      # x,y son vectores del tamaño de la poblacion
    y = np.zeros(POBLACION)
    for i in range(POBLACION):
        x[i] = xl+(xu-xl)*random.uniform(0, 1)       # xi = xl +(xu - xl)ri
        y[i] = xl+(xu-xl)*random.uniform(0, 1)
    return x, y


# Aptitud------------------------------------------------
def aptitudF1():
    for i in range(POBLACION):
        fxi = f(X[i], Y[i])     # f(xi)
        if fxi >= 0:    
            apt[i] = 1/(1+fxi)     # aptitudi(xi) = 1/(1 + f(xi))
        else:
            apt[i] = 1+math.fabs(fxi)   # aptitudi(xi) = 1 + |f(xi)|

# Aptitud para la función 2-----------------------------------------------
def aptitudF2():
    for i in range(POBLACION):
        fxi = f2(X[i], Y[i])
        if fxi >= 0:
            apt[i] = 1/(1+fxi)
        else:
            apt[i] = 1+math.fabs(fxi)


# Seleccion----------------------------------------------
def seleccion():
    aptTotal = 0
    for i in range(POBLACION):
        aptTotal += apt[i]          # aptitudTotal = aptitudTotal + aptitudI
    pi = np.zeros(POBLACION)
    for i in range(POBLACION):
        pi[i] = apt[i]/aptTotal     # pi = aptitudI / aptitudTotal
    r = random.uniform(0, 1)      
    pSum = 0
    for i in range(POBLACION):
        pSum = pSum+pi[i]           
        if pSum >= r:
            seleccion = i           # Se selecciona individuo i como padre
            return seleccion
    return seleccion

# Cruza---------------------------------------------------
def cruza():
    cont = 0
    for i in range(POBLACION/2):    # En cada iteracion se crean dos hijos nuevos
        while True:
            select1 = seleccion()   # Selección de ambos padres
            select2 = seleccion()
            if select1 != select2:  # Mientras que los padres no sean el mismo individuo
                break
        padre1 = [X[select1], Y[select1]]
        padre2 = [X[select2], Y[select2]]
        pc = random.randint(1, 2)   # pc = {1,D} D=2
        if pc == 1:                 # Si el punte de cruce es 1:
            X[cont] = padre1[0]     # El primer hijo toma la primer parte del padre1
            Y[cont] = padre2[1]     # y la segunda del padre2
            cont += 1
            X[cont] = padre2[0]     # El segundo hijo toma la primer parte del padre2
            Y[cont] = padre1[1]     # y la segunda del padre1
            cont += 1
        else:                       # Si el punte de cruce es 2:
            X[cont] = padre1[0]     # El primer hijo es idéntico al padre1
            Y[cont] = padre1[1]
            cont += 1
            X[cont] = padre2[0]     # El segundo hijo es idéntico al padre2
            Y[cont] = padre2[1]
            cont += 1

# Mutación--------------------------------------------------
def mutacion():
    pm = 0.01                       # Probablilidad de mutacion = 0.01
    for i in range(POBLACION):
        ra = random.uniform(0, 1)
        if ra < pm:
            X[i] = xl+(xu-xl)*random.uniform(0, 1)  # yij = xij + (xuj - xij)*rb
        ra = random.uniform(0, 1)
        if ra < pm:
            Y[i] = xl+(xu-xl)*random.uniform(0, 1)


# Algoritmo GA--------------------------------------------------
# Primera función
POBLACION = 200     # Definir la poblacion total

xl=-2
xu=2
X, Y = inicializacion()     # inicializa N padres dentro de los limites

apt = np.zeros(POBLACION)   # inicializa arreglo de apritudes

for i in range(100):        # 100 generaciones
    aptitudF1()             # Calcula la aptitud de cada individuo
    cruza()                 # Cruza de padres y creacion de hijos
    mutacion()              # Mutacion aleatoria de individuos nuevos
    
    if(i % 20 == 0):        # Cada 20 generaciones se muestra la gráfica
        grafica1(X,Y)

aptitudF1()     # Al terminar las generaciones se actualiza el vectro de aptitud
mejor = 0
im = 0
for i in range(POBLACION):
    if apt[i] > mejor:      # Encuentra la mejor aptitud
        mejor = apt[i]      
        im = i
print "Mayor aptitud: "
print 'x= ', X[im], 'y= ', Y[im], 'f(x,y)= ', f(X[im], Y[im])   # Imprime en consola el punto con mayor aptitud

grafica1(X, Y) # Muestra gráfica de la última generación

# Algoritmo GA--------------------------------------------------
# Segunda función


xl=-2
xu=6
X, Y = inicializacion()     # inicializa N padres dentro de los limites

apt = np.zeros(POBLACION)   # inicializa arreglo de apritudes

for i in range(100):        # 100 generaciones
    aptitudF2()             # Calcula la aptitud de cada individuo
    cruza()                 # Cruza de padres y creacion de hijos
    mutacion()              # Mutacion aleatoria de individuos nuevos

    if(i%20==0):            # Cada 20 generaciones se muestra la gráfica
        grafica2(X,Y)
        
aptitudF2()     # Al terminar las generaciones se actualiza el vectro de aptitud
mejor = 0
im = 0
for i in range(POBLACION):
    if apt[i] > mejor:      # Encuentra la mejor aptitud
        mejor = apt[i]
        im = i
print "Mayor aptitud: "
print 'x= ', X[im], 'y= ', Y[im], 'f(x,y)= ', f2(X[im], Y[im])  # Imprime en consola el punto con mayor aptitud

grafica2(X, Y)      # Muestra gráfica de la última generación