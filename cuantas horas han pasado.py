import datetime

fecha = datetime.datetime(day=9, month=1, year=2021)
hoy = datetime.datetime.now()
horas = hoy - fecha

print(int(horas.total_seconds()/3600),'horas')