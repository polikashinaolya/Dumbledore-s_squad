def write_1_999(figure):
    text = ''
    text_units = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
                  9: 'девять'}
    text_10_19 = {0: 'десять', 1: 'одиннадцать', 2: 'двенадцать', 3: 'тринадцать', 4: 'четырнадцать', 5: 'пятнадцать',
                  6: 'шестнадцать',
                  7: 'семнадцать', 8: 'восемнадцать', 9: 'девятнадцать'}
    text_decades = {2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят',
                    8: 'восемьдесят', 9: 'девяносто'}
    text_hundreds = {1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот',
                     8: 'восемьсот', 9: 'девятьсот'}

    rezult = figure//100
    if rezult != 0:
        text += text_hundreds[rezult]
        figure = figure % 100
    rezult = figure//10
    if rezult != 0 and rezult != 1:
        text += ' ' + text_decades[rezult]
        figure = figure % 10
    elif rezult == 1:
        text += ' ' + text_10_19[figure % 10]
    if 0 < figure <= 9:
        text += ' ' + text_units[figure]
    return text


def write_1000_999000(figure):
    text = ''
    rezult = figure // 1000
    if rezult == 0:
        text += write_1_999(figure % 1000)
    elif rezult == 1:
        text += 'одна тысяча' + ' ' + write_1_999(figure % 1000)
    elif rezult == 2:
        text += 'две тысячи' + ' ' + write_1_999(figure % 1000)
    elif rezult == 3:
        text += 'три тысячи' + ' ' + write_1_999(figure % 1000)
    elif rezult == 4:
        text += 'четыре тысячи' + ' ' + write_1_999(figure % 1000)
    else:
        text += write_1_999(figure // 1000) + ' тысяч' + ' ' + write_1_999(figure % 1000)
    return text


def write_1000000_999000000(figure):
    text = ''
    rezult = figure // 1000000
    if rezult == 1:
        text += 'один миллион' + ' ' + write_1000_999000(figure % 1000000)
    elif rezult == 2:
        text += 'два миллиона' + ' ' + write_1000_999000(figure % 1000000)
    elif rezult == 3:
        text += 'три миллиона' + ' ' + write_1000_999000(figure % 1000000)
    elif rezult == 4:
        text += 'четыре миллиона' + ' ' + write_1000_999000(figure % 1000000)
    else:
        text += write_1_999(figure // 1000000) + ' миллионов' + ' ' + write_1000_999000(figure % 1000000)
    return text


print('Введите число в формате ХХХ,ХХХ,ХХХ')
Figure = int(''.join(input().split(',')))
if 1 <= Figure <= 999:
    print(write_1_999(Figure))
elif 1000 <= Figure <= 999999:
    print(write_1000_999000(Figure))
elif 1000000 <= Figure <= 999999999:
    print(write_1000000_999000000(Figure))
elif Figure == 0:
    print('ноль')


