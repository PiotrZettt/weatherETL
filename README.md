# weatherETL
An ETL pipe line to work with weather data.
At the moment the app accepts an input of places, towns you want to check the weather for and saves the results to a text file.

## How to run
Create new folder and clone the repo.
Create venv and install requirements.txt

This app retrieves data from the openweathermap.org 
To use it you need to sign in to https://api.openweathermap.org and obtain your uniqe api_key.
Once you have the key set it as an evnvironmental variable:

```export API_KEY=<your_api_key>```

This app will accept a json input file where you can specify locations you want to check the weather for. Provide the locations with the "name" keyword.
For example:
[{"name": "New York"}, {"name": "Tokyo"}]

run the app providing the locations file path, i.e.:

```python main.py locations_list.json```






