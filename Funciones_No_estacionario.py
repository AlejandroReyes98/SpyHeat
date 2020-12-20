# PROGRAMA QUE CONTIENE LAS FUNCIONES PARA EL CÁLCULO DE LA SOLUCIÓN
# DE LA ECUACIÓN DE CALOR EN ESTADO NO ESTACIONARIO Y CONSIDERANDO EL 
# TÉRMINO CONVECTIVO

import numpy as np
import matplotlib.pyplot as plt
import pandas as ps
plt.style.use('Solarize_Light2')
from scipy import special

def Ingreso(sel,Titulo):
    """
    Esta función permite seleccionar al usuario la manera 
    en la que se ingresarán los datos

    Parameters
    ----------
    sel : Integer
        Valor de selección ingresado por el usuario

    Returns
    -------
    a : float
        Valor al inicio del dominio.
    b : float
        Valor al final del dominio.
    N : Integer
        Número de nodos
    Ta : float
        Temperatura en la frontera del inicio.
    Tb : float
        Temperatura en la frontera del final.
    S : float
        Valor de la fuente
    k : float
        Valor de la conductividad térmica
    ht : float
        Tamaño de paso en el tiempo
    Tmax: float
        Tiempo máximo hasta el cual calculamos la solución
    v : floar
        Velocidad del fluido en movimiento
    Tol : float
        Tolerancia del algoritmo
        

    """
    if sel == 1:
        val= np.loadtxt(Titulo)
        a = val[0]
        b = val[1]
        N = int(val[2])
        Ta = val[3]
        Tb = val[4]
        k = val[5]
        S = val[6]
        ht = val[7]
        Tmax = val[8]
        v = val[9]
        Tol = val[10]
       
        return a,b,N,Ta,Tb,k,S,ht,Tmax,v,Tol
    else:    
        # Datos de entrada
        a = float(input("Ingrese el comienzo de la barra.                a="))
        b = float(input("Ingrese el fin de la barra.                     b="))
        N = int(input("Ingresa el número de nodos que desea            N="))
        Ta = float(input("Ingrese la temperaruta al inicio.               Ta="))
        Tb = float(input("Ingrese la temperaruta al final.                Tb="))
        k = float(input("Ingrese la conductividad térmica.               k="))
        S = float(input("Ingrese las fuentes o sumideros.                S="))
        ht = float(input("Ingrese el paso del tiempo.                     ht="))
        Tmax= float(input("Ingrese el tiempo maximo.                       Tmax="))
        v = float(input("Ingrese la velocidad.                           v="))
        Tol = float(input("Ingrese la Tolerancia.                          Tol="))
        return a,b,N,Ta,Tb,k,S, ht, Tmax,v,Tol

def Constantes(a,b,N,ht,Tmax,K,v):
    """
    Esta función calcula las constantes que requiere el programa

    Parameters
    ----------
    a : float
        Valor al inicio del dominio.
    b : float
        Valor al final del dominio.
    N : Integer
        Número de nodos.
    ht : float
         Paso en el tiempo
    k : float
        Valor de la conductividad térmica
    Tmax: float
        Tiempo máximo hasta el cual calculamos la solución
    v : floar
        Velocidad del fluido en movimiento
         

    Returns
    -------
    h : float
        Distancia entre cada nodo
    x : float
        Vector con el cual se graficará
    lar : float
        Distancia total del dominio
    Nt: Int
        Número de nodos en el tiempo
    r : float
    p : float

    """
#    v = float(v)
    h = (b-a)/(N+1)
    x = np.linspace(a,b,N+2)
    lar = b-a
    Nt = int(Tmax / ht)
    r = ht * K / (h*h)
    p = ht *  v / (2*h)
    return h,x,lar,Nt,r, p

def Dominio(a,b,N):
    """
    Esta función genera la malla del dominio.

    Parameters
    ----------
    a : Float
        Incio del dominio.
    b : Float
        Fin del dominio.
    N : Int
        Numero de nodos.

    Returns
    -------
    x : float
        Vector de la malla del dominio.

    """
    x = np.linspace(a,b,N+2)
    return x

def Vector_aux(Ta,Tb,N,q):
    """
    Esta función genera un vector el cual se utiliza en la resolución del 
    problema.

    Parameters
    ----------
    Ta : float
        Temperatura en la frontera del inicio.
    Tb : float
        Temperatura en la frontera del final.
    N : Integer
        Número de nodos.
    q : float
        Vector con la información de las fuentes
    Returns
    -------
    b : float
        Vector con las condiciones a la frontera

    """
    b = np.zeros(N+2)
    b[0] = Ta
    b[-1] = Tb
    return b + q


