#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:32:38 2018

@author: luiggi

Example 4.1 from Malalasekera Book
----------------------------------
Consider the problem of source-free heat conduction in an insulated rod
whose ends are maintained at constant temperatures of 100°C and 500°C
respectively. The one-dimensional problem sketched in Figure 4.3 is governed
by
$
\dfrac{d}{dx} \left( k \dfrac{d T}{dx} \right) = 0
$

___________________________________________________________

 |<-------------- 0.5 m ------------->|
 A                                    B
 |====================================|
 |                                    |
 |====================================|
T_A = 100                            T_B = 500
___________________________________________________________
Figure 4.3

Calculate the steady state temperature distribution in the rod. Thermal conductivity
k equals 1000 W/m.K, cross-sectional area A is 10 × 10−3 m2.

Analytical solution:
    
T = 800 * x + 100
"""

import FiniteVolumeMethod as fvm
import numpy as np
import matplotlib.pyplot as plt
import time

longitud = 0.5 # meters
TI = 100 # °C 
TD = 100 # °C
TA = 100 # °C 
TB = 100 # °C 
k  = 1000 # W/m.K
N  = 4 # Número de nodos
#
# Creamos la malla y obtenemos datos importantes
#
malla = fvm.Mesh2D(nx = N, ny = N, lenx = longitud, leny = longitud)
nx, ny    = malla.nodes()     # Número de nodos
nvx, nvy   = malla.volumes()
print(nvx,nvy)   # Número de volúmenes
deltax, deltay = malla.delta()     # Tamaño de los volúmenes
#
# Imprimimos los datos del problema (nicely)
#
fvm.printData(Longitud = longitud,
              Temperatura_A = TA,
              Temperatura_B = TB,
              Conductividad = k,
              NodosX = nx,
              Nodosy = ny,
              Volumenesx = nvx,
              Volumenesy = nvy,
              Deltax = deltax,
              Deltay = deltay)
#
#  Creamos los coeficientes de FVM
#
df1 = fvm.Diffusion2D(nvx, nvy, Gamma = k, dx = deltax, dy = deltay)
df1.alloc() # Se aloja memoria para los coeficientes
df1.calcCoef()
df1.setSu(0) # Se calculan los coeficientes
#
# Se construye el arreglo donde se guardará la solución
#
T = np.zeros((nvx+2, nvy + 2)) # El arreglo contiene ceros
T[:,0]  = TI        # Condición de frontera izquierda
T[:,-1] = TD
T[0,:]  = TA        # Condición de frontera izquierda
T[-1,:] = TB        # Condición de frontera derecha
df1.bcDirichlet('LEFT_WALL', 100)   # Se actualizan los coeficientes
df1.bcDirichlet('RIGHT_WALL', 100) # de acuerdo a las cond. de frontera
df1.bcDirichlet('TOP_WALL', 100)
df1.bcDirichlet('DOWN_WALL', 100) 
print('aW = {}'.format(df1.aW()), 
      'aE = {}'.format(df1.aE()), 
      'Su = {}'.format(df1.Su()), 
      'aP = {}'.format(df1.aP()), sep='\n')
print('.'+'-'*70+'.')
#
# Se construye el sistema lineal de ecuaciones a partir de los coef. de FVM
#
Su = df1.Su()  # Vector del lado derecho
vol = malla.volumes()
A = fvm.Matrix2D(vol[0], vol[1])  # Matriz del sistema
Aux = A.build(df1) # Construcción de la matriz en la memoria
print('A = ', Aux,
      'b = {}'.format(Su), sep='\n')
print('.'+'-'*70+'.')
#
# Se resuelve el sistema usando un algoritmo del módulo linalg
#
Su.shape = Su.size
Aux3 = np.linalg.solve(Aux,Su)
Aux3.shape = (N+1, N+1)
T[1:N+2,1:N+2] = Aux3
print('Solución = {}'.format(T))
print('.'+'-'*70+'.')
#
# Se construye un vector de coordenadas del dominio
#
plt.imshow(T, cmap='inferno')
plt.colorbar()
plt.show()

x = np.linspace(0,7,7)
fig = plt.figure(1)
ax = plt.axes(projection='3d')
ax.contour3D(x,x,T,100)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
ax.view_init(60, 35)
plt.show()
'''
x = malla.createMesh2D()
#
# Calculamos la solución analítica
#
Ta = 800 * x + 100
#
#  Se grafica la solución
#
x *= 100 # Transformación a [cm]
plt.plot(x,Ta, '-', label = 'Sol. analítica') # Sol. analítica
plt.plot(x,T,'o', label = 'Sol. FVM')
plt.title('Solución de $k (\partial^2 T/\partial x^2) = 0$ con FVM')
plt.xlabel('$x$ [cm]')
plt.ylabel('Temperatura [$^o$C]')
plt.grid()
plt.legend()
plt.savefig('example01.pdf')
plt.show()
'''