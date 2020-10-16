def coder(text):
    new_text = ''
    for character in text:
        if 65 <= ord(character) <= 90 or 97 <= ord(character) <= 122:
            if character == 'z':
                new_text += 'A'
            elif character == 'Z':
                new_text += 'a'
            else:
                new_text += (chr(ord(character) + 1)).swapcase()
        else:
            new_text += character
    return new_text


def decoder(text):
    new_text = ''
    for character in text:
        if 65 <= ord(character) <= 90 or 97 <= ord(character) <= 122:
            if character == 'a':
                new_text += 'Z'
            elif character == 'A':
                new_text += 'z'
            else:
                new_text += (chr(ord(character) - 1)).swapcase()
        else:
            new_text += character
    return new_text


text_coder = coder(input())
print(text_coder)
print(decoder(text_coder))