#!/usr/bin/env python3

number = 23
guess = int(input('Введите целое число: '))

if guess == number:
    print('Поздравляю, вы угадали, ')
    print('(хотя и не выиграли никакого приза!)')
elif guess < number:
    print('Нет, загаданное число намного больше этого.')
else:
    print('Нет, загаданное число немного меньше этого.')

print('Завершено')

