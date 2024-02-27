# Programa para codificar cadenas de texto en hash

from tkinter import *
#import hash256

def botonPresionado():
    print("Boton presionado")

# Creacion de la ventana principal
window = Tk()

# Titulo de la ventana
window.title("Codificador HASH")

# Configurando dimensiones y ubicacion de la ventana
window.geometry("600x400+360+140")

window.minsize(400,200)
window.maxsize(800,600)

# Cambia el color de la ventana
#window.configure(bg="lightblue")

# Creacion de las etiquetas
mensaje1 = Label(window, text="Programa para codificar cadena de caracteres en hash256")
mensaje2 = Label(window, text="Ingrese una cadena de caracteres para codificarla")

# Modificar la presentación de los mensajes
mensaje1.config(font=("Arial", 14))
mensaje2.config(font=("Arial", 12))

# Creacion de boton de accion
boton = Button(window, text = "Codificar")
boton.config(font=("Arial", 12))

# Accion del boton
boton.config(command=botonPresionado)

# Mostrar etiquetas
mensaje1.grid(row=0, column=0)
mensaje2.grid(row=1, column=0)

#

# Mostrar boton
boton.grid(row=3, column=0)

# Bucle de ejecucion de la ventana
window.mainloop()
