import requests
from django.conf import settings

def get_weather(city='London'):
    params = {
        'q': city,
        'appid': settings.OPENWEATHER_API_KEY,
        'units': 'metric'  # For Celsius
    }
    
    try:
        response = requests.get(settings.OPENWEATHER_URL, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return {
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'city': city
        }
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return None