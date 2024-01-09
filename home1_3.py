# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа
# используйте код:  from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

a = randint(0, 1000)
print(a)
print('Угадайте число от 0 до 1000')

n = 0
while n < 10:
    b = int(input(f'{n+1} ВВедите число: '))
    if b > a and n < 9:
        print('Загаданное число меньше')
    elif a > b and n < 9:
        print('Загаданное число больше')
    elif a == b and n == 9:
        print('Молодец! Вы угадали!')
        break
    elif n == 9:
        print('Вы не угадали. Все количество попыток истрачено')
    n += 1
