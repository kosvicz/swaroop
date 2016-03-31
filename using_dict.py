#!/usr/bin/env python3

ab = {
    'Swaroop'   : 'swaroop@swaroopch.com',
    'Larry'     : 'larry@wall.org',
    'Matsumoto' : 'matz@ruby-lang.org',
    'Spammer'   : 'spammer@hotmail.com'
}

print("Адрес Swaroop'a:", ab['Swaroop'])

del ab['Spammer']

print('\nВ адрсной книге {} контактов\n'.format(len(ab)))

for name, address in ab.items():
    print('Контакт {} с адресом {}'.format(name, address))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print('\nАдрес Guido:', ab['Guido'])

