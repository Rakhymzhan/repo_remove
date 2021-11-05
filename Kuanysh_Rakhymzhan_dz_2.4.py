names = ['Игорь', 'МАРИНА', 'нИКОЛАй', 'аэлита']

positions = ['1.инженер-конструктор Игорь', '2.главный бухгалтер МАРИНА', '3.токарь высшего разряда нИКОЛАй',
             '4.директор аэлита']

new_pos = [p.lower().title() for p in positions]
print(new_pos)

user_pos = input('Выберите сотрудника: ')
if user_pos == '1':
    print(f'Привет {names[0].lower().capitalize()}!')
elif user_pos == '2':
    print(f'Привет {names[1].lower().capitalize()}!')
elif user_pos == '3':
    print(f'Привет {names[2].lower().capitalize()}!')
else:
    print(f'Привет {names[3].lower().capitalize()}!')
