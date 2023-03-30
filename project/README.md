    # Weather Forecast
    #### Video Demo:  https://youtu.be/6lh1HNuB4CY
    #### Description:
    A user enters a zip code and can get the weather for the location.
    #### Author: Mark Edwards

    Prerequisites
    The project uses these Python libraries

    Requests: https://pypi.org/project/requests/
    How to install: pip install requests

    RE: https://docs.python.org/3/library/re.html
    How to install: pip install re

    prettytable https://pypi.org/project/prettytable/
    How to install: pip install prettytable

    How to run program

    python3 project.py

    After starting the program, the user will be prompted to enter a zip code
    --------------------------
    Enter Zip code:
    --------------------------
    The zip code is validated using Regular Expressions.
    The valid format for a zip code is 00000 or 00000-0000

    After entering a valid zip code format the user will be prompted
    with a menu. There are three choices.
    --------------------------
    1) Get Daily forecast
    2) Get Hourly forecast
    9) Exit
    --------------------------

    The user can select the number for the weather they would like to see.

    The main function of the program is get_weather. It takes two
    parameters. The first one is the zip code and the second is the
    menu option.

    Getting the weather takes multiple steps

    The first step is to check the zip code to see if it is valid.
    This is done by using the Zippopotam web API,
    Along with making sure the zip code is valid it returns the
    latitude and longitude of the location.

    Example response:
    {"post code": "10001", "country": "United States", "country abbreviation": "US", "places": [{"place name": "New York City", "longitude": "-73.9967", "state": "New York", "state abbreviation": "NY", "latitude": "40.7484"}]}

    Reference the documentation at http://api.zippopotam.us/us/
    for more information about the API

    The National Weather Service (NWS) provides many web APIs. For
    this application we are using the API Web Service. Full
    documentation is available at
    https://www.weather.gov/documentation/services-web-api
    Each API request type can be obtained by using the corresponding
    endpoint. For the weather forecast we use we are using "points"
    https://api.weather.gov/points/(point)
    The input for the points request requires the latitude and longitude.
    We have the points from the Zippopotam API request.

    The point web service response contains a long list of information
    for the forecast we only need two properties/forecast and
    properties/forecastHourly. These are the forecast end points
    which are formatted with the correct forecast office and
    point. For New York the office is OKX and location is 32/36
    https://api.weather.gov/gridpoints/OKX/32,36/forecast
    https://api.weather.gov/gridpoints/OKX/32,36/forecast/hourly

    The response contains the forecast. The program parses the
    json to find the weather properties to use.

    To show the weather is a formatted table the program uses
    prettytable. This library contains functions to load data
    and then print the table using the properties that were set.

    After viewing the weather the user can enter 9 on the menu
    and the program will end.




    The program inputs a zip code.
    After getting the zip code it makes a request to a web service
    get the latitude and longitude.
    Once getting the correct latitude and longitude the program
    can get either the weekly or hourly weather forecast from
    the National Weather Service.


    1) Get Daily forecast
    2) Get Hourly forecast
    9) Exit

Option: 9

Weather for New York, NY

*** Hourly Forecast *************
┌──────────┬──────┬──────────┬───────────────────────────────┐
│ Hour     │ Temp │ Wind     │ Forecast                      │
├──────────┼──────┼──────────┼───────────────────────────────┤
│ 23:00:00 │ 34F  │ E 5 mph  │ Mostly Cloudy                 │
│ 00:00:00 │ 34F  │ NE 5 mph │ Mostly Cloudy                 │
│ 01:00:00 │ 34F  │ NE 5 mph │ Mostly Cloudy                 │
│ 02:00:00 │ 35F  │ NE 3 mph │ Cloudy                        │
│ 03:00:00 │ 35F  │ N 3 mph  │ Slight Chance Very Light Rain │
│ 04:00:00 │ 36F  │ NE 5 mph │ Slight Chance Very Light Rain │
│ 05:00:00 │ 36F  │ N 3 mph  │ Slight Chance Very Light Rain │
│ 06:00:00 │ 37F  │ E 5 mph  │ Slight Chance Very Light Rain │
│ 07:00:00 │ 37F  │ E 5 mph  │ Chance Very Light Rain        │
│ 08:00:00 │ 39F  │ E 5 mph  │ Chance Very Light Rain        │
└──────────┴──────┴──────────┴───────────────────────────────┘

Weather for New York, NY

*** Daily Forecast *************
┌───────────────────┬──────┬───────────┬───────────────────────────┐
│ Day               │ Temp │Wind       │Forecast                   │
├───────────────────┼──────┼───────────┼───────────────────────────┤
│ Tonight           │ 34F  │ NE 5 mph  │ Mostly Cloudy  Light Rain │
│ Thursday          │ 53F  │ SE 5 mph  │ Light Rain                │
│ Thursday Night    │ 49F  │ S 8 mph   │ Rain                      │
│ Friday            │ 53F  │ SW mph    │ Rain then Partly Sunny    │
│ Friday Night      │ 31F  │ NW 10 mph │ Partly Cloudy             │
│ Saturday          │ 39F  │ NW 9  mph │ Chance Snow Showers       │
│ Saturday Night    │ 27F  │ N 10 mph  │ Partly Cloudy             │
│ Sunday            │ 42F  │ N 9  mph  │ Sunny                     │
│ Sunday Night      │ 26F  │ N 5 mph   │ Mostly Clear              │
│ Monday Day        │ 44F  │ NW 5 mph  │ Mostly Sunny              │
└───────────────────┴──────┴───────────┴───────────────────────────┘


