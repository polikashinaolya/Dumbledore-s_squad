def transformation(time):
    time = time.split(':')
    if len(time) != 2:
        raise Exception('BadFormatException: Число нужно написать в формате ХХ:ХХ')
    try:
        hour = int(time[0])
        minute = int(time[1])
        return hour, minute
    except ValueError:
        print('Время должно быть представлено двумя числами через : , где первое число - часы, второе - минуты')


class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        if 0 > self.hour > 24:
            raise Exception('BadHourException: часы определяются промежутком от 0 до 23')
        if 0 > self.minute > 60:
            raise Exception('BadMinutesException: минуты определяются промежутком от 0 до 59')

    def __repr__(self):
        if self.hour in [1, 21]:
            return '%s час %s минут' % (self.hour, self.minute)
        elif self.hour % 10 in [2, 3, 4, 22, 23]:
            return '%s часа %s минут' % (self.hour, self.minute)
        else:
            return '%s часов %s минут' % (self.hour, self.minute)

    def in_minute(self):
        return self.hour * 60 + self.minute


time_1 = transformation(input())
time_2 = transformation(input())
time_1_min = Clock(time_1[0], time_1[1]).in_minute()
time_2_min = Clock(time_2[0], time_2[1]).in_minute()
if time_1_min < time_2_min:
    raise Exception('TimeTravellingException: сначала укажите более позднее время ')
else:
    Time = time_1_min - time_2_min
print(Clock(Time // 60, Time % 60))
