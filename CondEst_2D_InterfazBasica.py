#Conducción Estacionaria 2D

import numpy as np
import matplotlib.pyplot as plt
import pandas as ps
from scipy import special
import Funciones_No_estacionario as fun
import time
from tkinter import *
plt.style.use('seaborn-darkgrid')


def WinConduccionEst2D():
	def CalcCond():
		# Programa principal
		N = int(a1.get())
		#b = float(b1.get())
		#N = int(N1.get())
		Ta = float(Ta1.get())
		Tb = float(Tb1.get())
		Tc = float(Tc1.get())
		Td = float(Td1.get())
		#k = float(k1.get())
		#S = float(S1.get())



		A = fun.Matriz_Diagonal_Cond_est_2D(N)
		A[N**2-1,N**2-1]=-4

		b = fun.Vector_aux_cond_Est_2D(Ta,Tb,Tc,Td,N)

		u= fun.Sol_Sitema(A,b,N,Ta,Tb,Tc)

		f = np.copy(u[0:-1])

		nx, ny = (N, N) 
		f.shape = (nx, ny)
		x= np.linspace(0,1,nx)
		y= np.linspace(0,1,ny)
		xv, yv = np.meshgrid(x,y)
		h=plt.contourf(x, y, f, cmap='inferno')
		plt.show()


		print("\n--------------------------------------------")
		print("El vector auxiliar b es: ",b)
		print("La matriz A es: \n",A)
		print("La solución numérica es: \n",u)
		#print("La solución analítica es: \n",u_exa)
		#print("El error en la solución es: \n",error)
		print("\n--------------------------------------------\n")

		# Graficando la solucion
		#fun.Graficas(x,u,u_exa,'ECUACIÓN DE CALOR CON FUENTES.')

		# Guardando los datos
		#fun.Escritura(u,u_exa)

	# ---------------------------------------------------------------------------------
	root = Tk()
	root.geometry("320x200")
	root.title("Conducción de Calor Estacionaria 2D")

	l1 = Label(root, text='Número de nodos: ')
	l2 = Label(root, text='Temperatura a lo largo de a: ')
	l3 = Label(root, text='Temperatura a lo largo de b: ')
	l4 = Label(root, text='Temperatura a lo largo de c : ')
	l5 = Label(root, text='Temperatura a lo largo de d : ')

	#l5 = Label(root, text='Temperatura al final: ')
	#l6 = Label(root, text='Conductividad térmica: ')
	#l7 = Label(root, text='Fuentes o sumideros: ')

	a1 = Entry(root)
	a1.insert(0, '5')


	Ta1 = Entry(root)
	Ta1.insert(0, '1')

	Tb1 = Entry(root)
	Tb1.insert(0, '2')

	Tc1 = Entry(root)
	Tc1.insert(0, '3')

	Td1 = Entry(root)
	Td1.insert(0, '4')

	#k1 = Entry(root)
	#k1.insert(0, '1')

	#S1 = Entry(root)
	#S1.insert(0, '5')


	btn = Button(root, text='Calcular y generar grafica', command = CalcCond)

	l1.grid(row=0)
	l2.grid(row=3)
	l3.grid(row=4)
	l4.grid(row=5
		)
	l5.grid(row=6)
	#l6.grid(row=5)
	#l7.grid(row=6)

	a1.grid(row=0, column=1)
	#b1.grid(row=1, column=1)
	#N1.grid(row=2, column=1)
	Ta1.grid(row=3, column=1)
	Tb1.grid(row=4, column=1)
	Tc1.grid(row=5, column=1)
	Td1.grid(row=6, column=1)

	#k1.grid(row=5, column=1)
	#S1.grid(row=6, column=1)

	btn.grid(row = 15, columnspan=2)

	root.mainloop()

	#Comienza el diseño y la funcionalidad
	##############################################################################################################################