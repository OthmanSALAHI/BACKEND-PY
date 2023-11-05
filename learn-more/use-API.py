import requests
import datetime as dt

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

#print your api here from www.openweathermap.org
api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#changing kalvin to celisus and fehrenhit
def kalvinToC_F(kalvin):
    cels = kalvin - 273.15
    fahr = cels * (9 / 5) + 32
    return cels , fahr
 
#taking the city
city = input("enter the city you want :")

# if the city not found
if not city :
    print("city is not found")
    return

#the base url
url = BASE_URL + "appid=" + api_key + "&q=" + city

#connect to api
response = requests.get(url).json()

#the connect goes wrong :
if not response:
    print("connect is failed !")
    return
# take the the infos from api
kalvinTemp = response["main"]["temp"]

celsuis , fahrenhit = kalvinToC_F(kalvinTemp)

humidity = response["main"]["humidity"]


print(f"the weather in {city} is {celsuis:.2f} °C {fahrenhit:.2f} °F\n The humidity is {humidity}%")
