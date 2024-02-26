# Programa para codificar cadenas de texto en hash

import tkinter as tk
#import hash256

# Creacion de la ventana principal
window = tk.Tk()

# Titulo de la ventana
window.title("Codificador HASH")

# Configurando dimensiones y ubicacion de la ventana
window.geometry("600x400+360+140")

# Creacion de las etiquetas
mensaje1 = tk.Label(window, text="Programa para codificar cadena de caracteres en hash256")
mensaje2 = tk.Label(window, text="Ingrese una cadena de caracteres para codificarla")

# Mostrar etiquetas
mensaje1.grid(row=0, column=0)
mensaje2.grid(row=1, column=0)

# Bucle de ejecucion de la ventana
window.mainloop()
