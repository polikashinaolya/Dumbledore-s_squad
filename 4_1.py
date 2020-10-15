def algorithm(array, N):
    flag = False
    for i in range(len(array) - 1):
        for k in range(i+1, len(array)):
            if array[i] + array[k] == N:
                flag = True
                break
        if flag:
            break
    return flag


print(algorithm([int(number) for number in input().split()], int(input())))