#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:32:38 2018

@author: luiggi

Example 5.1 from Malalasekera Book
----------------------------------


___________________________________________________________

 |<-------------- 1.0 m ------------->|
                                     
            u ---> 
 |------------------------------------|
                                 
\phi_0 = 1                       \phi_L = 0
___________________________________________________________



"""

import FiniteVolumeMethod as fvm
import numpy as np
import matplotlib.pyplot as plt

def analyticSol(x):
    return (np.exp(rho * u * x / Gamma) - 1) / (np.exp(rho * u * L / Gamma) - 1) * (phiL - phi0) + phi0

L = 1.0 # m
rho = 1.0 # kg/m^3
u = 2.1 # m/s
Gamma = 0.1 # kg / m.s
phi0 = 1 #
phiL = 0 #
N = 20 # Número de nodos
#
# Creamos la malla y obtenemos datos importantes
#
malla = fvm.Mesh2D(nx = N, ny = N, lenx = L, leny = L)
nx, ny    = malla.nodes()     # Número de nodos
nvx, nvy   = malla.volumes()   # Número de volúmenes
deltax, deltay = malla.delta()     # Tamaño de los volúmenes
#
# Imprimimos los datos del problema (nicely)
#
fvm.printData(Longitud = L,
              Densidad = rho,
              Velocidad = u,
              Coef_Diff = Gamma,
              Prop_0 = phi0,
              Prop_L = phiL,
              NodosX = nx,
              Nodosy = ny,
              Volumenesx = nvx,
              Volumenesy = nvy,
              Deltax = deltax,
              Deltay = deltay)
#
# Se aloja memoria para los coeficientes
#
coef = fvm.Coefficients2D(nvx, nvy, deltax, deltay)
coef.alloc()
#fvm.Coefficients.alloc(nvx)
#
#  Calculamos los coeficientes de FVM de la Difusión
#
dif = fvm.Diffusion2D(nvx, nvy, Gamma = Gamma, dx = deltax, dy = deltay)
dif.calcCoef()
#print('aW = {}'.format(dif.aW()), 
#      'aE = {}'.format(dif.aE()), 
#      'Su = {}'.format(dif.Su()), 
#      'aP = {}'.format(dif.aP()), sep='\n')
#print('.'+'-'*70+'.')
#
#  Calculamos los coeficientes de FVM de la Advección
#
adv = fvm.Advection2D(nvx, nvy, rho = rho, dx = deltax, dy = deltay)
vol = malla.volumes()
u = np.array(vol[0],u)
adv.setU(u, u)
adv.calcCoef() 
#print('aW = {}'.format(dif.aW()), 
#      'aE = {}'.format(dif.aE()), 
#      'Su = {}'.format(dif.Su()), 
#      'aP = {}'.format(dif.aP()), sep='\n')
#print('u = {}'.format(adv.u()))
#print('.'+'-'*70+'.')
#
# Se construye el arreglo donde se guardará la solución
#
T = np.zeros((nvx+2, nvy + 2)) # El arreglo contiene ceros
T[:,0]  = phi0       # Condición de frontera izquierda
T[:,-1] = phiL      # Condición de frontera derecha
#
# Se aplican las condiciones de frontera
#
coef.bcDirichlet('LEFT_WALL', phi0/2)   # Se actualizan los coeficientes
coef.bcDirichlet('RIGHT_WALL', phiL/2) # de acuerdo a las cond. de frontera
#print('aW = {}'.format(dif.aW()), 
#      'aE = {}'.format(dif.aE()), 
#      'Su = {}'.format(dif.Su()), 
#      'aP = {}'.format(dif.aP()), sep='\n')
#print('u = {}'.format(adv.u()))
#print('.'+'-'*70+'.')
#
# Se construye el sistema lineal de ecuaciones a partir de los coef. de FVM
#


Su = coef.Su()  # Vector del lado derecho
vol = malla.volumes()
A = fvm.Matrix2D(vol[0], vol[1])  # Matriz del sistema
Aux = A.build(coef)


#Su = coef.Su()  # Vector del lado derecho
#A = fvm.Matrix(malla.volumes())  # Matriz del sistema
#A.build(coef) # Construcción de la matriz en la memoria
#print('A = ', A.mat(),
#      'b = {}'.format(Su[1:-1]), sep='\n')
#print('.'+'-'*70+'.')
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
#phi[1:-1] = np.linalg.solve(A.mat(),Su[1:-1])
#print('Solución = {}'.format(phi))
#print('.'+'-'*70+'.')
#
# Se construye un vector de coordenadas del dominio
#
x = malla.createMesh2D()


f1 = plt.figure()    
c= plt.contourf(x[0], x[1], T, 8, alpha=.75, cmap='inferno')
f1.gca().set_aspect('equal')
f1.colorbar(c, shrink=1.0)

f2 = plt.figure()
ax = f2.gca(projection='3d')    
s = ax.plot_surface(x[0], x[1], T, cmap='inferno')
f2.colorbar(s, shrink=0.5)

plt.show()



#
# Calculamos la solución exacta y el error
#/


'''
phi_a = analyticSol(x)
error = fvm.calcError(phi, phi_a)
datos = {'x(m)': x,
         'phi(x)': phi,
         'Analytic': phi_a,
         'Error': error}
fvm.printFrame(datos)
print('||Error|| = ', np.linalg.norm(error))
print('.'+ '-'*70 + '.')
#
# Calculamos la solución exacta en una malla más fina para graficar
#
x1 = np.linspace(0,L,100)
phi_a = analyticSol(x1)
#
#  Se grafica la solución
#
plt.plot(x1,phi_a, '-', label = 'Sol. analítica') 
plt.plot(x,phi,'--o', label = 'Sol. FVM')
plt.title('Solución de $\partial(p u \phi)/\partial x= \partial (\Gamma \partial\phi/\partial x)/\partial x$ con FVM')
plt.xlabel('$x$ [m]')
plt.ylabel('$\phi$ [...]')
plt.grid()
plt.legend()
plt.savefig('example04.pdf')
plt.show()
'''