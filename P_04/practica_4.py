import math
import sympy
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits import mplot3d

# Méndez Pérez Emmanuel
# I7039 D04
# Práctica 4
# Desarrollado en Python 2.7


def f(x, y):  # f(x,y) = x*e^(-x^2-y^2)
    return x*math.pow(math.e, -1*math.pow(x, 2)-(math.pow(y, 2)))


def f2(x, y):  # f(x,y) = (x-2)^2+(y-2)^2
    return math.pow(x-2, 2)+math.pow(y-2, 2)

# Grafica primera función-----------------------------------------
def grafica1(vX):
    a = np.linspace(-2, 2, RANGO)    # a,b son arreglos de 50 números en el rango (-2,2)
    b = np.linspace(-2, 2, RANGO)

    x,y = np.meshgrid(a, b)    # Regresa una matriz coordenada de los vectores x,y
    print x
    Z = np.vectorize(f)     # vectorize Permite que la función f(x,y) reciba como parámetros los vectores x,y
    ax = plt.axes(projection='3d')  # Dibuja la gráfica de f(x,y)
    
    ax.contour3D(x, y, Z(x, y), RANGO, cmap='binary')   # Dibuja la gráfica de f(x,y)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    for i in range(MU):
        ax.scatter3D(vX[0,i], vX[1,i], f(vX[0,i], vX[1,i]))     # Dibuja la población en la grafica
    plt.show()

# Grafica segunda función-----------------------------------------
def grafica2(vX):
    a = np.linspace(-2, 6, RANGO)    # a,b son arreglos de 50 números en el rango (-2,2)
    b = np.linspace(-2, 6, RANGO)

    x,y = np.meshgrid(a, b)    # Regresa una matriz coordenada de los vectores x,y
    
    Z = np.vectorize(f2)     # vectorize Permite que la función f(x,y) reciba como parámetros los vectores x,y
    ax = plt.axes(projection='3d')  # Dibuja la gráfica de f(x,y)
    
    ax.contour3D(x, y, Z(x, y), RANGO, cmap='binary')   # Dibuja la gráfica de f(x,y)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    for i in range(MU):
        ax.scatter3D(vX[0,i], vX[1,i], f2(vX[0,i], vX[1,i]))     # Dibuja la población en la grafica
    plt.show()


def Recombinar(x1,x2):  # Recombinación sexual intermedia
    y=0.5*(x1+x2)
    return y


def rand():
    return random.uniform(0,1),random.uniform(0,1)  # Genera vector de números random

def seleccionMmasL():       # (m+l)-ES    
    XY=np.hstack((X,Y))     # Une vectores padres e hijos
    sigmas=np.hstack((sigmaX,sigmaY))       # Une sigmas de padres e hijos
    Total=np.vstack((XY,sigmas,fitness))    # Une todos los vectores con su respectivo fitness
    Total=Total.T
    Total=Total[Total[:,4].argsort()]       # Ordena los vecores segun el mejor fitness
    for i in range(MU):         # Se asigna los mejores indiviudos a la siguiente generación de padres
        X[0,i]=Total[i,0]
        X[1,i]=Total[i,1]
        sigmaX[0,1]=Total[i,2]
        sigmaX[1,i]=Total[i,3]
        fitness[i]=Total[i,4]

def seleccionM_L():         # (m,l)-ES  
    fitnessY=np.zeros(LAMBDA)   
    for i in range(LAMBDA):
        fitnessY[i]=fitness[MU+i]   # Vector con los fitness de los hijos
    Total=np.vstack((Y,sigmaY,fitnessY))    # Une los vectores de hijos con sigmas y respectivos fitness
    Total=Total.T
    Total=Total[Total[:,4].argsort()]       # Ordena los vecores segun el mejor fitness
    for i in range(MU):         # Se asigna los mejores indiviudos a la siguiente generación de padres
        X[0,i]=Total[i,0]
        X[1,i]=Total[i,1]
        sigmaX[0,1]=Total[i,2]
        sigmaX[1,i]=Total[i,3]
        fitness[i]=Total[i,4]


