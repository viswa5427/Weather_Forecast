import requests
import json

api_key = "c046999b657d072a1dd2d413fd4dd156"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather_data(city):
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    data = response.json()
    return data

def weather_forecast():
    city_name = input("Enter city name : ")
    data = get_weather_data(city=city_name)
    if data["cod"] != "404":
        current_temperature = data["main"]["temp"]
        current_pressure=data["main"]["pressure"]
        current_humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        print(f"Weather report for {city_name.upper()}:")
        print(f"Temperature (in kelvin unit) = {str(current_temperature)}")
        print(f"Atmospheric pressure (in hPa unit) ={str(current_pressure)}")
        print(f"Humidity (in percentage) = {str(current_humidity)}")
        print(f"Description = {str(weather_description)}")
    else:
        print(city_name.upper() + " weather details not found")


if __name__ == "__main__":
    weather_forecast()