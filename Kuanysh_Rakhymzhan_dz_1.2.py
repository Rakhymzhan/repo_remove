cubes = []
for i in range(1, 1000):
    if i % 2 != 0:
        cubes.append(i ** 3)
print(cubes)


result = 0
for i in range(len(cubes)):
    sum_of_cube_numb = 0
    list_of_cubes_temp = cubes[i]
    while list_of_cubes_temp > 0:
        sum_of_cube_numb += list_of_cubes_temp % 10
        list_of_cubes_temp = list_of_cubes_temp // 10
    if sum_of_cube_numb % 7 == 0:
        result += (cubes[i])
print(f'Сумма чисел из списка, сумма цифр которых делится нацело на 7 составляет: {result}')

result = 0
for i in range(len(cubes)):
    cubes[i] += 17
    sum_of_cube_numb = 0
    list_of_cubes_temp = cubes[i]
    while list_of_cubes_temp > 0:
        sum_of_cube_numb += list_of_cubes_temp % 10
        list_of_cubes_temp = list_of_cubes_temp // 10
    if sum_of_cube_numb % 7 == 0:
        result += (cubes[i])
print(f'Сумма чисел, увеличенных на 17, сумма цифр которых делится нацело на 7 составляет: {result}')