operacion = input("multiplicar / dividir / sumar / restar? ")
primer_numero = int(input("primer_numero: "))
segundo_numero = int(input("segundo numero: "))
resultado = 0

if operacion == "multiplicar":
    resultado = primer_numero * segundo_numero
elif operacion == "dividir":
    resultado = primer_numero / segundo_numero
elif operacion == "sumar":
    resultado = primer_numero + segundo_numero
elif operacion == "restar":
    resultado = primer_numero - segundo_numero

print("el resultado es: ",resultado)

