from DateTime import DateTime

dt = DateTime().h_24()

if dt in [0, 1, 2, 3, 4]:
    print('Доброй ночи, %s' % 'Ольга')
elif dt in [5, 6, 7, 8, 9]:
    print('Доброе утро, %s' % 'Ольга')
elif dt in [10, 11, 12, 13, 14, 15, 16]:
    print('Добрый день, %s' % 'Ольга')
elif dt in [17, 18, 19, 20, 21, 22, 23, 24]:
    print('Добрый вечер, %s' % 'Ольга')