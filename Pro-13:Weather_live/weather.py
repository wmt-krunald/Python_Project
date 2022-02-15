import requests
from pprint import pprint

api_KEY = "8453e84800b4f45af4ad2b799152ddbe"

city = input("\nEnter the City Name : ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid=" + api_KEY + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)