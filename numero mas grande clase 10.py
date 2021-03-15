lista = [1,2,34,54,542,1,2,46,2,1]
mas_grande = 0

for indice in lista:
    if mas_grande < indice:
        mas_grande = indice

print(mas_grande)