#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 13:21:50 2018

@author: luiggi
"""
import numpy as np
from pandas import DataFrame
from Mesh2D import Mesh2D
from Coefficients2D import Coefficients2D
from Diffusion2D import Diffusion2D
from Advection2D import Advection2D
from Temporal2D import Temporal2D
from Matrix2D import Matrix2D
import time

def crono(f):
 	"""
 	Regresa el tiempo que toma en ejecutarse la funcion.
 	"""
 	def eTime(A,b):
 		t1 = time.time()
 		f(A,b)
 		t2 = time.time()
 		return 'Elapsed time: ' + str((t2 - t1)) + "\n"
 	return eTime

def decorate(f):
    def nicePrint(**kargs):
        line = '-' * 70
        print('.'+ line + '.')
        print('|{:^70}|'.format('NoNacos : Numerical Objects for Natural Convection Systems'))
        print('.'+ line + '.')
        print('|{:^70}|'.format(' Ver. 0.1, Author LMCS, 2018, [GNU GPL License V3]'))
        print('.'+ line + '.')
        f(**kargs)
        print('.'+ line + '.')
    return nicePrint
 
@decorate
def printData(**kargs):
    for (key,value) in kargs.items():
        if (type(value) == str):
            print('|{:^70}|'.format('{0:>15s} = {1:11s}'.format(key, value)))
        elif (type(value) == int):
            print('|{:^70}|'.format('{0:>15s} = {1:<11d}'.format(key, value)))            
        else:
            print('|{:^70}|'.format('{0:>15s} = {1:10.5e}'.format(key, value)))

def printFrame(d):
    # Calculo el error porcentual y agrego al DataFrame
    # una columna con esos datos llamada 'Error %'
    d['Error %'] = d['Error'] / d['Analytic'] 
    print(DataFrame(d))
    print('.'+ '-'*70 + '.')

def calcError(phiA, phiN):
    return np.absolute(phiA - phiN)
        
if __name__ == '__main__':
 
    m = Mesh2D(nx = 5, ny = 5, lenx = 10, leny = 10)
    vol = m.volumes()
    dell = m.delta()
    lenn = m.length()
    coef1 = Coefficients2D(vol[0], vol[1], dell[0], dell[1])
    #print(coef1.Vol())
    coef1.alloc()
    d = Diffusion2D(vol[0], vol[1], 1, dell[0], dell[1])
    d.calcCoef()
    ma = Matrix2D(vol[0], vol[1])
    #Aux = ma.build()
    #a = Advection1D(m.volumes())
    #t = Temporal1D(m.volumes()) 

    #print(vol[0], vol[1], dell[0], dell[1])
    #print(lenn)
    print(m.delta(), d.aP(), sep='\n')
    #print(m.delta(), d.aP(), '''a.aP()''', '''t.aP(), Aux''', sep='\n')

    printData(Name='Laplace', nvx = 5, nx = 6, longitud = 1.3)
    
