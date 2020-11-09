import json
import requests

response = requests.get("http://worldtimeapi.org/api/timezone/Europe/Moscow")
time = json.loads(response.text)
time = time['datetime'].split(':')
time = time[0].split('T')
hour = int(time[1])
if 0 <= hour <= 4:
    print ('Доброй ночи, Ольга')
elif 5 <= hour <= 9:
    print('Доброе утро, Ольга')
elif 10 <= hour <= 16:
    print('Добрый день, Ольга')
elif 17 <= hour <= 23:
    print('Добрый вечер, Ольга')
