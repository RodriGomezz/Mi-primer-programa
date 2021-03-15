from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 8
HOUR_DURATION = 1


def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)


def main():
    current_time = datetime.datetime.now()
    is_night = False

    # mi codigo
    answer = input('deseas colocar una alarma? [S/N]')
    if answer == 'S':
        alarma_horas = int(input('a que hora quiere su alarma: '))
    else:
        answer2 = input('quieres marcar una fecha en especifico? [S/N]')
        if answer2 == 'S':
            dia = int(input('ingrese dia\n'))
            mes = int(input('ingrese mes\n'))
            year = int(input('ingrese year\n'))
            date = datetime.datetime(month=mes, day=dia, year=year)
            alarma_day = input('insert day of the week: ')


    while True:
        if answer == 'S':
         if current_time.hour == alarma_horas:
            write_file_and_screen('suena alarma', 'horas.txt')
        if answer == 'N':
         if current_time.strftime('%x') == date.strftime('%x'):
            write_file_and_screen('suena alarma', 'horas.txt')

        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)
        light_changed = False

        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            is_night = True
            light_changed = True

        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:
            is_night = False
            light_changed = True

        if light_changed:
            if is_night:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
            else:
                write_file_and_screen("Se ha hecho de día", "horas.txt")

        write_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")


if __name__ == "__main__":
    main()