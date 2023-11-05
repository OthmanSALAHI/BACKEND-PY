# Weather Data Retrieval Script

This is a simple Python script that uses the OpenWeatherMap API to fetch and display weather data for a specified city. The script provides temperature information in both Celsius and Fahrenheit, as well as humidity.

## Requirements

- Python 3.x
- The `requests` library for making HTTP requests. You can install it using `pip install requests`.

## Usage

1. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).
2. Replace `"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"` with your actual API key in the code.
3. Run the script.
4. Enter the name of the city for which you want to fetch weather data.
5. The script will display the current temperature in both Celsius and Fahrenheit, as well as humidity.

## Functionality

- The script converts temperature data from Kelvin to both Celsius and Fahrenheit.
- It handles the case where the city is not found and when the API connection fails.

## Example
```
Enter the city you want: New York
The weather in New York is 17.77 °C 63.99 °F
The humidity is 51%
```

