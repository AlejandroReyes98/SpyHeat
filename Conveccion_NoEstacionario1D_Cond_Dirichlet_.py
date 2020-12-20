"""
Este programa calcula y grafica la solución a la ecuación de calor 
es estado no estacionario, además incluye el término convectivo. 


Los valores con los que se trabaja son:
a=0          Inicio del dominio
b=2.5        Fin del dominio 
N=300        Número de nodos
Ta=1         Temperatura en el inicio del dominio
Tb=0         Temperatura en el final del dominio
K=0.001      Conductividad térmica
S=0          Fuentes o sumideros
ht=0.002     Tamaño de paso en el tiempo
Tmax=1       Tiempo final
u=1          Velocidad
Tolerancia=1e-6

El archvio .txt tiene estos mismos valores escritos. 
Si se desea modificar el archivo, se debe respetar el orden de las variables.
"""
import Funciones_No_estacionario as fun
import numpy as np
import matplotlib.pyplot as plt
import time

# Programa principal
print()
print("+----------------------------------------------------+")
print("|      Solucion de la transferencia de calor         |")
print("+----------------------------------------------------+")

print('Opciones para la ejecución: \n'
	  '1.- Tomar datos de ejemplo de un archivo \n'
      '2.- Ingresar los datos manualmente.')

sel = int(input('Escoja una opción.\n'))

# Ingreso de variables necesarias
a,b,N,Ta,Tb,K,S,ht,Tmax,v,Tol = fun.Ingreso(sel,"Datos_Conv_No_EstD.txt")

# Cálculo de Constantes
h,x,lar,Nt,r,p = fun.Constantes(a,b,N,ht,Tmax,K,v)
print("\n-------------------------------------------------")
print("El ancho de la malla es: ",h)
print("El largo de la barra es: ",lar)
print("El número de pasos en el tiempo es: ",Nt)
print("Constante r: ",r)
print("Constante p: ",p)
print("---------------------------------------------------\n")

# Discretización del dominio
x = fun.Dominio(a,b,N)
#Llamada al vector auxiliar
u = fun.Vector_aux(Ta,Tb,N,0)

# Este es lado derecho de la ecuación, que contiene la condicion inicial.
# Es decir la solucion en el paso 0. Por eso hacemos una copia de u.
f = np.copy(u[1:N+1])
uold = np.copy(u)

# Construccion de la matriz
A = fun.Matriz_Diagonal_Conv_Noest(N,r,p)

#Graficación de la condición inicial
#plt.plot(x,u,'--k',label='Inicial')

# Definición del vector del error
error = []

#Solución Analítica del problema
xa, ua = fun.Sol_Analitica(a,b,K,Tmax,N,v)

# Ciclo en el tiempo, desde 0 hasta Nt+1
for n in range(1,Nt+1):
    f[0] += (p+r)*Ta
    f[N-1] += -(p-r)*Tb
    # Solución al sistema lineal
    u[1:N+1] = np.linalg.solve(A,f) 
    
    # Cálculo del error y modificación del vector
    err = np.sqrt(h) * np.linalg.norm(uold-u)
    error.append(err)
    
    if (n % 100==0):
        etiqueta = 'Sol. Num. steep = {}'.format(n*ht)
        plt.plot(x, u, '.--', label=etiqueta)
            
    # Actualizacion de la solucion para dar el siguiente paso
    f = np.copy(u[1:N+1])
    uold = np.copy(u)
    
    if (err < Tol):
        break

# Llamado a funciones para la graficación
fun.Graficas(xa,ua,'Solución Analítica y Numérica')
fun.Graficas_Error(error)

# Llamado a función para guardar los datos
fun.Escritura(xa,ua)
