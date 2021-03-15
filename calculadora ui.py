import tkinter.messagebox
from tkinter import ttk
from tkinter import *

i = 0

def calculate(*args):
    mi_numero = int(entero.get())
    resultado.set(mi_numero+10)

def resultado_boton(valor):
    global i
    entero_entry.insert(i,valor)
    i += 1

def igualdades():
    ecuaciones = entero_entry.get()
    igualdad = eval(ecuaciones)
    entero_entry.delete(0, END)
    entero_entry.insert(0, igualdad)


cuadro = Tk()
cuadro.title('Calculadora')

entero = StringVar()
resultado = StringVar()

entero_entry = ttk.Entry(cuadro, width=35, textvariable=entero)
entero_entry.grid(column=0, row=0, columnspan=2, padx= 50, pady=10)

botones = ttk.Frame(cuadro, padding="12 5 12 15")
botones.grid()

ttk.Button(botones, text="-", command=lambda: resultado_boton('-')).grid(column=4, row=3, padx=3.5, pady=3.5)
ttk.Button(botones, text="+", command=lambda: resultado_boton('+')).grid(column=4, row=4, padx=3.5, pady=3.5)
ttk.Button(botones, text="x", command=lambda: resultado_boton('*')).grid(column=4, row=1, padx=3.5, pady=3.5)
ttk.Button(botones, text="÷", command=lambda: resultado_boton('/')).grid(column=4, row=2, padx=3.5, pady=3.5)
ttk.Button(botones, text="x²", command=lambda: resultado_boton('**')).grid(column=2, row=1, padx=3.5, pady=3.5)
ttk.Button(botones, text="√", command=lambda: resultado_boton('*0.5')).grid(column=3, row=1, padx=3.5, pady=3.5)
ttk.Button(botones, text="%", command=lambda: resultado_boton('%')).grid(column=1, row=1, padx=3.5, pady=3.5)
ttk.Button(botones, text="1", command=lambda: resultado_boton(1)).grid(column=1, row=2, padx=3.5, pady=3.5)
ttk.Button(botones, text="2", command=lambda: resultado_boton(2)).grid(column=2, row=2, padx=3.5, pady=3.5)
ttk.Button(botones, text="3", command=lambda: resultado_boton(3)).grid(column=3, row=2, padx=3.5, pady=3.5)
ttk.Button(botones, text="4", command=lambda: resultado_boton(4)).grid(column=1, row=3, padx=3.5, pady=3.5)
ttk.Button(botones, text="5", command=lambda: resultado_boton(5)).grid(column=2, row=3, padx=3.5, pady=3.5)
ttk.Button(botones, text="6", command=lambda: resultado_boton(6)).grid(column=3, row=3, padx=3.5, pady=3.5)
ttk.Button(botones, text="7", command=lambda: resultado_boton(7)).grid(column=1, row=4, padx=7, pady=7)
ttk.Button(botones, text="8", command=lambda: resultado_boton(8)).grid(column=2, row=4, padx=3.5, pady=3.5)
ttk.Button(botones, text="9", command=lambda: resultado_boton(9)).grid(column=3, row=4, padx=3.5, pady=3.5)
ttk.Button(botones, text="0", command=lambda: resultado_boton(0)).grid(column=2, row=5, padx=3.5, pady=3.5)
ttk.Button(botones, text="=", command=lambda: igualdades()).grid(column=4, row=5, padx=3.5, pady=3.5)



cuadro.mainloop()
