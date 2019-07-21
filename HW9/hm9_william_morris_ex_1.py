import json
import requests
import threading
import datetime
import smtplib
import time


# Define the api info for getting the weather info (colorado is used here for weather)
apikey = "df8e2f4326f2d9286ec60516dd789fd3"
coloradoID = "5417598"
url = f"https://api.openweathermap.org/data/2.5/forecast?id={coloradoID}&APPID={apikey}"


def checkWeather():
    response = requests.get(url)
    response.raise_for_status()

    # load json info that was sent back by api
    weatherData = json.loads(response.text)

    # Display the weather info from the api info returned
    w = weatherData['list']

    tomorrowWeather = w[1]['weather'][0]['main'].lower()

    message = ""

    if 'rain' in tomorrowWeather:
        message = "Make sure to bring an umbrella!"

    elif 'snow' in tomorrowWeather:
        message = "It's cold, make sure to bundle up!"

    # security settings of email account must be changed to access
    # email account this way (for gmail)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("wmorris1367@gmail.com", "myPassword")

    # email self message
    server.sendmail(

        "wmorris1367@gmail.com",
        "wmorris1367@gmail.com",
        message
    )
    server.quit()
# checks weather and emails at 5am everyday


def checkTime():
    while True:
        currentTime = datetime.datetime.now()
        if currentTime.hour == 5 and currentTime.minute == 00:
            checkWeather()
        time.sleep(60)


threadObj = threading.Thread(target=checkTime)
threadObj.start()
    
    