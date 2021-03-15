def mostrar_titulo_subrayado(texto):
    rayas = ''
    for i in texto:
        rayas += '-'
    return rayas

print('Hola mundo  ')
print(mostrar_titulo_subrayado('Hola mundo'))



'''
nate correccion 
'''

def titulo_subrayado(text):
    print(text)
    print(len(text) * '-')

titulo_subrayado('hola mundo!')