#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 13:21:50 2018
@author: luiggi
"""

import numpy as np

class Mesh2D():
    
    def __init__(self, nx = None, volx = None, lenx = None, ny = None, voly = None, leny = None):
        self.__nx = nx
        self.__volx = volx
        self.__lenx = lenx
        self.__ny = ny
        self.__voly = voly
        self.__leny = leny
        self.__delx = 1
        self.__dely = 1
        self.adjustNodesVolumes(nx, ny, volx, voly)
        self.calcDelta()
    
    #def __del__(self):
    #    del(self.__nodes)
    #    del(self.__volumes)
    #    del(self.__length)
    #    del(self.__delta)
        
    def adjustNodesVolumes(self,nx, ny, volx, voly):
        if nx and ny:
            self.__volx = self.__nx + 1
            self.__voly = self.__ny + 1
        if volx and voly:
            self.__nx = self.__volx - 1
            self.__ny = self.__voly - 1
        
    def nodes(self):
        return self.__nx, self.__ny 
    
    def setNodes(self, nx, ny):
        self.__nx = nx
        self.__ny = ny
        self.adjustNodesVolumes(nx = nx, ny = ny, volx = None, voly= None)
        
    def volumes(self):
        return self.__volx, self.__voly

    def setVolumes(self, volx, voly):
        self.__volx = volx
        self.__voly = voly
        self.adjustNodesVolumes(nx = None, ny = None, volx = volx, voly = voly)
        
    def length(self):
        return self.__lenx, self.__leny
        
    def calcDelta(self):
        if self.__lenx and self.__leny:
            self.__delx = self.__lenx / (self.__nx - 1)
            self.__dely = self.__leny / (self.__ny - 1)
        
    def delta(self):
        return self.__delx, self.__dely
    
    def createMesh2D(self):
        first_volumex = self.__delx / 2
        first_volumey = self.__dely / 2
        final_volumex = self.__lenx - first_volumex
        final_volumey = self.__leny - first_volumey
        self.__x = np.zeros(self.__volx)
        self.__y = np.zeros(self.__voly)
        self.__x[1:-1] = np.linspace(first_volumex,final_volumex,self.__volx-2)
        self.__x[-1] = self.__lenx
        self.__y[1:-1] = np.linspace(first_volumey,final_volumey,self.__voly-2)
        self.__y[-1] = self.__leny
        self.__X, self.__Y = np.Mesh2Dgrid(self.__x, self.__y)
        return self.__X, self.__Y
        
if __name__ == '__main__':

    m1 = Mesh2D()
    print(m1.nodes(), m1.volumes())
    print('_' * 20)   
    
    m1 = Mesh2D(nx = 5, ny = 5) # Diferencia entre nodo y volumen
    print(m1.nodes(), m1.volumes())
    print('_' * 20)
    
    m1 = Mesh2D(volx = 5, voly = 5)
    print(m1.nodes(), m1.volumes())
    print('_' * 20)

    m1 = Mesh2D(5,5,5,5)
    print(m1.nodes(), m1.volumes())
    print('_' * 20)
    
    m1.setNodes(8,8)
    print(m1.nodes(), m1.volumes())
    print('_' * 20)
    
    m1.setVolumes(8,8)
    print(m1.nodes(), m1.volumes())
    print('_' * 20)
    
    m1 = Mesh2D(nx =  5, ny = 5, lenx = 33, leny = 33)
    print(m1.nodes(), m1.volumes(), m1.length())
    print('_' * 20)
    
    m1 = Mesh2D(volx =  5, voly = 5, lenx = 33, leny = 33)
    print(m1.nodes(), m1.volumes(), m1.length())
    print('_' * 20)
    
    m1 = Mesh2D(nx = 5, ny = 5, lenx = 1, leny= 1)
    print(m1.nodes(), m1.volumes(), m1.length(), m1.delta())
    print('_' * 20)    
    
    m1 = Mesh2D(volx = 10, voly = 10, lenx = 1, leny = 10)
    print(m1.nodes(), m1.volumes(), m1.length(), m1.delta())
    print('_' * 20) 

    m1 = Mesh2D(volx = 6, voly = 6, lenx = 1, leny = 1)
    print(m1.nodes(), m1.volumes(), m1.length(), m1.delta())
    print(m1.createMesh2D())
    print('_' * 20) 
    

