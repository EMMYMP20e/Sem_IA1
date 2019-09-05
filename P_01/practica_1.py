import math
import sympy
import numpy as np
from matplotlib import pyplot as plt

#Méndez Pérez Emmanuel 
#I7039 D04
#Práctica 1
#Desarrollado en Python 2.7

RANGO=100
ERROR=0.0001

def funcion1(x):    #f(x)= x^4 + 5x^3 + 4x^2 - 4x + 1
    return math.pow(x,4) + 5*math.pow(x,3) + 4*math.pow(x,2) - 4*x + 1

def funcion2(x):    #f(a)= sin(2a)
    return math.sin(x*2)

def funcion3(x):    #f(t)= sin(t) + tcos(t)
    return math.sin(x) + x*math.cos(x)

#Primera Derivada

def funcion1Prima(x):   #f'(x)= 4x^3 +15x^2 +8x -4
    return 4*math.pow(x,3) + 15*math.pow(x,2) + 8*x - 4

def funcion2Prima(x):   #f'(a)= 2cos(2a)
    return 2*math.cos(x*2)

def funcion3Prima(x):   #f'(t)= 2cos(t) - tsin(t)
    return 2*math.cos(x) - x*math.sin(x)

#Segunda Derivada

def funcion1Biprima(x):     #f''(x)=12x^2 + 30x +8
    return 12*math.pow(x,2) + 30*x +8

def funcion2Biprima(x):     #f''(a)=-4sin(2a)
    return -4*math.sin(x*2)

def funcion3Biprima(x):     #f''(t)=-3sin(t)-tcos(t)
    return -3*math.sin(x) - x*math.cos(x)




# Input de número de inicio

try:
    inicio=int(input("Punto de Inicio [-4,1]: "))
except:
    print "Error de Input, Inicio en -4"
    inicio=-4
print inicio
if (inicio>1 or inicio<-4):
    print "Error Numero fuera de rango, Inicio en -4"
    inicio=-4

# Gráfica primera función-----------------------------------
x=np.linspace(-4,1,RANGO)   #Arreglo de 100 números dentro de [-4,1]
y=np.zeros(len(x))          
for i in range(len(x)):
    y[i]=funcion1(x[i])     # y = x evaluado en la función

plt.plot(x,y,'b-',label='Funcion 1')    #Gráfica x,y
plt.xlabel("X")
plt.ylabel("Y")
plt.title("f(x)= x^4 + 5x^3 + 4x^2 - 4x + 1")
plt.grid()


#Método de Newton
x=np.linspace(inicio,1,RANGO)   #Arreglo de 100 números desde el inicio como input hasta 1
i=0
diferencia=1
while diferencia>ERROR:  #Calcula hasta que la diferencia entre xi y xri sea menor a .0001
    x[i+1]=x[i]-(funcion1Prima(x[i])/funcion1Biprima(x[i]))
    print x[i+1]
    diferencia=math.fabs(x[i+1]-x[i])
    x[i]=x[i+1]
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


#Cierre la ventana de la gráfica para continuar con las siguientes funciones

#-----Resultados obtenidos---------------------------------------------------

#en xi=-4 ('Minimo: ', -5.019646349962684, ' en x=', -2.9602734058319093)
#en xi=-1.5 ('Maximo: ', 5.049132261114146, ' en x=', -1.0975180200801602)
#en xi=0 ('Minimo: ', 0.30254533884856016, ' en x=', 0.3077914253705898)

#----------------------------------------------------------------------------

# Input de número de inicio

try:
    inicio=int(input("Punto de Inicio [-4,4]: "))
except:
    print "Error de Input, Inicio en -4"
    inicio=-4
print inicio
if (inicio>4 or inicio<-4):
    print "Error Numero fuera de rango, Inicio en -4"
    inicio=-4

# Gráfica segunda función-------------------------------------
x=np.linspace(-4,4,RANGO)        #Arreglo de 100 números dentro de [-4,4]
for i in range(len(x)):
    y[i]=funcion2(x[i])          # y = x evaluado en la función2
