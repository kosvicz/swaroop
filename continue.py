#!/usr/bin/env python3

while True:
    s = input('Введите что-нибудь: ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Введ́ёная строка достаточной длины')

