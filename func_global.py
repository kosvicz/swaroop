#!/usr/bin/env python3

x = 50;

def func():
    global x

    print('x равен', x)
    x = 2
    print('Заменяем глобальное значение x на', x)

func()

print('Значение x составляет', x)

