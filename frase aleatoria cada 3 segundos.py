import random
from time import sleep

lista = ['hola que hace', 'tas loco', 'que haces bo', 'mas bien', 'sape']

while True:
    num = random.randint(0, 5)
    print(lista[num])
    sleep(3)
