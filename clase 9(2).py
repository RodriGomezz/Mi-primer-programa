numero_usuario = int(input("ingrese un numero: "))

for indice in reversed(range(1, 11)):
     print("{} x {} = {}".format(numero_usuario, indice, numero_usuario*indice))