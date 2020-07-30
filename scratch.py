from pyowm import OWM

# смена языка на руссктй
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('3ec161f16da426ed9b08596dc17f3c4a')

place = input('Введи название города: ')

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
weather = observation.weather
temp = weather.temperature('celsius')["temp"]

# вывод температуры в цельсиях + рекомендации к погоде
print("В городе " + str(place) + " сейчас " + str(weather.detailed_status))
print("Температура " + str(temp))
if temp < 10:
    print("Сейчас прохладно, стоит одеться потеплее")
elif temp < 20:
	print("Можно что-нибудь накинуть сверху")
else:
	print("На улице тепло")
