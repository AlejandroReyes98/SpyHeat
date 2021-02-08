#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 18:15:28 2018

@author: luiggi
"""
import numpy as np

class Matrix2D():
    
    def __init__(self, nvx = None, nvy = None):
        self.__Nx = nvx  
        self.__Ny = nvy  
        self.__A = np.eye(self.__Nx*self.__Ny)

    def __del__(self):
        del(self.__Nx)
        del(self.__Ny)
        del(self.__A)
        
    def mat(self):
        return self.__A
    
    def nodes(self):
        return self.__Nx, self.__Ny
    
    def build(self, coefficients = None):
# nx = 5, nvx = 6
# 0     1     2     3     4     5  <-- Volumes 
# o--|--x--|--x--|--x--|--x--|--o
#       0     1     2     3        <-- Unknowns    
#
#        0   1   2   3
# --+---------------------
# 0 | [[12. -4.  0.  0.]
# 1 | [ -4.  8. -4.  0.]
# 2 | [  0. -4.  8. -4.]
# 3 | [  0.  0. -4. 12.]]

        aP = coefficients.aP()
        aE = coefficients.aE()
        aW = coefficients.aW()
        aN = coefficients.aN()
        aS = coefficients.aS()
        A = self.__A
        #def Laplaciano2D(Nx, Ny, diagonal): Nodos
        Nx = self.__Nx
        Ny = self.__Ny
        N = Nx*Ny
        A = np.zeros((N,N))

# Primero llena los bloques tridiagonales
        diagonal = aP[1][1]
        for j in range(0,Ny):
            ofs = Nx * j
            A[ofs, ofs] = diagonal; 
            A[ofs, ofs + 1] = -aE[1][1]
            for i in range(1,Nx-1):
                A[ofs + i, ofs + i] = diagonal
                A[ofs + i, ofs + i + 1] = -aE[1][1]
                A[ofs + i, ofs + i - 1] = -aW[1][1]
            A[ofs + Nx - 1, ofs + Nx - 2] = -aE[1][1] 
            A[ofs + Nx - 1, ofs + Nx - 1] = diagonal 

# Despues llena las dos diagonales externas
        for k in range(0,N-Nx):
            A[k, Nx + k] = -aN[1][1]
            A[Nx + k, k] = -aS[1][1]
            
        return A
          

'''
No es posible acceder con el metodo get a la matriz modificada
'''
if __name__ == '__main__':

    a = Matrix2D(5,5) # Pasamos el numero de volumenes
    print('-' * 20)  
    print(a.mat())
    print('-' * 20)  
    
    from Diffusion2D import Diffusion2D        
    df1 = Diffusion2D(6, 6, 1, 0.25, 0.25)
    df1.alloc()
    df1.calcCoef()
    df1.setSu(10)
    print(df1.aP(), df1.aE(), df1.aW(), df1.aN(), df1.aS(), df1.Su(), sep = '\n')
    print('-' * 20)  

    #df1.bcDirichlet('LEFT_WALL', 2)
    #df1.bcDirichlet('RIGHT_WALL', 1)
    #print(df1.aP(), df1.aE(), df1.aW(), df1.Su(), sep = '\n')
    #print('-' * 20)  
    
    A = a.build(df1)
    print(A)
    print('-' * 20)
    print(len(A))
