texto_usuario = input("texto: ")
vocales = ["a", 'e', 'i', 'o', 'u']
mi_lista = []

for indice in texto_usuario:
    if indice in vocales:
        mi_lista.append(indice)

print(mi_lista)