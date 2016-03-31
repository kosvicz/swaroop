# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#"""Наследование класов"""
'''Наследование класов'''


class SchoolMember:
    '''Представляєт любого человека в школе.'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    def tell(self):
        '''Вывести информацию.'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age))
