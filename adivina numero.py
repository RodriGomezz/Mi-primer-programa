number_to_guess = int(input('elige un numero: '))

user_number = 0

while user_number != number_to_guess:
    user_number = int(input("adivina un numero: "))
    if number_to_guess == user_number:
        print('has ganado')
    else:
        print('has perdido')