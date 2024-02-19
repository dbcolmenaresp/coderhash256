# Programa en cargado de codificar una cadena de caracteres con el formato hash

# Librerias necesarias para codificar una cadena de caracteres en hash

from hashlib import sha3_256
from datetime import datetime
#import numpy as np, pandas as pd
from random import randint, sample

def encriptar(frase):
    encriptado = sha3_256(frase.encode('utf-8')).hexdigest().upper()
    return ' '.join([encriptado[i:i + 4] for i in range(0, 64, 4)])

print("Este es un programa para codificar cadena de caracteres en hash")

print("Ingrese una cadena de caracteres para codificar en HASH")

cadena = input()

print(f"La cadena a encriptar es: ", cadena)

print(f"El codigo resultante es\n", encriptar(cadena))
