import requests, json


def get_weather(city):
  
  url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
  weather_data = requests.get(url).json()
  weather_data_structure = json.dumps(weather_data, indent=2)
  return weather_data_structure

