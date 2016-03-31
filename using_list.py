#!/usr/bin/env python3

shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

print('Я должен сделать ', len(shoplist), 'покупок.')

print('Покупки:', end=' ')
for item in shoplist:
    print(item)

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)

print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список выгладит так:', shoplist)

print('Первое, что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список:', shoplist)

