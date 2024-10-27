# https://sunrise-sunset.org/api    (provides sunset and sunrise times for a given latitude and longitude)

import requests

parameters = {          # Take 'lat' and 'lng' since it is the format of that API
    'lat': 20.951666,
    'lng': 85.098526,
}   # Odisha 

response = requests.get("https://api.sunrise-sunset.org/json", params = parameters) # It will not work without parameters
response.raise_for_status()
data = response.json()
print(data)



