#!/usr/bin/env python3
# --*-- coding: utf-8 --*--

with open('poem.txt') as f:
    for line in f:
        print(line, end='')
