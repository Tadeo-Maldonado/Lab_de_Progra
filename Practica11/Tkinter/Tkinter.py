import sys
from tkinter import *

def sumar():
    try:
        valor1 = int(entrada_texto.get())
        valor2 = int(entrada2_texto.get())
        valor = valor1+valor2
        etiqueta3.config(text=valor)
    except ValueError:
        etiqueta3.config(text="Introduce un numero por favor")

def restar():
    try:
        valor1 = int(entrada_texto.get())
        valor2 = int(entrada2_texto.get())
        valor = valor1 - valor2
        etiqueta4.config(text=valor)
    except ValueError:
        etiqueta4.config(text="Introduce un numero por favor")

def multiplicar():
    try:
        valor1 = int(entrada_texto.get())
        valor2 = int(entrada2_texto.get())
        valor = valor1 * valor2
        etiqueta5.config(text=valor)
    except ValueError:
        etiqueta5.config(text="Introduce un numero por favor")


app = Tk()
app.title("Profe no me deje en segundas.jpg, app de tkinter")

# Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Primer número")
etiqueta.grid(column=1, row=1, sticky=(W, E))
etiqueta2 = Label(vp, text="Segundo número")
etiqueta2.grid(column=3, row=1, sticky=(W, E))

etiqueta3= Label(vp, text="*")
etiqueta3.grid(column=1, row=5, sticky=(W, E))
etiqueta4= Label(vp, text="**")
etiqueta4.grid(column=2, row=5, sticky=(W, E))
etiqueta5= Label(vp, text="***")
etiqueta5.grid(column=3, row=5, sticky=(W, E))

boton = Button(vp, text="Sumar", command=sumar)
boton.grid(column=1, row=4)
boton2 = Button(vp, text="Restar", command=restar)
boton2.grid(column=2, row=4)
boton3= Button(vp, text="Multiplicar", command=multiplicar)
boton3.grid(column=3, row=4)

valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=2, row=1)
valor2 = ""
entrada2_texto = Entry(vp, width=10, textvariable=valor2)
entrada2_texto.grid(column=4, row=1)


app.mainloop()
