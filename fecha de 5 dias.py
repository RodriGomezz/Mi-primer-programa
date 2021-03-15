import datetime

cinco_dias = datetime.datetime.now() - datetime.timedelta(days=5)
dia = cinco_dias.strftime('%A')
print(f'hace cinco dias fue {dia} de la fecha {cinco_dias}')