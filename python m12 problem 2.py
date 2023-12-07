import requests

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None
def main():
    api_key = 'YOUR_API_KEY'
    city_name = input("Enter the name of the municipality: ")
    weather_data = get_weather(api_key, city_name)
    if weather_data:
        weather_description = weather_data['weather'][0]['description']
        temperature_celsius = weather_data['main']['temp']
        print(f"\nWeather in {city_name}:")
        print(f"Condition: {weather_description}")
        print(f"Temperature: {temperature_celsius:.2f} °C")
    else:
        print("Failed to fetch weather information. Check your API key or city name.")
if __name__ == "__main__":
    main()