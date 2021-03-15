import datetime
dias_traducidos = {'Monday': 'Lunes','Tuesday': 'Martes','Wednesday': 'Miercoles', 'Thursday': 'Jueves', 'Friday': 'Viernes', 'Saturday': 'Sabado', 'Sunday': 'Domingo'}
birth_day = datetime.datetime(day=3, month=6, year=2021)
today = datetime.datetime.now()
time_remaining = birth_day - today
dia = birth_day.strftime('%A')
for i in dias_traducidos:
    if dia in dias_traducidos:
        dia = dias_traducidos[dia]

print(f'para mi cumpleaños faltan {time_remaining.days} dias y {int(time_remaining.seconds/3600)} horas el cual sera un dia {dia}')
