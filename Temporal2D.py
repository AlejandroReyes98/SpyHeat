class Temporal2D(Coefficients):
    
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
        dx_dt = self.__dx / self.__dt
        dy_dt = self.__dy / self.__dt

        for i in range(1,self.__nvx-1):
            for j in range(1,self.__nvy-1):
                aP[i,j] += rho * dx_dt 
                Su[i,j] += phi_old[i,j] * dx_dt

if __name__ == '__main__':
    
    nx = 6
    ny = 6
    phi_oldx = np.sin(np.linspace(0,1,nx))
    phi_oldy = np.sin(np.linspace(0,1,ny))
    phi_old = 
    print('-' * 20)  
    print(phi_old)
    print('-' * 20)  

    tf1 = Temporal1D(6, 1, 1, 1)
    tf1.alloc(6)
    tf1.calcCoef(phi_old)
    print(tf1.aP())
    print('-' * 20)  





