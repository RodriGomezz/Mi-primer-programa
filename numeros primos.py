numero = int(input("ingrese dos numeros para conocer sus numero primos: "))
numero2 = int(input())
divisor = 3
contador = 0
i = 1
lista = []

while numero <= numero2:
    if not numero % 2 == 0:
        while divisor <= numero and contador == 0:
         if numero % divisor == 0:
            contador += 1
         else:
            divisor += 2
    if contador == 1:
        lista.append(numero)
    numero += 1
    divisor = 3
    contador = 0

print(lista)