import tkinter as tk
from tkinter import *
from tkinter import messagebox

import CondNoEst_1D_Interfaz as Win1
import ConvNoEst1D_Interfaz as Win2
import CondEst_1D_Interfaz as Win3

import CondEst_2D_InterfazBasica as Win5


import ConvNoEst_2D_Interfaz as Win8


#Ventana principal
ventana=tk.Tk()
ventana.title("SPY HEAT")
ventana.geometry('360x330')
ventana.configure(background="#FFCE00")

#Barra de menu dentro de la ventana principal:
menubar = Menu(ventana)
#Menu 'File':
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=ventana.quit)
#Menu 'Help':
#helpmenu = Menu(menubar, tearoff=0)
#helpmenu.add_command(label="Help", command=infoPrograma)
#helpmenu.add_command(label="About...", command= infoEquipo)

#menubar.add_cascade(label="Help", menu=helpmenu)

#Vamos a poner una etiqueta para que ahí el usuario escoga el metodo
e1=tk.Label(ventana,text="MENU PRINCIPAL",bg="#FFCE00",fg="#C70509",font = ('Helvetica', 12))
e1.pack(padx=5,pady=5,ipadx=5,ipady=5)

seleccionador = IntVar()
R1 = Radiobutton(ventana, text='Conduccion No Estacionaria. 1D', bg = "#FFCE00",fg="#C70509",font = ('Helvetica', 12) ,variable = seleccionador, value=1)
R1.pack( anchor = W )
R2 = Radiobutton(ventana, text='Convección No Estacionaria. 1D ', bg = "#FFCE00",fg="#C70509",font = ('Helvetica', 12), variable = seleccionador, value=2)
R2.pack( anchor = W )
R3 = Radiobutton(ventana, text='Conduccion Estacionaria. 1D', bg = "#FFCE00",fg="#C70509",font = ('Helvetica', 12), variable = seleccionador, value=3)
R3.pack( anchor = W )
R4 = Radiobutton(ventana, text='Convección Estacionaria. 1D "PENDIENTE"', bg = "#FFCE00",fg="#C70509",font = ('Helvetica', 12), variable = seleccionador, value=4)
R4.pack( anchor = W )
R5 = Radiobutton(ventana, text='Conducción Estacionaria 2D', bg = "#FFCE00",fg="#C70509",font = ('Helvetica', 12), variable = seleccionador, value=5)
R5.pack( anchor = W )
R6 = Radiobutton(ventana, text='Conducción No Estacionaria 2D "PENDIENTE"', bg = "#FFCE00",fg="#C70509",font = ('Helvetica', 12), variable = seleccionador, value=6)
R6.pack( anchor = W )
R7 = Radiobutton(ventana, text='Convección Estacionaria 2D "PENDIENTE"', bg = "#FFCE00",fg="#C70509",font = ('Helvetica', 12), variable = seleccionador, value=7)
R7.pack( anchor = W )
R8 = Radiobutton(ventana, text='Convección No Estacionaria 2D', bg = "#FFCE00",fg="#C70509",font = ('Helvetica', 12), variable = seleccionador, value=8)
R8.pack( anchor = W )
#Condicion para verificar el caso a implementar
def validar():
    """
    Función que valida la opción seleccionada por el usuario y ejecuta
    una función según sea el caso seleccionado
    Parameters
    ----------
    Ningún parámetro de entrada
        
    Returns
    -------
    Ningún parametro de salida

    """
    if seleccionador.get()==1:
        Win1.WinConduccionNoEst1D()
    elif seleccionador.get()==2:
        Win2.WinConveccionNoEst1D()
    elif seleccionador.get()==3:
        Win3.WinConduccionEst1D()
    elif seleccionador.get()==4:
        print("Falta el algoritmo para implementar Convección  Est 1D")
    elif seleccionador.get()==5:
        Win5.WinConduccionEst2D()
    elif seleccionador.get()==6:
        print("Falta el algoritmo para implementar Conducción No Est 1D")
    elif seleccionador.get()==7:
        print("Falta el algoritmo para implementar Convección  Est 1D")
    elif seleccionador.get()==8:
        Win8.WinConveccionNoEst2D()

    return()

#Boton para seleccionar el metodo
botonVerif=tk.Button(ventana,text="Validar selección",bg="#E4AB3B",fg="black",command=validar)
botonVerif.pack(side=tk.TOP)

ventana.config(menu=menubar)
ventana.mainloop()















