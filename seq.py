#!/usr/bin/env python3

shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'swaroop'

print('Элемент 0 -', shoplist[0])
print('Элемент 1 -', shoplist[1])
print('Элемент 2 -', shoplist[2])
print('Элемент 3 -', shoplist[3])
print('Элемент -1 -', shoplist[-1])
print('Элемент -2 -', shoplist[-2])
print('\nСимвол 0 -', name[0])

print('\nЭлименты с 1 по 3:', shoplist[1:3])
print('Элименты с 2 до конца:', shoplist[2:])
print('Элименты с 1 по -1:', shoplist[1:-1])
print('Элименты от начала до конца:', shoplist[:])

print('\nСимволы с 1 по 3:', name[1:3])
print('Символы с 2 до конца:', name[2:])
print('Символы с 1 по -1:', name[1:-1])
print('Символы от начала до конца:', name[:])

