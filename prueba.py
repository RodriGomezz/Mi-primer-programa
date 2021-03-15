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