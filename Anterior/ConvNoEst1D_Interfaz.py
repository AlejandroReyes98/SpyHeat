import numpy as np
import matplotlib.pyplot as plt
import pandas as ps
from scipy import special
import Funciones_No_estacionario as fun
import time
from tkinter import *
plt.style.use('seaborn-darkgrid')

def WinConveccionNoEst1D():


	def calcConv_DatosUsuario():
		# Ingreso de variables
		a = float(a1.get())
		b = float(b1.get())
		Ta = float(Ta1.get())
		Tb = float(Tb1.get())
		K = float(K1.get())
		Tmax = float(Tmax1.get())
		N = int(N1.get())
		S = float(S1.get())
		ht = float(ht1.get())
		v = float(v1.get())
		Tol = float(Tol1.get())

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

		# Llamado a función para guardar los datos
		fun.Escritura(xa,ua)

	def calcConv_Texto():
		#Lectura del archivo.
		archivoDatos=filedialog.askopenfilename(title="Abrir archivo",filetypes=(("Text Files","*.txt"),))
		archivoDatos=open(archivoDatos,'r')
		val=np.loadtxt(archivoDatos)
		archivoDatos.close()
		# Ingreso de variables
		a = float(val[0])
		b = float(val[1])
		N = int(val[2])
		Ta = float(val[3])
		Tb = float(val[4])
		K = float(val[5])
		S = int(val[6])
		ht = float(val[7])
		Tmax = int(val[8])
		v = float(val[9])
		Tol = float(val[10])

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

		# Llamado a función para guardar los datos
		fun.Escritura(xa,ua)

	def GraficarError_DatosUsuario():
		# Ingreso de variables
		a = float(a1.get())
		b = float(b1.get())
		Ta = float(Ta1.get())
		Tb = float(Tb1.get())
		K = float(K1.get())
		Tmax = float(Tmax1.get())
		N = int(N1.get())
		S = float(S1.get())
		ht = float(ht1.get())
		v = float(v1.get())
		Tol = float(Tol1.get())

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
		            
		    # Actualizacion de la solucion para dar el siguiente paso
		    f = np.copy(u[1:N+1])
		    uold = np.copy(u)
		    
		    if (err < Tol):
		        break

		fun.Graficas_Error(error)
		#Llamado a función para guardar los datos

	def GraficarError_Texto():
		#Lectura del archivo.
		archivoDatos=filedialog.askopenfilename(title="Abrir archivo",filetypes=(("Text Files","*.txt"),))
		archivoDatos=open(archivoDatos,'r')
		val=np.loadtxt(archivoDatos)
		archivoDatos.close()
		# Ingreso de variables
		a = float(val[0])
		b = float(val[1])
		N = int(val[2])
		Ta = float(val[3])
		Tb = float(val[4])
		K = float(val[5])
		S = int(val[6])
		ht = float(val[7])
		Tmax = int(val[8])
		v = float(val[9])
		Tol = float(val[10])

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
		            
		    # Actualizacion de la solucion para dar el siguiente paso
		    f = np.copy(u[1:N+1])
		    uold = np.copy(u)
		    
		    if (err < Tol):
		        break

		fun.Graficas_Error(error)





	##############################################################################################################################
	#Comienza el diseño y la funcionalidad 

	root = Tk()
	root.geometry("480x350")
	root.title("Convección de calor No estacionaria. 1D")

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

	a1 = Entry(root)
	a1.insert(0,'0')

	b1 = Entry(root)
	b1.insert(0,'2.5')

	Ta1 = Entry(root)
	Ta1.insert(0,'1')

	Tb1 = Entry(root)
	Tb1.insert(0,'0')

	K1 = Entry(root)
	K1.insert(0,'0.001')

	Tmax1= Entry(root)
	Tmax1.insert(0,'1')

	N1 = Entry(root)
	N1.insert(0,'300')

	S1 = Entry(root)
	S1.insert(0,'0')

	ht1= Entry(root)
	ht1.insert(0,'0.002')

	v1 = Entry(root)
	v1.insert(0,'1')

	Tol1 = Entry(root)
	Tol1.insert(0,'1e-6')


	btn = Button(root, text='Calcular aproximacion numérica y generar gráfica con datos ingresados por el usuario', command = calcConv_DatosUsuario)
	btn2 = Button(root, text='Calcular y graficar el error con los datos del usuario', command = GraficarError_DatosUsuario)
	btn3 = Button(root, text='Calcular aproximacion numérica y generar gráfica con datos del archivo de texto', command = calcConv_Texto)
	btn4 = Button(root, text='Calcular y graficar el error con los datos del archivo de texto', command = GraficarError_Texto)


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

	a1.grid(row=0, column=1)
	b1.grid(row=1, column=1)
	Ta1.grid(row=2, column=1)
	Tb1.grid(row=3, column=1)
	K1.grid(row=4, column=1)
	Tmax1.grid(row=5, column=1)
	N1.grid(row=6, column=1)
	S1.grid(row=7, column=1)
	ht1.grid(row=8, column=1)
	v1.grid(row=9, column=1)
	Tol1.grid(row=10, column=1)


	btn.grid(row = 15, columnspan=5)
	btn2.grid(row = 17, columnspan=5)
	btn3.grid(row = 19, columnspan=5)
	btn4.grid(row = 21, columnspan=5)



	root.mainloop()

	#Comienza el diseño y la funcionalidad
	##############################################################################################################################