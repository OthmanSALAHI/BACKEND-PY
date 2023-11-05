import requests
import datetime as dt

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "5d6f9927daa5c67338d1fb97b7fad348"


def kalvinToC_F(kalvin):
    cels = kalvin - 273.15
    fahr = cels * (9 / 5) + 32
    return cels , fahr
 
   
city = input("enter the city you want :")
url = BASE_URL + "appid=" + api_key + "&q=" + city
response = requests.get(url).json()

kalvinTemp = response["main"]["temp"]

celsuis , fahrenhit = kalvinToC_F(kalvinTemp)

humidity = response["main"]["humidity"]

print(f"the weather in {city} is {celsuis:.2f} °C {fahrenhit:.2f} °F\n The humidity is {humidity}%")
