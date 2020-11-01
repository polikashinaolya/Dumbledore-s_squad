flag = True

print('Введите первый массив c числами через пробел X X X')
mass_1 = [int(x) for x in input().split()]
print('Введите второй массив c числами через пробел X X X')
mass_2 = [int(x) for x in input().split()]
for i in mass_1:
    if i not in mass_2:
        flag = False
        break
print(flag)
