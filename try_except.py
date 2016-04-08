#!/usr/bin/env python3
#--*-- coding: utf-8 --*--


try:
    text = input('Введите что-нибудь --> ')
except EOFError:
    print('Ну зачем вы сделали мне  EOF?')
except KeyboardInterrupt:
    print('\nВы отменили операцию.')
else:
    print('Вы ввели {0}'.format(text))