plt.plot(x,y,'b-',label='Funcion 2')    #Gráfica x,y
plt.xlabel("X")
plt.ylabel("Y")
plt.title("f(a)= sin(2a)")
plt.grid()

#Metodo de Newton
x=np.linspace(inicio,4,RANGO) #Arreglo de 100 números desde el inicio como input hasta 4
i=0
diferencia=1
while diferencia>ERROR:       #Calcula hasta que la diferencia entre xi y xri sea menor a .0001
    if funcion2Biprima(x[i])==0:
        x[i]=x[i+1]
    x[i+1]=x[i]-(funcion2Prima(x[i])/funcion2Biprima(x[i]))
    diferencia=math.fabs(x[i+1]-x[i])
    x[i]=x[i+1]
valorOptimo=funcion2(x[i])
evaluar=funcion2Biprima(x[i])       #Evalua f''(xi) para saber sí es máximo o mínimo
if evaluar<0:
    print("Maximo: ",valorOptimo," en x=",x[i])
    labelTxt='Maximo'
else:                                                       #imprime en consola el punto máximo o mínimo
    print("Minimo: ",valorOptimo," en x=",x[i])
    labelTxt='Minimo'
plt.plot(x[i],valorOptimo, 'ro',label=labelTxt) #Grafíca el punto máximo o mínimo
plt.legend(loc='upper right')
plt.show()   #Muestra la gráfica

#Cierre la ventana de la gráfica para continuar con las siguientes funciones

#-----Resultados obtenidos---------------------------------------------------

#en xi=-4 ('Minimo: ', -1.0, ' en x=', -3.9269908169872414)
#en xi=-2 ('Maximo: ', 1.0, ' en x=', -2.356194490192345)
#en xi=-1 ('Minimo: ', -1.0, ' en x=', -0.7853981633974483)
#en xi=1 ('Maximo: ', 1.0, ' en x=', 0.7853981633974483)
#en xi=2 ('Minimo: ', -1.0, ' en x=', 2.356194490192345)
#en xi=4 ('Maximo: ', 1.0, ' en x=', 3.9269908169872414)

#----------------------------------------------------------------------------


try:
    inicio=int(input("Punto de Inicio [-5,5]: "))
except:
    print "Error de Input, Inicio en -5"
    inicio=-5
print inicio
if (inicio>5 or inicio<-5):
    print "Error Numero fuera de rango, Inicio en -5"
    inicio=-5



# Gráfica segunda función-------------------------------------

x=np.linspace(-5,5,RANGO)
y=np.zeros(len(x))
for i in range(len(x)):
    y[i]=funcion3(x[i])

plt.plot(x,y,'b-',label='Funcion 3')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("f(t)= sin(t) + tcos(t)")
plt.grid()


#Metodo de Newton
x=np.linspace(inicio,5,RANGO)
i=0
diferencia=1
while diferencia>ERROR:
    x[i+1]=x[i]-(funcion3Prima(x[i])/funcion3Biprima(x[i]))
    diferencia=math.fabs(x[i+1]-x[i])
    x[i]=x[i+1]
valorOptimo=funcion3(x[i])
evaluar=funcion3Biprima(x[i])
if evaluar<0:
    print("Maximo: ",valorOptimo," en x=",x[i])
    labelTxt='Maximo'
else:
    print("Minimo: ",valorOptimo," en x=",x[i])
    labelTxt='Minimo'
plt.plot(x[i],valorOptimo, 'ro',label=labelTxt)
plt.legend(loc='upper right')
plt.show()


#-----Resultados obtenidos---------------------------------------------------

#en xi=-4 ('Maximo: ', 3.675233063660319, ' en x=', -3.6435971674277003)
#en xi=-2 ('Minimo: ', -1.391007845455877, ' en x=', -1.0768739863118115)
#en xi=2 ('Maximo: ', 1.391007845455877, ' en x=', 1.0768739863118115)
#en xi=4 ('Minimo: ', -3.675233063660319, ' en x=', 3.6435971674277003)

#----------------------------------------------------------------------------
