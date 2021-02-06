from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import matplotlib.animation as animation
plt.style.use('Solarize_Light2')


###############################################################################################################################
#Comienza funcion asingada al boton "Simulacion" en la interfaz gráfica

def WinConduccionNoEst1D():
	def calcSimul():
		#Lectura de Datos
		L = float(Long.get())
		T1 = float(TA.get())
		T2 = float(TB.get())
		k = float(kt.get())
		Nodos = int(N.get())
		tfinal1 = float(tfinal.get())
		Tinic1 = [float(i) for i in Tinic.get().split(",")]

		#Se asignan las condiciones de frontera 
		Tinic1[0] = T1
		Tinic1[-1] = T2
		print(Tinic1)
		Tinic1 = np.array(Tinic1)
		Tmax=Tinic1.max()
		
		#Discretizamos el dominio
		x = np.linspace(0,L,Nodos)
		barra = np.ones(len(x))
		dx = L/(Nodos-1)
		t = 0.0
		dt = (dx**2/(2*k))/1.001

		#Comienza la implementación del algoritmo de diferencias finitas
		Tdt=Tinic1.copy()
		Tsol = [Tinic1]
		tsol = [t]

		while t<tfinal1:
			for i in range(Nodos):
				if i==0:
					Tdt[i]=T1
				elif i == Nodos-1:
					Tdt[i]=T2
				else:
					Tdt[i]=((k*dt/dx**2)*Tinic1[i-1] + (1-2*k*dt/dx**2)*Tinic1[i] + (k*dt/dx**2)*Tinic1[i+1])
			Tinic1 = Tdt.copy()
			t = t + dt
			print(Tinic1)
			Tsol.append(Tinic1)
			tsol.append(t)

		Tsol = np.array(Tsol)
		tsol = np.array(tsol)
		#Se realizan las graficas
		fig = plt.figure()
		ax = plt.gca()
		plt.scatter(x, barra, s = 500, c=[Tsol[0][j] for j in range(len(Tsol[i]))],vmin= min([float(i) for i in Tinic.get().split(",")]), vmax=Tmax, cmap='inferno')
		cbar = plt.colorbar()
		cbar.set_label('Temperatura [°C]')
		plt.xlim(-0.1, L+0.1)
		plt.ylim(T2)

		def act(i):
			ax.clear()
			plt.scatter(x, barra, s = 500, c=[Tsol[i][j] for j in range(Nodos)], vmin= min([float(i) for i in Tinic.get().split(",")]), vmax=Tmax, cmap='inferno')
			plt.xlabel('Distancia [m]')
			plt.ylabel('Barra')
			plt.title('Tiempo: ' + str(format(tsol[i],'.5f') + 'segundos'))
			plt.xlim(-0.1, L+0.1)
			plt.ylim(0, 2)

		ani = animation.FuncAnimation(fig, act, range(len(tsol)))
		plt.show()
	#Termina funcion asignada al boton "Simulacion" en la interfaz gráfica
	###############################################################################################################################



	###############################################################################################################################
	#Comienza funcion asingada al boton "Calcular y generar gráfica" en la interfaz gráfica

	def calcGraf():
		#Lecura de datos
		L = float(Long.get())
		T1 = float(TA.get())
		T2 = float(TB.get())
		k = float(kt.get())
		Nodos = int(N.get())
		tfinal1 = float(tfinal.get())
		Tinic1 = [float(i) for i in Tinic.get().split(",")]

		#Generamos un vector para ajustar el eje Y a la hora de hacer la simulación
		yAdjust=[]
		for i in Tinic1:
			yAdjust.append(i)

		yAdjust.append(T1)
		yAdjust.append(T2)

	    #Establecemos las condiciones de frontera
		Tinic1[0] = T1
		Tinic1[-1] = T2
		print(Tinic1)
		Tinic1 = np.array(Tinic1)
		x = np.linspace(0,L,Nodos)
		barra = np.ones(len(x))
		dx = L/(Nodos-1)
		t = 0.0
		dt = (dx**2/(2*k))/1.001

		Tdt=Tinic1.copy()
		Tsol = [Tinic1]
		tsol = [t]

		while t<tfinal1:
			for i in range(Nodos):
				if i==0:
					Tdt[i]=T1
				elif i == Nodos-1:
					Tdt[i]=T2
				else:
					Tdt[i]=((k*dt/dx**2)*Tinic1[i-1] + (1-2*k*dt/dx**2)*Tinic1[i] + (k*dt/dx**2)*Tinic1[i+1])
			Tinic1 = Tdt.copy()
			t = t + dt
			print(Tinic1)
			Tsol.append(Tinic1)
			tsol.append(t)



		Tsol = np.array(Tsol)
		tsol = np.array(tsol)

		fig = plt.figure()
		ax = plt.gca()

		def act(i):
			ax.clear()
			plt.plot(x, Tsol[i], 'o')
			plt.title('Tiempo: ' + str(format(tsol[i],'.5f'))+" segundos")
			plt.ylabel('Temperatura [°C]')
			plt.xlabel('Distancia [m]')
			plt.xlim(0, L+.01)
			plt.ylim(min(yAdjust)+.1*min(yAdjust), max(yAdjust)+.1*max(yAdjust))
		ani = animation.FuncAnimation(fig, act, range(len(tsol)))
		plt.show()

	##############################################################################################################################
	#Termina funcion asingada al boton "Simulacion" en la interfaz gráfica


	##############################################################################################################################
	#Comienza el diseño y la funcionalidad 
	root = Tk()
	root.geometry("320x200")
	root.title("Conducción de calor No Estacionaria 1D")

	l1 = Label(root, text='Longitud del conductor: ')
	l2 = Label(root, text='Temperatura frontera A: ')
	l3 = Label(root, text='Temperatura frontera B: ')
	l4 = Label(root, text='Condcuctividad térmica: ')
	l5 = Label(root, text='Tiempo total: ')
	l6 = Label(root, text='Numero de nodos: ')
	l7 = Label(root, text='Temperatura Inicial en los nodos: ')

	Long = Entry(root)
	Long.insert(0, '0.5')

	TA = Entry(root)
	TA.insert(0, '100')

	TB = Entry(root)
	TB.insert(0, '500')

	kt = Entry(root)
	kt.insert(0, '1')

	tfinal = Entry(root)
	tfinal.insert(0, '1')

	N = Entry(root)
	N.insert(0, '6')

	Tinic = Entry(root)
	Tinic.insert(0, '0,0,0,0,0,0')


	btn = Button(root, text='Calcular y generar grafica', command = calcGraf)
	btn2 = Button(root, text='Generar simulación', command = calcSimul)

	l1.grid(row=0)
	l2.grid(row=1)
	l3.grid(row=2)
	l4.grid(row=3)
	l5.grid(row=4)
	l6.grid(row=5)
	l7.grid(row=6)

	Long.grid(row=0, column=1)
	TA.grid(row=1, column=1)
	TB.grid(row=2, column=1)
	kt.grid(row=3, column=1)
	tfinal.grid(row=4, column=1)
	N.grid(row=5, column=1)
	Tinic.grid(row=6, column=1)


	btn.grid(row = 15, columnspan=2)
	btn2.grid(row = 16, columnspan=2)

	root.mainloop()

#Comienza el diseño y la funcionalidad
##############################################################################################################################