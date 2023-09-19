import json
import logging
import sys
from datetime import datetime

import pandas as pd
import requests

URL = "https://api.openweathermap.org/data/2.5/weather"
logger = logging.getLogger(__name__)


def download_data(places, api_key):
    # Create Logger
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s,%(msecs)03d %(name)-20s %(levelname)-7s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%s",
        stream=sys.stdout,
    )

    if not api_key:
        logger.error("No API_KEY environment variable found, can't download data")
        sys.exit(1)

    extraction_timestamp = datetime.now().isoformat()

    data = _extract_data(api_key, places)
    print(data)
    save_data(data, extraction_timestamp)


def save_data(data, extraction_timestamp):
    json_formatted_data = [
        {
            "name": record["name"],
            "temp": record["main"]["temp"],
            "humidity": record["main"]["humidity"],
            "wind": record["wind"]["speed"],
            "visibilty": record["visibility"],
            "description": record["weather"][0]["description"],
            "extraction_timestamp": extraction_timestamp,
        }
        for record in data
    ]
    # Write data to file
    with open("files/weather.json", "a") as f:
        for record in json_formatted_data:
            print(json.dumps(record), file=f)
    df = pd.DataFrame(json_formatted_data)
    existing_data = pd.read_csv('files/weather.csv')
    new_data = pd.concat([existing_data, df], ignore_index=True)
    new_data.to_csv('files/weather.csv', index=False)


def _extract_data(api_key, places):
    data = []

    # iterate through the locations list
    for place in places:
        querystring = {"q": place, "units": "metric", "appid": api_key}

        # send a get request
        try:
            response = requests.request("GET", URL, params=querystring)
            response.raise_for_status()
        except Exception as error:
            logger.error(f"Can't extract data for {place}")
            logger.error(error)
            continue

        weather_data = response.json()
        data.append(weather_data)
    return data

