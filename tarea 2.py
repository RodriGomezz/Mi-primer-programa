#crea un programa que sea capaz de contar la camtidad de letras mayusculas en una string introducida por el usuario. ej: Hola, me llamo Nate. ¿Tu como te llamas?  =3
texto_usuario = input("ingrese un texto: ")
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
mayusculas = 0

for indice in texto_usuario:
    if indice in abc:
           mayusculas += 1

print(mayusculas)