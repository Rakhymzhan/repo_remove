duration = int(input('Укажите количество секунд: '))
days = duration // (24 * 60 * 60)
hours = duration // (60 * 60) - days * 24
minutes = duration // 60 - hours * 60 - days * 24 * 60
seconds = duration % 60

if days and hours and minutes and seconds == 0:
    print('Время не указано!')
else:
    print(f'{days} дней {hours} часов {minutes} минут {seconds} секунд')


