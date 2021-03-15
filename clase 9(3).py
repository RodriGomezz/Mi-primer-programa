numero_usuario = input("ingrese un numero: ")
lista_usuario = []

while numero_usuario != "fin":
    if numero_usuario.isdigit():
     lista_usuario.append(int(numero_usuario))
    else:
        print('ingresa un numero')
    numero_usuario = input("ingrese otro numero: ")

numero_mas_chico = lista_usuario[0]
suma = 0

for numero in lista_usuario:
    if numero < numero_mas_chico:
        numero_mas_chico = numero
    suma += numero

contador_lista = 0
for indice in lista_usuario:
    contador_lista += 1

print('mas_pequeno = {} \nlargo de la lista: {} \nmedia= {}'.format(numero_mas_chico,contador_lista,suma/contador_lista))

