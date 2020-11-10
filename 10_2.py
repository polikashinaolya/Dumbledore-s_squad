class Clock_Exception(Exception):

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return self.text


class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        if self.hour in [1, 21]:
            return '%s час %s минут' % (self.hour, self.minute)
        elif self.hour % 10 in [2, 3, 4, 22, 23]:
            return '%s часа %s минут' % (self.hour, self.minute)
        else:
            return '%s часов %s минут' % (self.hour, self.minute)

    def in_minute(self):
        return self.hour * 60 + self.minute


def transformation(time):
    try:
        time = time.split(':')
        if len(time) != 2:
            raise Clock_Exception('BadFormatException: Число нужно написать в формате ХХ:ХХ')
        hour = int(time[0])
        minute = int(time[1])
        if hour > 23 or hour < 0:
            raise Clock_Exception('BadHourException: часы определяются промежутком от 0 до 23')
        if minute > 60 or minute < 0:
            raise Clock_Exception('BadMinutesException: минуты определяются промежутком от 0 до 59')
    except ValueError:
        print('Время должно быть представлено двумя числами через : , где первое число - часы, второе - минуты')
    except Clock_Exception as CE:
        print(CE)
    else:
        return hour, minute


time_1 = transformation(input())
time_2 = transformation(input())
time_1_min = Clock(time_1[0], time_1[1]).in_minute()
time_2_min = Clock(time_2[0], time_2[1]).in_minute()
if time_1_min < time_2_min:
    raise Exception('TimeTravellingException: сначала укажите более позднее время ')
else:
    Time = time_1_min - time_2_min
print(Clock(Time // 60, Time % 60))
