texto_usuario = input("ingresa un texto: ").lower()
vocales = ['a','e','i','o','u']

numero = 1
for indice in texto_usuario:
    if indice in vocales:
     texto_usuario = texto_usuario.replace(indice,str(numero),1)
     numero += 1

print(texto_usuario)
