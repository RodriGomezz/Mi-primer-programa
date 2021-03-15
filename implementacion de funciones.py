"""
encuentre el numero mas grande entre tres numeros
"""
def numero_mas_grande(numero1, numero2, numero3):
    mas_grande = 0
    if numero1 > numero2:
        mas_grande = numero1
    else:
        mas_grande = numero2
    if numero3 > mas_grande:
        mas_grande = numero3
    return mas_grande

num1 = int(input("ingrese 3 numeros para saber cual es el mas grande: "))
num2 = int(input(": "))
num3 = int(input(": "))

print(numero_mas_grande(num1, num2, num3))

"""
dado un numero y un rango comprobar que ese numero este entre los dos
"""
def comprobar_numero(numero, mini, maxi):
    resultado = False
    while mini <= maxi and resultado == False:
        if numero == mini:
            resultado = True
        mini += 1
    return resultado


numero_usuario = int(input("ingrese un numero: "))
minimo = int(input("ingrese el numero minimo: "))
maximo = int(input("ingrese el numero maximo: "))

print(comprobar_numero(numero_usuario, minimo, maximo))

'''
funcion que reciba una lista y devuelva otra pero con solo numero pares
'''

def numeros_pares(lis):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return pares

lista = [1, 2, 3, 4, 5, 6]
print(numeros_pares(lista))