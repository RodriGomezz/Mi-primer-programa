agenda_cumples = dict()

condicion = False
while not condicion:
    pregunta = input('ingrese fechas[A] / consulte fechas [C] / salir [S]: ').upper()
    if pregunta == 'A':
        nombre = input('ingrese nombre: ')
        fecha = input('ingrese fecha: ')
        agenda_cumples[nombre] = fecha
    elif pregunta == 'C':
        nombre = input('ingrese un nombre: ')
        print(agenda_cumples[nombre])
    elif pregunta == 'S':
        condicion = True

