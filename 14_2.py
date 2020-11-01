def ATM(Summa, Money_there):
    Money_put = []
    if Summa // Money_there[0] <= Money_there[1]:
        Money_put = [Money_there[0], Summa // Money_there[0]]
        Summa = Summa % Money_there[0]
    if Summa // Money_there[0] > Money_there[1]:
        Money_put = [Money_there[0], Money_there[1]]
        Summa = Summa - Money_there[0] * Money_there[1]
    return {'Количество купюр': Money_put, 'остаток суммы': Summa}


money_there = [[100, 10], [200, 1], [500, 0], [1000, 0], [2000, 0], [5000, 1]]    #здесь необходимо заполнить банкомат
money_put = [[100, 0], [200, 0], [500, 0], [1000, 0], [2000, 0], [5000, 0]]

print('Введите сумму которую необходимо выдать')
summa = int(input())
if summa % 100 != 0:
    raise Exception(' BadFormatException')

print('Сумма крупными купюрами? Y - Yes/N - No')
flag = input()

if flag == 'Y':
    for i in reversed(range(6)):
        money_put[i] = ATM(summa, money_there[i])['Количество купюр']
        summa = ATM(summa, money_there[i])['остаток суммы']
if flag == 'N':
    for i in range(6):
        money_put[i] = ATM(summa, money_there[i])['Количество купюр']
        summa = ATM(summa, money_there[i])['остаток суммы']

if summa != 0:
    raise Exception('BadSumException')
else:
    print(money_put)
