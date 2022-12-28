# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите натуральную степень k: '))

with open('file.txt', 'w') as result:
    for i in range(k, -1, -1):
        r = random.randint(0, 100)
        if i > 1:
            if r > 1:
                result_01 = f'{r}*x**{i} + '
                result.write(result_01)
            elif r == 1:
                result_02 = f'x**{i} + '
                result.write(result_02)
        elif i == 1:
            if r > 1:
                result_03 = f'{r}*x + '
                result.write(result_03)
            elif r == 1:
                result_04 = f'x + '
                result.write(result_04)
        elif i == 0:
            if r > 0:
                result_05 = f'{r}'
                result.write(result_05)
    result.write(' = 0')