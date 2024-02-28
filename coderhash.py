"""
Programa para codificar cadenas de texto en hash
Se lee el texto a codificar y se muestra en la ventana el resultado
en forma de codigo hash del texto de entrada
"""

from tkinter import *
import hash256 as hs

def on_click(event):
    cadena.set(entrada.get())
    cadenaCodificada = hs.encriptar(cadena.get())
    mensaje3.config(text = "Texto codificado")
    mostrarTexto.insert('1.0', cadenaCodificada)
# Creacion de la ventana principal
window = Tk()

# Configuracion de la ventana
# Titulo de la ventana
window.title("Codificador HASH")

# Configurando dimensiones y ubicacion de la ventana
window.geometry("650x400+360+140")

window.minsize(400,200)
window.maxsize(800,600)

# Cambia el color de la ventana
#window.configure(bg="lightblue")

# Creacion de cadena de texto de entrada
cadena = StringVar()

# Creacion de cadena de texto codificada
cadenaCodificada = StringVar()

# Creacion de las etiquetas
mensaje1 = Label(window, text="Programa para codificar cadena de caracteres en hash256")
mensaje2 = Label(window, text="Ingrese una cadena de caracteres para codificarla")

# Modificar la presentación de los mensajes
mensaje1.config(font=("Arial", 14))
mensaje2.config(font=("Arial", 12))

# Mostrar etiquetas
mensaje1.grid(row=0, column=0, padx = 10, pady = 10)
mensaje2.grid(row=1, column=0, padx = 10, pady = 10)

# Crear caja de ingreso de datos
entrada = Entry(window, textvariable = cadena)

# Mostrar caja de ingreso de datos
entrada.grid(row=2, column=0, padx = 10, pady = 10)

# Creacion de boton de accion
boton = Button(window, text = "Codificar")
boton.config(font=("Arial", 12))

# Mostrar boton
boton.grid(row=3, column=0)

# Accion del boton
boton.bind("<Button 1>", on_click)

# Creacion de las etiquetas
mensaje3 = Label(window, text=" ")

# Modificar la presentación de los mensajes
mensaje3.config(font=("Arial", 10))

# Mostrar etiqueta
mensaje3.grid(row=4, column=0, padx = 10, pady = 10)

# Crear texto
mostrarTexto = Text(window, width = 85, height = 5, font=("Arial", 10), bg="lightgray")

# Mostrar texto
mostrarTexto.grid(row=5, column=0, padx = 10, pady = 10)

# Bucle de ejecucion de la ventana
window.mainloop()
