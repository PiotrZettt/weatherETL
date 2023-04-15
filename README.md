# weatherETL
An ETL pipe line to work with weather data.
At the moment the app accepts an input of places, towns you want to check the weather for and saves the results to a text file.

## How to run
Create new folder and clone the repo.
Create venv and install requirements.txt

This app retrieves data from the openweathermap.org. 
To use it you need to sign in to https://api.openweathermap.org and obtain your uniqe api_key.
Once you have the key create an environmental variable:

```% export API_KEY=<your_key>```

The app uses the argparse library and to run it you need to provide locations you want to check the weather for
as arguments in the command line:

```% python main.py --locations_list location1 location2 location3``` and so on.



