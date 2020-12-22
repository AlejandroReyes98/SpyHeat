import numpy as np
import matplotlib.pyplot as plt
import pandas as ps
from scipy import special
import Funciones_No_estacionario as fun
import time
from tkinter import *
plt.style.use('Solarize_Light2')

def calcConv():
	# Ingreso de variables
	a = int(a.get())
	b = int(b.get())
	Ta = float(Ta.get())
	Tb = float(Tb.get())
	k = float(k.get())
	Tmax = float(Tmax.get())
	N = int(N.get())
	S = float(S.get())
	ht = float(ht.get())
	u = float(u.get())
	Tol = float(Tol.get())

	# Cálculo de Constantes
	h,x,lar,Nt,r,p = fun.Constantes(a,b,N,ht,Tmax,K,v)
	print("\n-------------------------------------------------")
	print("El ancho de la malla es: ",h)
	print("El largo de la barra es: ",lar)
	print("El número de pasos en el tiempo es: ",Nt)
	print("Constante r: ",r)
	print("Constante p: ",p)
	print("---------------------------------------------------\n")

	# Discretización del dominio
	x = fun.Dominio(a,b,N)
	#Llamada al vector auxiliar
	u = fun.Vector_aux(Ta,Tb,N,0)

	# Este es lado derecho de la ecuación, que contiene la condicion inicial.
	# Es decir la solucion en el paso 0. Por eso hacemos una copia de u.
	f = np.copy(u[1:N+1])
	uold = np.copy(u)

	# Construccion de la matriz
	A = fun.Matriz_Diagonal_Conv_Noest(N,r,p)

	#Graficación de la condición inicial
	#plt.plot(x,u,'--k',label='Inicial')

	# Definición del vector del error
	error = []

	#Solución Analítica del problema
	xa, ua = fun.Sol_Analitica(a,b,K,Tmax,N,v)

	# Ciclo en el tiempo, desde 0 hasta Nt+1
	for n in range(1,Nt+1):
	    f[0] += (p+r)*Ta
	    f[N-1] += -(p-r)*Tb
	    # Solución al sistema lineal
	    u[1:N+1] = np.linalg.solve(A,f) 
	    
	    # Cálculo del error y modificación del vector
	    err = np.sqrt(h) * np.linalg.norm(uold-u)
	    error.append(err)
	    
	    if (n % 100==0):
	        etiqueta = 'Sol. Num. steep = {}'.format(n*ht)
	        plt.plot(x, u, '.--', label=etiqueta)
	            
	    # Actualizacion de la solucion para dar el siguiente paso
	    f = np.copy(u[1:N+1])
	    uold = np.copy(u)
	    
	    if (err < Tol):
	        break

	# Llamado a funciones para la graficación
	fun.Graficas(xa,ua,'Solución Analítica y Numérica')
	fun.Graficas_Error(error)

	# Llamado a función para guardar los datos
	fun.Escritura(xa,ua)

##############################################################################################################################
#Comienza el diseño y la funcionalidad 
root = Tk()
root.geometry("320x200")
root.title("Transferencia de Calor 1D")

l1 = Label(root, text='Punto de inicio del conductor: ')
l2 = Label(root, text='Punto final del conductor: ')
l3 = Label(root, text='Temperatura frontera A: ')
l4 = Label(root, text='Temperatura frontera B: ')
l5 = Label(root, text='Conductividad térmica: ')
l6 = Label(root, text='Tiempo total: ')
l7 = Label(root, text='Numero de nodos: ')
l8 = Label(root, text='Fuentes o sumideros: ')
l9 = Label(root, text='Paso de tiempo: ')
l10 = Label(root, text='Velocidad: ')
l11 = Label(root, text='Tolerancia: ')

a = Entry(root)
a.insert(0,'0')

b = Entry(root)
b.insert(0,'2.5')

Ta = Entry(root)
Ta.insert(0,'1')

Tb = Entry(root)
Tb.insert(0,'0')

k = Entry(root)
k.insert(0,'0.001')

Tmax= Entry(root)
Tmax.insert(0,'1')

N = Entry(root)
N.insert(0,'300')

S = Entry(root)
S.insert(0,'0')

ht= Entry(root)
ht.insert(0,'0.002')

u = Entry(root)
u.insert(0,'1')

Tol = Entry(root)
Tol.insert(0,'1e-6')


btn = Button(root, text='Calcular y generar grafica', command = calcConv)
#btn2 = Button(root, text='Generar simulación', command = calcSimul)

l1.grid(row=0)
l2.grid(row=1)
l3.grid(row=2)
l4.grid(row=3)
l5.grid(row=4)
l6.grid(row=5)
l7.grid(row=6)
l8.grid(row=7)
l9.grid(row=8)
l10.grid(row=9)
l11.grid(row=10)

a.grid(row=0, column=1)
b.grid(row=1, column=1)
Ta.grid(row=2, column=1)
Tb.grid(row=3, column=1)
k.grid(row=4, column=1)
Tmax.grid(row=5, column=1)
N.grid(row=6, column=1)
S.grid(row=7, column=1)
ht.grid(row=8, column=1)
u.grid(row=9, column=1)
Tol.grid(row=10, column=1)


btn.grid(row = 15, columnspan=2)
#btn2.grid(row = 16, columnspan=2)

root.mainloop()

#Comienza el diseño y la funcionalidad
##############################################################################################################################