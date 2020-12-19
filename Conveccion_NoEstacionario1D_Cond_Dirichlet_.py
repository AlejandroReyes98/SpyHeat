# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 02:45:56 2020

@author: andy_
"""
# PROGRAMA PARA LA SOLUCIÓN DE LA ECUACIÓN DE CALOR, NO estacionario
#incluye termino convección
#(Condiciones tipo Dirichlet)

#Valores
#a=0
#b=2.5
#N=300
#Ta=1
#Tb=0
#K=0.001
#S=0
#ht=0.002
#Tmax1
#v=1
#Tolerancia=1e-6

import Funciones_No_estacionario as fun
import numpy as np
import matplotlib.pyplot as plt
import time

# Programa principal
print()
print("+----------------------------------------------------+")
print("|      Solucion de la transferencia de calor         |")
print("+----------------------------------------------------+")

print('Opciones para la ejecución: \n'
	  '1.- Tomar datos de ejemplo de un archivo \n'
      '2.- Ingresar los datos manualmente.')

sel = int(input('Escoja una opción.\n'))

a,b,N,Ta,Tb,K,S,ht,Tmax,v,Tol = fun.Ingreso(sel,"Datos_Conv_No_EstD.txt")

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

# Este es lado derecho de la ecuación, que contiene la condicion inicial
# es decir la solucion en el paso 0. Por eso hacemos una copia de u.
f = np.copy(u[1:N+1])
uold = np.copy(u)

# Construccion de la matriz
A = fun.Matriz_Diagonal_Conv_Noest(N,r,p)

#Graficación de la condición inicial
plt.plot(x,u,'--k',label='Inicial')

tolerancia=Tol
error = []

#Solución Analítica del problema
xa, ua = fun.Sol_Analitica(a,b,K,Tmax,N,v)

# Ciclo en el tiempo, desde 0 hasta Nt+1
for n in range(1,Nt+1):
    

    f[0] += (p+r)*Ta
    f[N-1] += -(p-r)*Tb
    u[1:N+1] = np.linalg.solve(A,f) # Sol. del sistema lineal
    
    err = np.sqrt(h) * np.linalg.norm(uold-u)
    error.append(err)
    
    #print("n = ", n, ' Error = %12.10g' % err)
    if (n % 100==0):
        etiqueta = 'Sol. Num. steep = {}'.format(n*ht)
        plt.plot(x, u, '.--', label=etiqueta)
        
        
    # Actualizacion de la solucion para dar el siguiente paso
    f = np.copy(u[1:N+1])
    uold = np.copy(u)
    

    if (err < tolerancia):
        break


fun.Graficas(xa,ua,'Solución Analítica y Numérica')
fun.Graficas_Error(error)
