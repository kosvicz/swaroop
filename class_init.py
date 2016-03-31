#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Привіт! Мене звати', self.name)

p = Person('Victor')
p.sayHi()

