#!/usr/bin/env python3

def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', a с равно', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)

