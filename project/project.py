###################
# CS50P Python
# Mark Edwards
# Final Project
##################

import requests
import re
from prettytable import PrettyTable
from prettytable import SINGLE_BORDER

def main():
    print("**********************************")
    print("Weather Forecast written in Python")
    print("**********************************")
    zipcode=get_zipcode()
    while True :
        print_menu()
        try:
            option = int(input("Option: "))
        except KeyboardInterrupt:
            print("")
            break
        if(option==9):
            break
        elif(option==1 or option==2) :
            get_weather(zipcode,option)
        else :
            print("Invalid Selection")

def print_menu():
    print(
    """
    1) Get Daily forecast
    2) Get Hourly forecast
    9) Exit
    """
    )

def get_weather(zipcode,option):

    # get latitute and longitute
    location=requests.get("http://api.zippopotam.us/us/"+zipcode)
    lat = location.json()["places"][0]["latitude"]
    lon = location.json()["places"][0]["longitude"]

    # get weather points
    weather_data=requests.get("https://api.weather.gov/points/"+lat+","+lon)

    match(option):
        case 1 : # Daily Forecast
            forecast_url=weather_data.json()["properties"]["forecast"]
        case 2 : # Hourly Forecast
            forecast_url=weather_data.json()["properties"]["forecastHourly"]
        case _:
            raise ValueError("Invalid Option")

    # Get Forecast
    forecast=requests.get(forecast_url)
    print("")
    print(f'Weather for {weather_data.json()["properties"]["relativeLocation"]["properties"]["city"]} {weather_data.json()["properties"]["relativeLocation"]["properties"]["state"]}')
    print("")
    match(option):
        case 1 : # Daily Forecast
            print_daily(forecast.json())
        case 2 : # Hourly Forecast
            print_hour(forecast.json())


def print_daily(forecast):
    print("*** Daily Forcast *************")
    x=PrettyTable()
    x.field_names = ["Day","Temp","Wind","Forecast"]

    for i in range(10):
        p=forecast["properties"]["periods"][i]
        x.add_row([p["name"],f'{p["temperature"]}{p["temperatureUnit"]}',f'{p["windDirection"]} {p["windSpeed"]}',p["shortForecast"][:40]])
    x.align="l"
    x.set_style(SINGLE_BORDER)
    print(x)

def print_hour(forecast):
    print("*** Hourly Forcast *************")
    x=PrettyTable()
    x.field_names = ["Hour","Temp","Wind","Forecast"]

    for i in range(10):
        p=forecast["properties"]["periods"][i]
        x.add_row([get_time(p["startTime"]),f'{p["temperature"]}{p["temperatureUnit"]}',f'{p["windDirection"]} {p["windSpeed"]}',p["shortForecast"][:40]])
    x.align="l"
    x.set_style(SINGLE_BORDER)
    print(x)

def get_zipcode():
    while True :
        try:
            zipcode=input("Enter Zipcode: ")
            if (validate_zipcode(zipcode)):
                break
        except KeyboardInterrupt:
            print("")
            exit("exit")

    return(zipcode)

def validate_zipcode(zipcode):

    if(re.search(r"^[0-9]{5}(?:-[0-9]{4})?$",zipcode)):
        return(True)
    else :
        return(False)

def get_time(date_time):
    dt=date_time.split("T")
    t=dt[1].split("-")[0]
    return(t)

if __name__ == "__main__":
    main()