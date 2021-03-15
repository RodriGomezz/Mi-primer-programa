import random
from time import sleep

numero_random = str(random.randint(1,10))
texto_usuario = input('ingrese un numero entre 1 y 10: ')

while texto_usuario != numero_random:
    sleep(3)
    input('incorrecto')
    texto_usuario = input('ingrese un numero entre 1 y 10: ')

sleep(3)
input(f'correcto el numero era {numero_random}')