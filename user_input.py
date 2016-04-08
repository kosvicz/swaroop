#!/usr/bin/env python3
#--*-- conding: utf-8 --*--

def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text ==  reverse(text)


something = input('Введите текск: ')
if(is_palindrome(something)):
    print('Да, это палиндром')
else:
    print('Нет, это не палиндром')
