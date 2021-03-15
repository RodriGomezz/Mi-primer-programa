import datetime
import random
from time import sleep

frases_alegres = ['hoy es un dia hermoso', 'hoy es viernes', 'comenzo el 2021']
nombre_de_muebles = ['silla', 'mesa', 'sillon', 'ropero', 'cama', 'escritorio']
nombre_de_bebidas = ['cocacola', 'fanta', 'sprite', 'pepsi', 'ron', 'whisky', 'cerveza']
frases_de_odio = ['El odio no es un buen consejero', 'Mientras odies, existirán personas a las que odiar', 'Lo opuesto al amor no es el odio, sino la indiferencia']
nombres_de_comida = ['napolitana', 'empanadas', 'tortafitas', 'pasta', 'ensalada', 'hamburguesa']
frases_absurdas = ['No te insulto, te defino brevemente', 'El 80% de tus calcetines no tienen pareja y no andan por ahí llorando', 'Hay personas que se merecen una palmadita. En la cara. Con una silla']
nombres_de_animales = ['perro', 'gato', 'raton', 'peces', 'tigre', 'lobo']
frases_motivacionales = ['El mejor momento para plantar un árbol era hace 20 años. El segundo mejor momento es AHORA', 'Cada día es una nueva oportunidad para cambiar tu vida', 'El momento que da más miedo es siempre justo antes de empezar']
sonidos_de_animales = ['oink', 'quiquiriquí', 'miau']
frases_tristes = ['Ella encendió la soledad, para apagar un rato de su vida.', 'El silencio es el grito más fuerte.', 'Estoy bien, sólo duele cuando respiro.']
frases = {0: frases_alegres, 1: nombre_de_muebles, 2: nombre_de_bebidas, 3: frases_de_odio, 4: nombres_de_comida, 5: frases_absurdas, 6: nombres_de_animales, 7: frases_motivacionales, 8: sonidos_de_animales, 9: frases_tristes}


while True:
    currency_time = datetime.datetime.now()
    tiempo = currency_time.second
    while tiempo >= 10:
        tiempo = tiempo - 10

    alazar = random.randint(0, len(frases[tiempo]) - 1)
    print(frases[tiempo][alazar])
    sleep(1)