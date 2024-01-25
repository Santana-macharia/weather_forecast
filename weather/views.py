# weather/views.py
from django.shortcuts import render
import requests

def get_weather(city):
    api_key = '2b3280ac7852ecbeb86e070203a5d267'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key}
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data

def index(request):
    city = request.GET.get('city', 'Nairobi')
    weather_data = get_weather(city)

    context = {
        'city': city,
        'temperature': weather_data.get('main', {}).get('temp'),
        'description': weather_data.get('weather', [{}])[0].get('description'),
    }

    return render(request, 'weather/weather.html', context)
