texto_usuario = input('ingrese un texto: ')
lista = texto_usuario
palabras_repetidas = dict()
palabra = ' '

for i in lista:
    if i == ' ':
        if palabra in palabras_repetidas:
            palabras_repetidas[palabra] += 1
            palabra = ' '
        else:
            palabras_repetidas[palabra] = 1
            palabra = ' '
    else:
        palabra += i

if palabra in palabras_repetidas:
    palabras_repetidas[palabra] += 1
else:
    palabras_repetidas[palabra] = 1

for a in palabras_repetidas:
    if palabras_repetidas[a] == 1:
        print(f'{a}: {palabras_repetidas[a]} vez')
    else:
        print(f'{a}: {palabras_repetidas[a]} veces')

