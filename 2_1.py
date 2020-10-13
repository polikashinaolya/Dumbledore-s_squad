
def text_editor(text, max_length):
    lenght_text = len(text)
    print(lenght_text)
    lenght_without_spaces = len(''.join(text.split()))
    print(lenght_without_spaces)

    if lenght_text % 2 == 0:
        print('количество символов в тексте четное')
    else:
        print('количество символов в тексте нечетное')

    if lenght_text > max_length:
        print('длина текста превышает длину %s символов' % max_length)


text_i = input()
max_length_i = int(input())
text_editor(text_i, max_length_i)