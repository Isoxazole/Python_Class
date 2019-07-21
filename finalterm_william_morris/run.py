import json
import requests
from python_class.finalterm_william_morris.script import getcities

api_key = "12439651-e41e243e56226f8612742e9a6"
image_ext = ['jpg', 'png']
cities = []
errorImage = "https://cdn.windowsreport.com/wp-content/uploads/2019/02/Ddkmd.sys-blue-screen-errors-in-Windows.jpg"
try:
    file = open("data.txt", "r")
    for i in file:
        cities.append(i)
    cities = cities[0].split()
    file.close()
except Exception:
    print("Dowloading cities")
    getcities()
    file = open("data.txt", "r")
    for i in file:
        cities.append(i)
    cities = cities[0].split()
    file.close()

def get_city_image_url(city_name):
    if city_name.title() not in cities:
        print("Sorry, image for your city was not found")
        return errorImage
    search_parameter = "+".join(city_name.split())
    url = f"https://pixabay.com/api/?key={api_key}&q={search_parameter}&image_type=photo"
    response = requests.get(url)
    response.raise_for_status()
    pictureData = json.loads(response.text)

    photo_url = pictureData['hits'][0]['largeImageURL']

    return photo_url
get_city_image_url("Barcelona")