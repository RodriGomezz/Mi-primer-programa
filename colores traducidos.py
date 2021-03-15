colores_traducidos = {'rojo': 'red', 'azul': 'blue', 'amarillo': 'yellow', 'verde': 'green', 'marron': 'brown', 'violeta': 'purple', 'negro': 'black', 'blanco': 'white', 'gris': 'gray', 'naranja': 'orange'}

condicion = False
while not condicion:
    color = input('ingreese un color: ')
    if color == 'fin':
        condicion = True
        print('cerrando aplicacion')
    elif color in colores_traducidos:
        print(colores_traducidos[color])
    else:
        print('prueba nuevamente')