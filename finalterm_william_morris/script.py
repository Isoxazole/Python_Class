""""
This file will do the API call to get the image URL from the city as argument

"""

import json
import requests

image_ext = ['jpg', 'png']
def getcities():
    url = "https://api.teleport.org/api/urban_areas/"
    response = requests.get(url)
    response.raise_for_status()
    data = json.loads(response.text)

    cityData = data["_links"]["ua:item"]
    file = open("data.txt", "w")
    for i in cityData:
        file.write(i['name'] + " ")
    file.close()