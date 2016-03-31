#!/usr/bin/env python3

number = 23
running = True

while running:
    guess = int(input('Введите целое число: '))

    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False
    elif guess < number:
        print('Нет, загаданое число намного больше этого.')
    else:
        print('Нет, загаданое число намного меньше этого.')
else:
    print('Цикл while закончен.')

print('Завершение.')

