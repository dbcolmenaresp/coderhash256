# coderhash256
Codificador [hash]([https://es.wikipedia.org/wiki/Funci%C3%B3n_hash]) 256 con Python



Es importante tener conocimientos relacionados con la codificacion de la informacion, esto con la necesidad de mantener la confidencialidad de la misma, una de las caracteristicas imoortantes de la seguridad de la informacion que consiste en evitar que personas no autorizadas tengan acceso a la informacion que se resguarda en nuestros sistemas de informacion.

Esta caracteristica de la confidencialidad es muy importante en el ambiente hibrido e hiperconectado en el que nos desenvolvemos actualmente, en vista de que estamos constantemente compartiendo información a traves de las plataformas de telecomunicaciones disponibles actualmente.

El codigo hash es un algoritmo matematico que transforma cualquier bloque arbitrario de datos, puede ser una cadena de caracteres o datos de otra naturaleza, en una nueva cadena de caracteres de longitud fija, independientemente de la longitud del objeto de datos de entrada.

Parametros de entrada
Una cadena de caracteres ingresada por linea de comandos

Salida
Una cadena de caracteres equivalente a la codificacion hash de la cadena de caracteres recibida por la linea de comandos como entrada del programa

Iniciamos el programa importando las librerias necesarias, en este caso

~~~python
from hashlib import sha3_256
~~~

A continuación se procede a crear la funcion encargada de realizar la conversion de la cadena de caracteres recibida como parametro a su correspondiente codigo hash

~~~python
def encriptar(frase):
    encriptado = sha3_256(frase.encode('utf-8')).hexdigest().upper()
    return ' '.join([encriptado[i:i + 4] for i in range(0, 64, 4)])
~~~

Se procede a solicitar al usuario una cadena de caracteres para codificar, de la siguiente manera

~~~python
print("Ingrese una cadena de caracteres para codificar en HASH")

cadena = input()
~~~

Esta instruccion se puede codificar de manera resumida en una sola linea

~~~python
cadena = input(print("Ingrese una cadena de caracteres para codificar en HASH"))
~~~

Una vez recibido el parametro necesario, se hace el llamado de la funcion para realizar la correspondiente codificacion

~~~python
encriptar(cadena)
~~~


