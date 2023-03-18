import requests
import os
from dotenv import load_dotenv

# User input
places = input("Enter the list of towns (comma-separated): ").split(",")

# Extract data from OpenWeatherMap API
load_dotenv()
api_key = os.getenv('API_KEY')
url = "https://api.openweathermap.org/data/2.5/weather"
data = []

for place in places:
    querystring = {"q": place, "units": "metric", "appid": api_key}
    response = requests.request("GET", url, params=querystring)
    print(response.status_code)
    weather_data = response.json()
    data.append(weather_data)

# Transform data
formatted_data = []
for d in data:
    place = d["name"]
    temp = d["main"]["temp"]
    humidity = d["main"]["humidity"]
    wind_speed = d["wind"]["speed"]
    description = d["weather"][0]["description"]
    formatted_data.append(f"The weather conditions for {place}: "
                          f" the temperature is {temp}C, "
                          f"humidity: {humidity}%, "
                          f"wind: {wind_speed}m/s, "
                          f" {description}")

# Write data to file
with open("weather.txt", "w") as f:
    f.write("\n".join(formatted_data))
