#crea un programa que sea capaz de contar espacios. puntos y comas en una string intoducida por el usuario
texto_usuario = input("ingrese un texto: ")
letra = [".", ",", " "]

n_puntos = 0
n_comas = 0
n_espacios = 0

for indice in texto_usuario:
  if indice in letra[0]:
      n_puntos += 1
  elif indice in letra[1]:
      n_comas += 1
  elif indice in letra[2]:
      n_espacios += 1

print("espacios", n_espacios, '\n' "puntos", n_puntos, "\n" "comas",n_comas)