def time_min(time):
    time = time.split(':')
    time = int(time[0]) * 60 + int(time[1])
    return time


def time_hour(time):
    time = [time // 60, time % 60]
    for i in range(2):
        if time[i] < 10:
            time[i] = '0' + str(time[i])
    time = str(time[0]) + ':' + str(time[1])
    return time


print('Введите начальное время в формате ХХ:ХХ')
time_first = input()
time_first = time_min(time_first)
print('Введите конечное время в формате YY:YY')
time_second = input()
time_second = time_min(time_second)
if time_second >= time_first:
    time_delta = time_second - time_first
else:
    time_delta = (24*60 - time_first) + time_second
print('Прошло времени')
print(time_hour(time_delta))