def Matriz_Diagonal_Conv_Noest(N,r,p):
    """
    Esta función genera la matriz diagonal necesaria en la resolución del 
    problema.    

    Parameters
    ----------
    N : Integer
        Número de nodos.
    r : Float
        Valor en la diagonal
    p : Float
        Valor en la diagonal

    Returns
    -------
    A : float
        Matriz diagonal

    """
    A = np.zeros((N,N))
    
    A[0,0] = 1 + (2 * r); 
    A[0,1] = p-r
    for i in range(1,N-1):
        A[i,i] = 1 + (2 * r) 
        A[i,i+1] = p-r
        A[i,i-1] = -(p+r)
    A[N-1,N-2] = -(p+r); 
    A[N-1,N-1] = 1 + (2 * r)
    return A



def Sol_Sitema(A,b,N,Ta,Tb):
    """
    Esta función resuelve el sistema matricial para el problema

    Parameters
    ----------
    A : float
        Matriz diagonal
    b : float
        Vector con las condiciones a la frontera
    N : Integer
        Número de nodos.
    Ta : float
        Temperatura en la frontera del inicio.
    Tb : float
        Temperatura en la frontera del final.

    Returns
    -------
    u : float
        Vector que contiene las soluciones del problema
    """
    u = np.zeros(N+2)
    u[1:-1] = np.linalg.solve(A,b)
    u[0] = Ta
    u[-1] = Tb
    return u

def Graficas(xa,ua,Titulo):
    """
    Esta función genera las gráficas de la solución analítica y numérica

    Parameters
    ----------
    x : float
        Vector con el cual se graficará
    u : float
        Vector que contiene la solución numérica del problema
    u_exa : float
        Vector que contiene la solución analítica del problema

    Returns
    -------
    Grafica de la solución.

    """
    
    plt.plot(xa,ua, 'k-', lw=2.5, label='Solución Analítica')
    plt.xlabel('$x$')
    plt.ylabel('$u(x)$')
    plt.title(Titulo)
    plt.grid(color = 'w')
    plt.legend()
    plt.show()
    
def Graficas_Error(Error):
    """
    Esta función grafica el error calculado.

    Parameters
    ----------
    Error : float
        Vector que contiene el error de la solución.

    Returns
    -------
    None.

    """
    plt.plot(Error)
    plt.title('Error en la solución')
    plt.yscale('log')
    plt.xlabel('$n$')
    plt.ylabel('$RMS$')
    plt.grid(color = 'w')
    plt.title('')
    plt.show()
    

    
def Sol_Analitica(a,b,K,Tmax,N,v):  
    """
    Esta función genera un vector que contiene la solución exacta al problema.

    Parameters
    ----------
    a : float
        Valor al inicio del dominio.
    b : float
        Valor al final del dominio.
    N : Integer
        Número de nodos.
    k : float
        Valor de la conductividad térmica
    Tmax: float
        Tiempo máximo hasta el cual calculamos la solución
    v : floar
        Velocidad del fluido en movimiento
         
    Returns
    -------
    xa : float.
        Malla del dominio sin incluir las fronteras.
    ua : float.
        Solución exacta al problema.

    """
    xa = np.linspace(a, b, N)
    
    divisor = 2 * np.sqrt(K * Tmax)
    ua = 0.5 * (special.erfc((xa - v * Tmax)/ divisor) + 
                np.exp(v * xa) * np.exp(-K) * special.erfc((xa + v * Tmax)/divisor))
    return (xa, ua)
    
def Escritura(u,u_exa):
    """
    Esta función genera un archivo .txt de dos columnas con los datos de
    las soluciones numérica y analítica
    Parameters
    ----------
    u : float
        Vector que contiene la solución numérica del problema
    u_exa : float
        Vector que contiene la solución analítica del problema

    Returns
    -------
    Archivo.
    """
    
    serie1 = ps.Series(u)
    serie2 = ps.Series(u_exa)
    tabla = ps.DataFrame(serie1,columns = ['Solución analítica'])
    tabla['Solución numérica'] = serie2
    np.savetxt('Solución1.txt',tabla,fmt='%f', header = 'Sol. Analítica    Sol. Exacta')
    
    
