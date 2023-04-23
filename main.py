import argparse
import json
import logging
import os
import sys
from datetime import datetime

import pandas as pd
import requests


def main():
    # Create Logger
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s,%(msecs)03d %(name)-20s %(levelname)-7s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%s",
        stream=sys.stdout,
    )

    # Add Parser

    parser = argparse.ArgumentParser()
    parser.add_argument("--locations_list", nargs="+", help="A list of places to check the weather for", required=True)
    args = parser.parse_args()
    places = args.locations_list

    # Extract data from OpenWeatherMap API
    # set the API key
    api_key = os.environ.get("API_KEY", None)
    if not api_key:
        logger.error("No API_KEY environment variable found, can't download data")
        sys.exit(1)

    url = "https://api.openweathermap.org/data/2.5/weather"
    data = []
    timestamp = datetime.now().isoformat()

    # iterate through the locations list
    for place in places:
        querystring = {"q": place, "units": "metric", "appid": api_key}

        # send a get request
        try:
            response = requests.request("GET", url, params=querystring)
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            logger.error(error)
        else:
            logger.info(response.status_code)

        weather_data = response.json()
        data.append(weather_data)

    # Transform data

    json_formatted_data = [
        {
            "name": record["name"],
            "temp": record["main"]["temp"],
            "humidity": record["main"]["humidity"],
            "wind": record["wind"]["speed"],
            "visibilty": record["visibility"],
            "description": record["weather"][0]["description"],
            "extraction_timestamp": timestamp,
        }
        for record in data
    ]

    # Write data to file
    with open("weather.json", "a") as f:
        for record in json_formatted_data:
            print(json.dumps(record), file=f)

    df = pd.DataFrame(json_formatted_data)
    df.to_parquet("weather.parquet")


if __name__ == "__main__":
    main()
