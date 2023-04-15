import requests
import os
import argparse
import json
import logging
import pandas as pd


def main():

    # Create Logger
    logger = logging.getLogger(__name__)
    
    # Add Parser

    parser = argparse.ArgumentParser()
    parser.add_argument('--locations_list', nargs='+', help='A list of places to check the weather for')
    args = parser.parse_args()
    places = args.locations_list

    # Extract data from OpenWeatherMap API
    # set the API key
    try:
        api_key = os.environ['API_KEY']
        if not api_key:
            raise ValueError('API_KEY environment variable is empty')
    except KeyError:
        raise ValueError('API_KEY environment variable is not set')

    url = "https://api.openweathermap.org/data/2.5/weather"
    data = []

    # iterate through the locations list
    for place in places:
        querystring = {"q": place, "units": "metric", "appid": api_key}

        # send a get request
        try:
            response = requests.request("GET", url, params=querystring)
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            logger.error(error)
            print(error)
        else:
            logger.info(response.status_code)
            print(response.status_code)

        weather_data = response.json()
        data.append(weather_data)

    # Transform data
    formatted_data = []
    json_formatted_data = []
    for d in data:
        place = d["name"]
        temp = d["main"]["temp"]
        humidity = d["main"]["humidity"]
        wind_speed = d["wind"]["speed"]
        description = d["weather"][0]["description"]
        formatted_data.append([["name", place],
                               ["temp", str(temp)],
                               ["humidity", str(humidity) + '%'],
                               ["wind", str(wind_speed)],
                               ["description", description]
                               ])
        json_formatted_data.append({"name": place, "temp": str(temp),
                                    "humidity": str(humidity) + '%',
                                    "wind":str(wind_speed),
                                    "description": description
                                    })

    # Write data to file
    with open("weather.json", "w") as f:
        json.dump(json_formatted_data, f)

    df = pd.DataFrame(formatted_data)
    df.to_parquet("weather.parquet")


if __name__ == '__main__':
    main()
