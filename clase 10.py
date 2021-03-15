usuario = input("escribe: ")
lista_int = []
lista_str = []

while usuario != "fin":
   if usuario.isdigit():
    lista_int.append(usuario)
   elif type(usuario) == str:
     lista_str.append(usuario)
   usuario = input("escribe: ")


print('lista int',lista_int,'\nlista str', lista_str)
