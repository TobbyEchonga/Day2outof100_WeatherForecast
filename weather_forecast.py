import requests

def get_weather_forecast(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Change units as needed (metric/imperial)
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data['name']
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"Weather in {city_name}: {weather_desc}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Failed to retrieve weather data.")

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
api_key = 'YOUR_API_KEY'
city_name = input("Enter city name: ")

get_weather_forecast(api_key, city_name)
