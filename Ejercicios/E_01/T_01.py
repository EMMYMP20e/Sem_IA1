import math
import sympy
import numpy as np
from matplotlib import pyplot as plt

#Méndez Pérez Emmanuel y Villaseñor Cisneros Damian Alfonso
#I7039 D04
#Ejercicio 1
#Desarrollado en Python 2.7

RANGO=100
ERROR=0.0001

def funcion1(l):    #f(l)=(20-2*l)^2*l
    return math.pow((20-2*l),2)*l


#Primera Derivada
def funcion1Prima(l):   #f'(l)=4(3*l^2-40*l+100)
    return 4*(3*math.pow(l,2)-40*l+100)


#Segunda Derivada
def funcion1Biprima(l):     #f''(l)=8(3l-20)
    return 8*(3*l-20)




inicio=0

# Gráfica primera función-----------------------------------
x=np.linspace(0,10,RANGO)   #Arreglo de 100 números dentro de [0,10]
y=np.zeros(len(x))          
for i in range(len(x)):
    y[i]=funcion1(x[i])     # y = x evaluado en la función

plt.plot(x,y,'b-',label='Funcion f(l)')    #Gráfica x,y
plt.xlabel("X")
plt.ylabel("Y")
plt.title("f(l)=(20-2*l)^2*l")
x=np.linspace(0,10,RANGO)   #Arreglo de 100 números dentro de [0,10]
y=np.zeros(len(x))

for i in range(len(x)):
    y[i]=funcion1Prima(x[i]) 
plt.plot(x,y,'y-',label='Funcion Prima')
for i in range(len(x)):
    y[i]=funcion1Biprima(x[i]) 
plt.plot(x,y,'r-',label='Funcion Biprima')
plt.grid()


#Método de Newton
x=np.linspace(inicio,1,RANGO)   #Arreglo de 100 números desde el inicio como input hasta 1
i=0
diferencia=1
while diferencia>ERROR:  #Calcula hasta que la diferencia entre xi y xri sea menor a .0001
    x[i+1]=x[i]-(funcion1Prima(x[i])/funcion1Biprima(x[i]))     #xi+1 = xi-(f'(xi)/f''(xi))
    diferencia=math.fabs(x[i+1]-x[i])
    x[i]=x[i+1]     #xi = xi+1
    i+=1
valorOptimo=funcion1(x[i])
evaluar=funcion1Biprima(x[i])   #Evalua f''(xi) para saber sí es máximo o mínimo
if evaluar<0:                   
    print("Maximo: ",valorOptimo," en x=",x[i]) 
    labelTxt='Maximo'
else:                                                       #imprime en consola el punto máximo o mínimo
    print("Minimo: ",valorOptimo," en x=",x[i])
    labelTxt='Minimo'
plt.plot(x[i],valorOptimo, 'ro',label=labelTxt) #Grafíca el punto máximo o mínimo
plt.legend(loc='upper right')
plt.show() #Muestra la gráfica