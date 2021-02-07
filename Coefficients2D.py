#Esta celda es de prueba ggg
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:11:05 2018

@author: luiggi
"""

import numpy as np
#Las lineas comentadas son cosas que creo que estarían bien
class Coefficients2D():
    """
    Esta clase define los arreglos principales para los coeficientes del
    metodo de Volumen Finito. Los arreglos son definidos como variables de
    clase para que sean compartidos por todos los objetos de esta clase.
    """    
    __aP = None 
    __aE = None
    __aW = None
    __aN = None
    __aS = None
    __Su = None
    __nvx = None
    __deltax = None
    __nvy = None
    __deltay = None
    #__Nx = None
    #__Ny = None
  
    def __init__(self, nvx = None, nvy = None, deltax = None, deltay = None):
        Coefficients2D.__nvx = nvx
        Coefficients2D.__nvy = nvy
        #Coefficients2D.__Nx = Nx
        #Coefficients2D.__Ny = Ny
        Coefficients2D.__deltax = deltax
        Coefficients2D.__deltay = deltay

    @staticmethod
    def alloc():
        nvx = Coefficients2D.__nvx
        nvy = Coefficients2D.__nvy
        Coefficients2D.__aP = np.zeros((nvx,nvy))
        Coefficients2D.__aE = np.zeros((nvx,nvy))
        Coefficients2D.__aW = np.zeros((nvx,nvy))
        Coefficients2D.__aN = np.zeros((nvx,nvy))
        Coefficients2D.__aS = np.zeros((nvx,nvy))
        Coefficients2D.__Su = np.zeros((nvx,nvy))

    def setVolumes(self, nvx, nvy):
        Coefficients2D.__nvx = nvx
        Coefficients2D.__nvy = nvy
        
    def setDelta(self, deltax, deltay):
        Coefficients2D.__deltax = deltax
        Coefficients2D.__deltay = deltay
    
    #def setNodes(self, Nx, Ny):
    #    Coefficients2D.__Nx = Nx
    #    Coefficients2D.__Ny = Ny
        
    def aP(self):
        return Coefficients2D.__aP

    def aE(self):
        return Coefficients2D.__aE
    
    def aS(self):
        return Coefficients2D.__aS
    
    def aN(self):
        return Coefficients2D.__aN

    def aW(self):
        return Coefficients2D.__aW
    
    def Su(self):
        return Coefficients2D.__Su



    @staticmethod
    def bcDirichlet(wall, phi):
        aP = Coefficients2D.__aP
        aE = Coefficients2D.__aE
        aW = Coefficients2D.__aW
        aN = Coefficients2D.__aN
        aS = Coefficients2D.__aS
        Su = Coefficients2D.__Su

        if wall == 'LEFT_WALL':
            aP[:,0] += aW[:,0]
            Su[:,0] += 2 * aW[:,0] * phi
        elif wall == 'RIGHT_WALL':
            aP[:,-1] += aE[:,-1]
            Su[:,-1] += 2 * aE[:,-1] * phi
        elif wall == 'TOP_WALL':
            aP[0,:] += aN[0,:]
            Su[0,:] += 2 * aN[0,:] * phi
        elif wall == 'DOWN_WALL':
            aP[-1,:] += aS[-1,:]
            Su[-1,:] += 2 * aS[-1,:] * phi

    @staticmethod
    def bcNeumman(wall, flux):
        aP = Coefficients2D.__aP
        aE = Coefficients2D.__aE
        aW = Coefficients2D.__aW
        aN = Coefficients2D.__aN
        aS = Coefficients2D.__aS
        Su = Coefficients2D.__Su
        dx = Coefficients2D.__deltax
        dy = Coefficients2D.__deltay

        if wall == 'LEFT_WALL':
            aP[:,0] -= aW[:,0]
            Su[:,0] -= aW[:,0] * flux * dx
        elif wall == 'RIGHT_WALL':
            aP[:,-1] -= aE[:,-1]
            Su[:,-1] -= aE[:,-1] * flux * dx
        elif wall == 'TOP_WALL':
            aP[0,:] -= aN[0,:]
            Su[0,:] -= aN[0,:] * flux * dy
        elif wall == 'DOWN_WALL':
            aP[-1,:] -= aS[-1,:]
            Su[-1,:] -= aS[-1,:] * flux * dy

          
            
    def setSu(self, q): #¿Como afecta que esto sea en dos dimensiones?
        Su = Coefficients2D.__Su
        dx = Coefficients2D.__deltax
        dy = Coefficients2D.__deltay
        Su += q * dx * dy
        
    def setSp(self, Sp): #¿De donde viene y para que? 
        aP = Coefficients2D.__aP
        dx = Coefficients2D.__deltax
        dy = Coefficients2D.__deltay
        aP -= Sp * dx
        
    def printCoefficients(self):
        print('aP = {}'.format(self.__aP), 
              'aE = {}'.format(self.__aE), 
              'aW = {}'.format(self.__aW),
              'aN = {}'.format(self.__aN),
              'aS = {}'.format(self.__aS),
              'Su = {}'.format(self.__Su), sep='\n')

    def cleanCoefficients(self):
        Coefficients2D.__aP[:] = 0.0
        Coefficients2D.__aE[:] = 0.0
        Coefficients2D.__aW[:] = 0.0
        Coefficients2D.__aN[:] = 0.0
        Coefficients2D.__aS[:] = 0.0
        Coefficients2D.__Su[:] = 0.0

if __name__ == '__main__':
    
    coef1 = Coefficients2D(5,5,0.25, 0.25)
    coef1.alloc()
    coef1.setSu(1)
    coef1.setSp(1)
    
    #print('-' * 20)  
    #print(coef1.aP(), coef1.aE(), coef1.aW(), coef1.aN(),coef1.aS(), coef1.Su(), sep = '\n')
    #print('-' * 20)  

    ap = coef1.aP()
    #ap[2] = 25
    #print(ap, coef1.aP(),sep='\n')
    #print('-' * 20)  

    ae = coef1.aE()
    aw = coef1.aW()
    an = coef1.aN()
    asur = coef1.aS()
    su = coef1.Su()
    ae.fill(1)
    aw.fill(1)
    an.fill(1)
    asur.fill(1)
    ap.fill(1)
    coef1.setSp(1)
    #coef1.bcDirichlet('LEFT_WALL', 2)
    #coef1.bcDirichlet('RIGHT_WALL', 2)
    #coef1.bcDirichlet('TOP_WALL', 2)
    #coef1.bcDirichlet('DOWN_WALL', 2)
    
    coef1.bcNeumman('RIGHT_WALL', 1)
    coef1.bcNeumman('LEFT_WALL', 1)
    coef1.bcNeumman('TOP_WALL', 1)
    coef1.bcNeumman('DOWN_WALL', 1)

    coef1.printCoefficients()
    #print(coef1.aP(), coef1.aE(), coef1.aW(), coef1.aN(),coef1.aS(), coef1.Su(), sep = '\n')
    print('-' * 20)
    print(coef1.Nx())