RANGO=50
GENERACIONES=10
D=2
MU=40
LAMBDA=60

xl=np.array([-2,-2])
xu=np.array([2,2])

X=np.zeros((2,MU))          # padres
Y=np.zeros((2,LAMBDA))      # hijos
sigmaX=np.zeros((2,MU))     
sigmaY=np.zeros((2,LAMBDA))
r=np.zeros((2,LAMBDA))      # vector para random normal
fitness=np.zeros(MU+LAMBDA)

def inicializa():
    for i in range(MU):
        X[:,i]=xl+(xu-xl)*rand()    # X con valores random
        sigmaX[0,i]=random.uniform(0,.5)    # sigma con valores random
        sigmaX[1,i]=random.uniform(0,.5)
        fitness[i]=f(X[0,i],X[1,i])     #cacula el fitness de los valores random


def estrategias_evolutivas(MmasL):
    for i in range(GENERACIONES):
        if(i % 5 ==0):          
            print "Generacion: ",i
            grafica1(X)                 #Grafíca cada 5 generaciones
        for j in range(LAMBDA):
            r1=random.randint(1,MU-1)       # Selecciona aleatoriamente dos padres
            r2=random.randint(1,MU-1)   
            Y[:,j]=Recombinar(X[:,r1],X[:,r2])      # Recombinar los padres para crear un hijo
            sigmaY[:,j]=Recombinar(sigmaX[:,r1],sigmaX[:,r2])
            r[:,j]=np.random.normal(0,sigmaY[:,j],2)        # Genera vector con random normal
            Y[:,j]=Y[:,j]+r[:,j]    #Se le añade el random normal al hijo
            fitness[j+MU]=f(Y[0,j],Y[1,j])

        if MmasL==True: #Al terminar de crear hijos se hace la seleccion para la siguiente generación
            seleccionMmasL()
        else:
            seleccionM_L()

    print "Generacion: ",i
    print "X,Y: ",X[:,0],"f(x,y)",(f(X[0,0],X[1,0]))     #Imprime resultado con mejor fitness
    grafica1(X)

inicializa()
estrategias_evolutivas(True)
inicializa()
estrategias_evolutivas(False)

def inicializaF2():
    for i in range(MU):
        X[:,i]=xl+(xu-xl)*rand()    # X con valores random
        sigmaX[0,i]=random.uniform(0,.5)     # sigma con valores random
        sigmaX[1,i]=random.uniform(0,.5)
        fitness[i]=f2(X[0,i],X[1,i])    #cacula el fitness de los valores random


def estrategias_evolutivasF2(MmasL):
    for i in range(GENERACIONES):
        if(i % 5 ==0):      
            print "Generacion: ",i
            grafica2(X)                 #Grafíca cada 5 generaciones
        for j in range(LAMBDA):
            r1=random.randint(1,MU-1)       # Selecciona aleatoriamente dos padres
            r2=random.randint(1,MU-1)   
            Y[:,j]=Recombinar(X[:,r1],X[:,r2])      # Recombinar los padres para crear un hijo
            sigmaY[:,j]=Recombinar(sigmaX[:,r1],sigmaX[:,r2])
            r[:,j]=np.random.normal(0,sigmaY[:,j],2)        # Genera vector con random normal
            Y[:,j]=Y[:,j]+r[:,j]    #Se le añade el random normal al hijo
            fitness[j+MU]=f2(Y[0,j],Y[1,j])

        if MmasL==True:     #Al terminar de crear hijos se hace la seleccion para la siguiente generación
            seleccionMmasL()
        else:
            seleccionM_L()

    print "Generacion: ",i
    print "X,Y: ",X[:,0],"f2(x,y)",(f2(X[0,0],X[1,0]))     #Imprime resultado con mejor fitness
    grafica2(X)

xl=np.array([-2,-2])
xu=np.array([6,6])

inicializaF2()
estrategias_evolutivasF2(True)
inicializaF2()
estrategias_evolutivasF2(False)