"""
Homework 8, Exercise 3
William Morris
3/17/19
This program downloads the weather forecast for the next few days for
a city and prints it as plain text
"""

#! python3

import json
import requests

# Define the api info for getting the weather info (colorado is used here for weather)
apikey = "df8e2f4326f2d9286ec60516dd789fd3"
coloradoID = "5417598"
url = f"https://api.openweathermap.org/data/2.5/forecast?id={coloradoID}&APPID={apikey}"
response = requests.get(url)
response.raise_for_status()

# load json info that was sent back by api
weatherData = json.loads(response.text)

# Display the weather info from the api info returned
w = weatherData['list']
print('Current weather in %s: ' % "Colorado")
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
