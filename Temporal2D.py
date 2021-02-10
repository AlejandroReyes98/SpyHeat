import numpy as np
from Coefficients2D import Coefficients2D

class Temporal2D(Coefficients2D):
    
    def __init__(self, nvx = None, nvy = None, rho = None, dx = None, dy = None, dt = None):
        super().__init__(nvx, nvy, dx, dy)
        self.__nvx = nvx
        self.__nvy = nvy
        self.__rho = rho
        self.__dx = dx
        self.__dy = dy
        self.__dt = dt

    def __del__(self):
        del(self.__nvx)
        del(self.__nvy)
        del(self.__rho)
        del(self.__dx)
        del(self.__dy)
        del(self.__dt)
    
    def deltaT(self):
        return self.__dt

    def calcCoef(self, phi_old):
        aP = self.aP()
        Su = self.Su()
        rho = self.__rho
        dxdy_dt = (self.__dx*self.__dy) / self.__dt
        #dy_dt = self.__dy / self.__dt

        for i in range(self.__nvx):
            for j in range(self.__nvy):
                aP[i,j] += rho * dxdy_dt 
                Su[i,j] += phi_old[i,j] * dxdy_dt

if __name__ == '__main__':
    
    nx = 6
    ny = 6
    phi_oldx = np.sin(np.linspace(0,1,nx))
    phi_oldy = np.sin(np.linspace(0,1,ny))

    phi_old = np.meshgrid(phi_oldx,phi_oldy)
    phi_old2=phi_old[1]+phi_old[0]
    print(phi_old2)

    print('-' * 20)  
#    print(phi_old)
    print('-' * 20)  

    tf1 = Temporal2D(6,6, 1, 1, 1,1)
    tf1.alloc()
    tf1.calcCoef(phi_old2)
    print(tf1.aP())
    print(tf1.Su())
    print('-' * 20)  

#matriz1
#matriz2=matriz1



