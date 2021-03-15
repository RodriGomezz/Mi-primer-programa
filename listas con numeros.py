numeros = [1, 10, 70, 30, 50, 55]
multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []

for i in numeros:
    if i % 2 == 0:
        multiplos_dos.append(i)
    if i % 3 == 0:
        multiplos_tres.append(i)
    if i % 5 == 0:
        multiplos_cinco.append(i)
    if i % 7 == 0:
        multiplos_siete.append(i)

print("multiplos_dos = {}\nmultiplos_tres = {}\nmultiplos_cinco = {}\nmultiplos_siete = {}".format(multiplos_dos,multiplos_tres,multiplos_cinco,multiplos_siete))