#!/usr/bin/env python3
#--*-- coding: utf-8 --*--


poem = """\
Программировать весело.
Если работа скучна,
Чтобы придать ей веселый тон - 
используй питон
"""

f = open('poem.txt', 'w')
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')

f.close()
