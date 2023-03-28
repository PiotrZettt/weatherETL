import requests
import os
from dotenv import load_dotenv


def main():
    # User input
    # TODO: this should be parsed from command line parameters, use argparse library for it
    places = input("Enter the list of towns (comma-separated): ").split(",")

    # Extract data from OpenWeatherMap API
    # TODO: why is this dotenv library used exactly? Seems like not needed at all
    load_dotenv()

    # TODO: what happens if API_KEY is not set properly? You need some kind of error detection here
    api_key = os.getenv('API_KEY')
    url = "https://api.openweathermap.org/data/2.5/weather"
    data = []

    for place in places:
        querystring = {"q": place, "units": "metric", "appid": api_key}
        response = requests.request("GET", url, params=querystring)
        # TODO: we don't really use print in programs. Please use logger (library logging)
        # this should be logged to info channel
        print(response.status_code)
        # TODO: what happens if this response is not a correct one, like 404 or 500?
        # You need some kind of error detection here: response.raise_for_status()
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
    # TODO: if we want to import it into table, this should be a machine readable format
    # json is enough. but you could also try to save it as parquet file format as an excercise
    with open("weather.txt", "w") as f:
        f.write("\n".join(formatted_data))


with __name__ == "__main__":
    main()
