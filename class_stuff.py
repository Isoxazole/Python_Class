import requests
import json
import sys
apikey =
coloradoID = "5417598"
url = f"api.openweathermap.org/data/2.5/forecast?id={coloradoID}&APPID={apikey}"

response = requests.get(url)
try:
    response.raise_for_status()
except Exception:
    print("Error retrieving url")
    sys.exit()
weatherData = json.loads(response.text)

w = weatherData['list']
print(w)