import requests # install this package using 'pip install requests'

# http://open-notify.org/Open-Notify-API/ISS-Location-Now/

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response) # it will print a 200 response code (like 404)

# 1XX : Hold on 
# 2XX : Here you go
# 3XX : Go Away
# 4XX : You screwed up
# 5XX : I screwed up

response.raise_for_status() 

data = response.json()
print(data)
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)

# To detect where is the location go to this website: https://www.latlong.net/Show-Latitude-Longitude.html
