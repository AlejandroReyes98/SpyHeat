# PROGRAMA PARA LA RESOLUCIÓN DE LA ECUACIÓN DE CALOR CON FUENTES O SUMIDEROS

import numpy as np
import matplotlib.pyplot as plt
import Funciones_Conduccion1DEsta as fun
from tkinter import *
plt.style.use('Solarize_Light2')

def WinConduccionEst1D():
	def CalcCond():
		# Programa principal
		a = float(a1.get())
		b = float(b1.get())
		N = int(N1.get())
		Ta = float(Ta1.get())
		Tb = float(Tb1.get())
		k = float(k1.get())
		S = float(S1.get())

		# Cálculo de Constantes
		h,x,largo = fun.Constantes(a,b,N)
		print("\n-------------------------------------------------")
		print("El ancho de la malla es: ",h)
		print("El largo de la barra es: ",largo)
		print("---------------------------------------------------\n")

		# Vector que contiene las fuentes
		q = fun.Vector_Fuente(N,S,h,k)
		# Creación de vector b
		B = fun.Vector_aux(Ta,Tb,N,q)

		# Creación de matriz diagonal
		A = fun.Matriz_Diagonal(N,-2)

		# Solucion del sistema
		u = fun.Sol_Sitema(A,B,N,Ta,Tb)

		# Solución analítica del problema
		u_exa = fun.Sol_Analitica_F(a, b, Ta, Tb, S, k, N)

		error = fun.Error(u,u_exa,N)

		print("\n--------------------------------------------")
		print("El vector b es: ",B)
		print("La matriz A es: \n",A)
		print("La solución numérica es: \n",u)
		print("La solución analítica es: \n",u_exa)
		print("El error en la solución es: \n",error)
		print("\n--------------------------------------------\n")

		# Graficando la solucion
		fun.Graficas(x,u,u_exa,'ECUACIÓN DE CALOR CON FUENTES.')

		# Guardando los datos
		fun.Escritura(u,u_exa)

	# ---------------------------------------------------------------------------------
	root = Tk()
	root.geometry("320x200")
	root.title("Conducción de Calor 1D")

	l1 = Label(root, text='Comienzo del dominio: ')
	l2 = Label(root, text='Final del dominio: ')
	l3 = Label(root, text='Número de nodos: ')
	l4 = Label(root, text='Temperatura en el inicio: ')
	l5 = Label(root, text='Temperatura al final: ')
	l6 = Label(root, text='Conductividad térmica: ')
	l7 = Label(root, text='Fuentes o sumideros: ')

	a1 = Entry(root)
	a1.insert(0, '0')

	b1 = Entry(root)
	b1.insert(0, '5')

	N1 = Entry(root)
	N1.insert(0, '25')

	Ta1 = Entry(root)
	Ta1.insert(0, '10')

	Tb1 = Entry(root)
	Tb1.insert(0, '15')

	k1 = Entry(root)
	k1.insert(0, '1')

	S1 = Entry(root)
	S1.insert(0, '5')


	btn = Button(root, text='Calcular y generar grafica', command = CalcCond)

	l1.grid(row=0)
	l2.grid(row=1)
	l3.grid(row=2)
	l4.grid(row=3)
	l5.grid(row=4)
	l6.grid(row=5)
	l7.grid(row=6)

	a1.grid(row=0, column=1)
	b1.grid(row=1, column=1)
	N1.grid(row=2, column=1)
	Ta1.grid(row=3, column=1)
	Tb1.grid(row=4, column=1)
	k1.grid(row=5, column=1)
	S1.grid(row=6, column=1)

	btn.grid(row = 15, columnspan=2)

	root.mainloop()

	#Comienza el diseño y la funcionalidad
	##############################################################################################################################