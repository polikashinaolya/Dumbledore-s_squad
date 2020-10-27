def public_helper(str_str, maxLen, str_end):
    if len(str_str) < maxLen:  #если длина первой строки меньше числа
        return str_str         #выходим из функции со значением первой строки
    str_split = str_str.split() #бьем первую строку по пробелаи
    str_new = ''
    for str_part in str_split: #ищем элемент больше числа
        if len(str_new) > maxLen:
            break
        str_new += str_part  #прибавляем его к пустой строке
    str_new += str_end   #прибавляем вторую строку
    return str_new


print(public_helper(input(), int(input()), input()))