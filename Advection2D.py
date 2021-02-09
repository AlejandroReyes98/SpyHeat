import numpy as np
from Coefficients2D import Coefficients2D

class Advection2D(Coefficients2D):
    
    def __init__(self, nvx = None, nvy = None, rho = None, dx = None, dy = None):
        super().__init__(nvx, nvy, dx, dy)
        self.__nvx = nvx
        self.__nvy = nvy
        self.__rho = rho
        self.__dx = dx
        self.__dy = dy
        #self.__u = np.zeros((2,nvx,nvy))
        self.__ux = np.ones((nvx+2,nvy+2))
        self.__uy = np.ones((nvx+2,nvy+2))

    def __del__(self):
        del(self.__nvx)
        del(self.__nvy)
        del(self.__rho)
        del(self.__dx)
        del(self.__dy)
        #del(self.__u)
        del(self.__ux)
        del(self.__uy)

    #def setU(self, u):
    #    if type(u) == float:
    #        self.__u.fill(u)
    #    else:
    #        self.__u = u

    def setU(self, ux, uy):
        if type(ux) == float and type(uy) == float:
            self.__ux.fill(ux)
            self.__uy.fill(uy)
        else:
            self.__ux = ux
            self.__uy = uy

    #def u(self):
    #    return self.__u
    def ux(self):
        return self.__ux    
    def uy(self):
        return self.__uy
    
    def calcCoef(self):
        aE = self.aE()
        aW = self.aW()
        aP = self.aP()
        aN = self.aN()
        aS = self.aS()
        #u = self.__u
        ux = self.__ux
        uy = self.__uy
        rho = self.__rho

        for i in range(self.__nvx):
            for j in range(self.__nvy):
                # Diferencias Centrales
                CE = - rho * ux[i,j] * 0.5
                CW =   rho * ux[i-1,j] * 0.5
                CN = - rho * uy[i,j] * 0.5
                CS =   rho * uy[i,j-1] * 0.5
                # Upwind
     #           CE = max((-u[i],0)) 
     #           CW = max((u[i-1],0))
                aE[i,j] += CE 
                aW[i,j] += CW
                aN[i,j] += CN 
                aS[i,j] += CS
                aP[i,j] += CE + CW + CN + CS + rho * (ux[i,j] - ux[-i,j]) + rho * (uy[i,j] - uy[i,-j]) 

if __name__ == '__main__':
    
    nx = 6
    ny = 6
    x = np.linspace(0,1,nx)
    y = np.linspace(0,1,ny)
    X, Y = np.meshgrid(x,y)
    #print(X)
    #print(Y)
    #print('-' * 20)
    u = np.cos((X,Y))
    #print(X)
    #print(Y)
    #print('-' * 20)
    #uy = np.sin((X,Y))
    #print(ux[1])
    #print(uy)

    af1 = Advection2D(nx-1, ny-1, 1, 2, 2)
    af1.alloc()
    af1.setU(u[0], u[1])
    af1.calcCoef()
    af1.setSu(10)
    #print(af1.ux(), af1.uy())
    #af1.calcCoef()
    #print(af1.aP(), af1.aE(), af1.aW(), af1.aN(), af1.aS(), af1.Su(), sep = '\n')
    print('-' * 20)  

    #af1.bcDirichlet('LEFT_WALL', 2)
    #af1.bcDirichlet('RIGHT_WALL', 2)
    #af1.bcDirichlet('TOP_WALL', 2)
    #af1.bcDirichlet('DOWN_WALL', 2)

    #af1.bcNeumman('RIGHT_WALL', 1)
    #af1.bcNeumman('LEFT_WALL', 1)
    #af1.bcNeumman('TOP_WALL', 1)
    #af1.bcNeumman('DOWN_WALL', 1)
    print(af1.aP(), af1.aE(), af1.aW(), af1.aS(), af1.aN(), af1.Su(), sep = '\n')
    #print('-' * 20)  


