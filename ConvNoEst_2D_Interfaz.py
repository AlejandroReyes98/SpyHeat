#Convección No Estacionaria 2D
import Funciones_No_estacionario as fun
import numpy as np
import matplotlib.pyplot as plt
import pandas as ps
from scipy import special
import Funciones_No_estacionario as fun
import time
from tkinter import *
plt.style.use('seaborn-darkgrid')


def WinConveccionNoEst2D():
	def CalcCond():
		# Programa principal
		a = int(a1.get())
		b = float(b1.get())
		N = int(N1.get())
		Ta = float(Ta1.get())
		Tb = float(Tb1.get())
		Tc = float(Tc1.get())
		Td = float(Td1.get())
		K = float(K1.get())
		S = float(S1.get())
		ht= float(ht1.get())
		Tmax= int(Tmax1.get())
		v= int(v1.get())



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
		h=plt.contourf(x, y, f)
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
	root.geometry("320x300")
	root.title("Conducción de Calor Estacionaria 2D")

	l1 = Label(root, text='a: ')
	l2 = Label(root, text='b: ')
	l3 = Label(root, text='Número de nodos: ')
	l4 = Label(root, text='Temperatura a lo largo de a: ')
	l5 = Label(root, text='Temperatura a lo largo de b: ')
	l6 = Label(root, text='Temperatura a lo largo de c : ')
	l7 = Label(root, text='Temperatura a lo largo de d : ')
	l8 = Label(root, text='K: ')
	l9 = Label(root, text='S: ')
	l10 = Label(root, text='ht: ')
	l11 = Label(root, text='Tmax: ')
	l12= Label(root, text='v: ')



	#l5 = Label(root, text='Temperatura al final: ')
	#l6 = Label(root, text='Conductividad térmica: ')
	#l7 = Label(root, text='Fuentes o sumideros: ')

	a1 = Entry(root)
	a1.insert(0, '0')

	b1= Entry(root)
	b1.insert(0,'1')

	N1=Entry(root)
	N1.insert(0,'11')

	Ta1 = Entry(root)
	Ta1.insert(0, '1')

	Tb1 = Entry(root)
	Tb1.insert(0, '2')

	Tc1 = Entry(root)
	Tc1.insert(0, '3')

	Td1 = Entry(root)
	Td1.insert(0, '4')

	K1 = Entry(root)
	K1.insert(0, '0.001')

	S1 = Entry(root)
	S1.insert(0,'0')

	ht1 = Entry(root)
	ht1.insert(0,'0.02')

	Tmax1 =Entry(root)
	Tmax1.insert(0,'1')

	v1= Entry(root)
	v1.insert(0,'1')

	#S1 = Entry(root)
	#S1.insert(0, '5')


	btn = Button(root, text='Calcular y generar grafica', command = CalcCond)

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
	l12.grid(row=11)




	a1.grid(row=0, column=1)
	b1.grid(row=1, column=1)
	N1.grid(row=2, column=1)
	Ta1.grid(row=3, column=1)
	Tb1.grid(row=4, column=1)
	Tc1.grid(row=5, column=1)
	Td1.grid(row=6, column=1)
	K1.grid(row=7, column=1)
	S1.grid(row=8, column=1)
	ht1.grid(row=9, column=1)
	Tmax1.grid(row=10, column=1)
	v1.grid(row=11, column=1)


	btn.grid(row = 15, columnspan=2)

	root.mainloop()

	#Comienza el diseño y la funcionalidad
	##############################################################################################################################