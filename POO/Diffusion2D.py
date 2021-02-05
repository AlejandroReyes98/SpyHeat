class Diffusion2D(Coefficients):
    
    def __init__(self, nvx = None, nvy = None, Gamma = None, dx = None, dy = None):
        super().__init__(nvx, nvy, dx, dy)
        self.__nvx = nvx
        self.__nvy = nvy
        self.__Gamma = Gamma
        self.__dx = dx
        self.__dy = dy

    def __del__(self):
        del(self.__Gamma)
        del(self.__dx)
        del(self.__dy)
    
    def calcCoef(self):
        aE = self.aE()
        aW = self.aW()
        aP = self.aP()
        aS = self.aS()
        aN = self.aN()
        
        aE += self.__Gamma * self.__dy / self.__dx
        aW += self.__Gamma * self.__dy / self.__dx
        aS += self.__Gamma * self.__dx / self.__dy
        aN += self.__Gamma * self.__dx/ self.__dy
        aP += aE + aW + aS + aN
 
#        for i in range(self.__nvx):
#            aE[i] += self.__Gamma / self.__dx
#            aW[i] += self.__Gamma / self.__dx
#            aP[i] += aE[i] + aW[i]

if __name__ == '__main__':
    
    df1 = Diffusion2D(5, 5, 1, 6, 6)
    df1.alloc()
    df1.calcCoef()
    df1.setSu(10)

    #print('-' * 20)  
    #print(df1.aP(), df1.aE(), df1.aW(), df1.Su(), df1.aS(), df1.aN(), sep = '\n')
    #print('-' * 20)  

    df1.bcDirichlet('LEFT_WALL', 2)
    df1.bcDirichlet('RIGHT_WALL', 2)
    df1.bcDirichlet('TOP_WALL', 2)
    df1.bcDirichlet('DOWN_WALL', 2)

    #df1.bcNeumman('RIGHT_WALL', 1)
    #df1.bcNeumman('LEFT_WALL', 1)
    #df1.bcNeumman('TOP_WALL', 1)
    #df1.bcNeumman('DOWN_WALL', 1)
    print(df1.aP(), df1.aE(), df1.aW(), df1.Su(), df1.aS(), df1.aN(), sep = '\n')
    print('-' * 20)  

