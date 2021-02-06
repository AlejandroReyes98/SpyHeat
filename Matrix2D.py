#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 18:15:28 2018

@author: luiggi
"""
import numpy as np

class Matrix2D():
    
    def __init__(self, nvx = None, nvy = None):
        self.__Nx = nvx - 2 
        self.__Ny = nvy - 2 
        self.__A = np.eye(self.__Nx*self.__Ny)

    def __del__(self):
        del(self.__Nx)
        del(self.__Ny)
        del(self.__A)
        
    def mat(self):
        return self.__A
    
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
        A[0][0] = aP[1][1]
        A[0][1] = -aE[1][1]
        A[0][4] = aN[1][1]
        A[4][0] = aS[1][1]  # ¿Por qué el renglón 1?
        for i in range(1,self.__Nx-1): # range(1,N-3)  <-- (1,2)
            A[i][i] = aP[i+1][1]
            # for 
                A[i][i+1] = -aE[i+1][1]  # ¿Por qué los signos?
                A[i][i-1] = -aW[i+1][1]
            # for 
                A[i][i+4] = aN[i+1][1]
                A[i+4][i] = aS[i+1][1]
                #A[i+6][i+2] = aS[i+1][1]
                #A[i+8][i+4] = aS[i+1][1]
                #A[i+10][i+6] = aS[i+1][1]
                #A[i+12][i+8] = aS[i+1][1]
        A[-1][-1] = aP[-2][-2]
        A[-1][-2] = -aW[-2][-2]
        A[-5][-1] = aN[-2][-2]  # ¿Por qué es -2?
        A[-1][-5] = aS[-2][-2]

if __name__ == '__main__':

    a = Matrix2D(6,6)
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
    
    a.build(df1)
    print(a.mat())
    print('-' * 20)  
