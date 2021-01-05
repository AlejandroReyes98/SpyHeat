# PROGRAMA QUE CONTIENE LAS FUNCIONES PARA EL CÁLCULO DE LA SOLUCIÓN
# DE LA ECUACIÓN DE CALOR

import numpy as np
import matplotlib.pyplot as plt
import pandas as ps
plt.style.use('Solarize_Light2')

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
       
        return a,b,N,Ta,Tb,k,S
    else:    
        # Datos de entrada
        a = float(input("Ingrese el comienzo de la barra.                a="))
        b = float(input("Ingrese el fin de la barra.                     b="))
        N = int(input("Ingresa el número de nodos que desea            N="))
        Ta = float(input("Ingrese la temperaruta al inicio.               Ta="))
        Tb = float(input("Ingrese la temperaruta al final.                Tb="))
        k = float(input("Ingrese la conductividad térmica.               k="))
        S = float(input("Ingrese las funetes o sumideros.                S="))
        
        return a,b,N,Ta,Tb,k,S

def Constantes(a,b,N):
    """
    Esta función calcula las constantes que requiere el programa
    Parameters
    ----------
    a : float
        Valor al inicio del dominio.
    b : float
        Valor al final del dominio.
    N : Integer
        Número de nodos
    Returns
    -------
    h : float
        Distancia entre cada nodo
    x : float
        Vector con el cual se graficará
    lar : float
        Distancia total del dominio
    """
    h = (b-a)/(N+1)
    x = np.linspace(a,b,N+2)
    lar = b-a
    return h,x,lar

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
    b = np.zeros(N)
    b[0] = -Ta
    b[-1] = -Tb
    return b + q

def Vector_Fuente(N,S,h,k):
    q = np.ones(N) * (-S*h**2/k)
    return q

def Matriz_Diagonal(N,cons):
    """
    Esta función genera la matriz diagonal necesaria en la resolución del 
    problema.    
    Parameters
    ----------
    N : Integer
        Número de nodos.
    cons : Integer
        Valor en la diagonal
    Returns
    -------
    A : float
        Matriz diagonal
    """
    A = np.zeros((N,N))

    A[0,0] = cons; A[0,1] = 1
    for i in range(1,N-1):
        A[i,i] = cons
        A[i,i+1] = 1
        A[i,i-1] = 1
    A[N-1,N-2] = 1; A[N-1,N-1] = cons
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

def Sol_Analitica_F(a, b, Ta, Tb, S, k, N):
    """
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
        
    Returns
    -------
    sol : float
        Vector que contine la solución analica del problema
    """
    x = np.linspace(a,b,N+2)
    m = (Tb-Ta)/(b-a)
    sol = np.zeros(N+2)
    for i in range(N+2):
        aux = x[i]
        sol[i] = (m + (S/(2*k))*((b-a)-aux))*aux + Ta        
    return sol


def Error(u,u_exa,N):
    """
    Esta función genera un vector que contiene la diferencia entre los 
    valores de las soluciones y devuelve la suma de este.    
    Parameters
    ----------
    u : float
        Vector que contiene la solución numérica del problema
    u_exa : float
        Vector que contiene la solución analítica del problema
    Returns
    -------
    error: float
        Diferencia entre los valores obtenidos numérica y analíticamente.
    """
    error = np.zeros(N+2)
    for i in range(N+2):
        error[i] = u[i] - u_exa[i]
    return sum(error)

def Graficas(x,u,u_exa,Titulo):
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
    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.suptitle(Titulo)
    ax1.plot(x, u, '-bo', label = 'Solución')
    ax1.set_title('Solución numérica', color = 'blue', fontsize = 12)
    ax1.set(xlabel = 'Dominio [m]', ylabel = 'Temperatura [C]')
    ax1.grid(color = 'w')
    ax1.legend()
    
    ax2.plot(x, u_exa, '-ro', label = 'Solución')
    ax2.grid(color = 'w')
    ax2.set_title('Solución analítica', color = 'blue', fontsize = 12)
    ax2.set(xlabel = 'Dominio [m]', ylabel = 'Temperatura [C]')
    ax2.legend()
    plt.show()

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
    np.savetxt('Solución1.txt',tabla,fmt='%f', header = 'Soluciones del problema')