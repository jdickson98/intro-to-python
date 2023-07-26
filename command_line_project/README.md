# Weather App

Welcome to my weather app powered by OpenWeatherMap - todays sponsor of Joe Dickson's Command Line Program

## Prerequisites

Before running the script, you need to have the following:

1. Python installed on your system.
   
2. The `requests` library installed. If you don't have it, you can install it using `pip`:


## How to Use

1. Clone the repository or download the `weather_app.py` file to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the `weather_app.py` file.

3. Run the script using the following command: python weather_app.py

4. The script will ask for the name of a city.

5.  Et voila, current weather for the location is provided

## API Key

The script uses the OpenWeatherMap API to fetch weather data. To make API requests, you need to have an API key. In the `main()` function, replace the placeholder `api_key` variable with your actual OpenWeatherMap API key. If you don't have an API key, you can sign up for a free account at [OpenWeatherMap](https://openweathermap.org/) to obtain one.

## Attribution

This script was created as a simple demonstration of using the `requests` library to interact with APIs in Python. It uses the OpenWeatherMap API to fetch weather data for a given location. 

## Notes

- The weather data is displayed in Celsius (°C) units, as the API request specifies the units as metric.

- The `show_my_weather` function displays weather information such as temperature, humidity, and wind speed for the specified location. Feel free to modify or extend the function to display more weather details based on the API response.

- JSON is not as fun as python can confirm but data is stored in that format on OpenWeatherMap

Enjoy checking the weather for your favorite cities with this simple Python weather app!
