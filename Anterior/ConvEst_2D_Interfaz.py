#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 00:12:09 2021

@author: alejandro
"""
from scipy import special
import Funciones_No_estacionario as fun
import time
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('seaborn-darkgrid')

#Datos iniciales :
#Obtención de condiciones de frontera:
a=0
b=1
c=0
d=1
Nx=4

"""
#Nx = int(input("Ingresa el número de nodos que desea            N= "))
#Ny = int(input("Ingresa el número de nodos que desea en y            Ny= "))
Ta = float(input("Ingrese la temperaruta en el lado a.               Ta= "))
Tb = float(input("Ingrese la temperaruta en el lado b.                Tb= "))
Tc = float(input("Ingrese la temperaruta en el lado c.                Tc= "))
Td = float(input("Ingrese la temperaruta en el lado d.                Td= "))
kx = float(input("Ingrese la conductividad térmica.               k= "))
#ky = float(input("Ingrese la conductividad térmica en y.               ky= "))
S = float(input("Ingrese las fuentes o sumideros.                S= "))

#rhoy = float(input('Ingrese la densidad de y.                    rhoy=  '))
vx = float(input("Ingrese la velocidad.                v= "))
#vy = float(input("Ingrese la velocidad en y.                vy= "))
Tol = float(input("Ingrese la Tolerancia.                Tol= "))
"""

Ta=100
Tb=200
Tc=100
Td=200 
kx=1000
S=0
vx=1000
rhox = float(input('Ingrese la densidad.                    rho=  '))
Ny=Nx
ky=kx
rhoy=rhox
vy=vx

#Datos constantes:
hx=abs((b-a))/(Nx+1)
hy=abs((d-c))/(Ny+1)
Ma=-(((2*kx)/(hx*hx))+((2*ky)/(hy*hy)))
rx=kx/hx*hx
px=(rhox*vx)/(2*hx)
ry=ky/hy*hy
py=(rhoy*vy)/(2*hy)
Mb=-px+rx
Mc=px+rx
Md=-py+rx
Me=py+ry


f=np.zeros((Nx,Ny))
u=np.zeros((Nx+2,Ny+2))
u[-1,:]=Tc
u[0,:]=Td
u[:,0]=Ta
u[:,-1]=Tb

f[-1,:]=Me * Td
f[0,:]=Md * Tc
f[:,0]=Mc * Ta
f[:,-1]=Mb * Tb

print(f)
print(u)

#Construcción del vector b:

#Construcción de la matriz A:
N = Nx * Ny

A = np.zeros((N,N))
# Primero llena los bloques tridiagonales
for j in range(0,Ny):
	ofs = Nx * j
	A[ofs, ofs] = 1-Ma; 
	A[ofs, ofs + 1] = Mb
	for i in range(1,Nx-1):
		A[ofs + i, ofs + i]     = 1-Ma
		A[ofs + i, ofs + i + 1] = Mb
		A[ofs + i, ofs + i - 1] = -Mc
	A[ofs + Nx - 1, ofs + Nx - 2] = -Mc; 
	A[ofs + Nx - 1, ofs + Nx - 1] = 1-Ma 

# Despues llena las dos diagonales externas
for k in range(0,N-Nx):
	A[k, Nx + k] =  -Md
	A[Nx + k, k] = -Me
print (A)

#Resolución del sistema:
ut=np.copy(u[1:N+1,1:N+1])

ut.shape=ut.size
f.shape=f.size
ut= np.linalg.solve(A,f)
print(ut)

#Gráfica:
nx, ny = (Nx, Ny) 
ut.shape = (nx, ny)
u[1:Nx+1,1:Ny+1]=ut
print (u)
x= np.linspace(0,1,nx+2)
y= np.linspace(0,1,ny+2)
xv, yv = np.meshgrid(x,y)
h=plt.contourf(xv, yv, u, cmap="inferno") 
fig=plt.gcf()
fig.colorbar(h)
plt.show()
#Guardado de datos
"""
def WinConveccionEst2D():
    def CalcConv():
		# Programa principal
        N = int(a1.get())
		#b = float(b1.get())
        #N = int(N1.get())
        Ta = float(Ta1.get())
        Tb = float(Tb1.get())
        Tc = float(Tc1.get())
        Td = float(Td1.get())
        k = float(k1.get())
        u = float(u1.get())
        p = float(p1.get())
        S = float(S1.get())



        A = fun.Matriz_Diagonal_Cond_est_2D(N)
        A[N**2-1,N**2-1]=-4

        b = fun.Vector_aux_cond_Est_2D(Ta,Tb,Tc,Td,N)

        u= fun.Sol_Sitema(A,b,N,Ta,Tb,Tc)

        f = np.copy(u[0:-1])

        nx, ny = (N, N) 
        f.shape = (nx, ny)
        np.linspace(0,1,nx)
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
    l6 = Label(root, text='Conductividad térmica: ')
    l7 = Label(root, text='Fuentes o sumideros: ')
    l8 = label(root, text='Velocidad de conveccion: ')

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

    k1 = Entry(root)
    k1.insert(0, '5')

    S1 = Entry(root)
    S1.insert(0, '1')


    btn = Button(root, text='Calcular y generar grafica', command = CalcCond)

    l1.grid(row=0)
    l2.grid(row=3)
    l3.grid(row=4)
    l4.grid(row=5)
    l5.grid(row=6)
    l6.grid(row=5)
    l7.grid(row=6)

    #a1.grid(row=0, column=1)
    #b1.grid(row=1, column=1)
    N1.grid(row=2, column=1)
    Ta1.grid(row=3, column=1)
    Tb1.grid(row=4, column=1)
    Tc1.grid(row=5, column=1)
    Td1.grid(row=6, column=1)
    
    k1.grid(row=5, column=1)
    S1.grid(row=6, column=1)

    btn.grid(row = 15, columnspan=2)

    root.mainloop()

	#Comienza el diseño y la funcionalidad
	##############################################################################################################################
"""
