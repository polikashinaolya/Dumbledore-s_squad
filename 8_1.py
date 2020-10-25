def converting(x, binary):
    a = x // 2
    b = x % 2
    binary = str(b) + binary
    if a <= b:
        return str(a) + binary
    return converting(a, binary)


print('Введите число')
binary_number = ''
print(int(converting(int(input()), binary_number)))