import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_parameters = {
    "lat": 20.296059,
    "lon": 85.824539,
    "appid": "{Your API ID}",
    "cnt": 4
}

response = requests.get(OWM_endpoint, params=weather_parameters)
print(response.status_code)
# print(response.json())  # Prints the exact error if any
# You can see the JSON in a nice format in https://jsonviewer.stack.hu/


# After reading the documentation of OWM API (https://openweathermap.org/weather-conditions),
# I came to know that the weather ids that are less than 700, are actually indicated raining

weather_data = response.json()
# weather_list = weather_data["list"][0]["weather"][0]["id"] (write the structure by looking the JSON format)
weather_list = weather_data["list"]

will_rain = False
for hour in weather_list:
    weather_id = hour["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
        # print(f"It will rain at {hour['dt_txt']}, beacuse weather id = {weather_id}")
    # else:
    #     print(f"It will not rain at {hour['dt_txt']}, beacuse weather id = {weather_id}")
if will_rain:
    print(f"It will not rain at {hour['dt_txt']}. Bring an Umbrella")
# You can check the whether it's correct or not by adding a place where it's raining
# from this website: https://www.ventusky.com/?p=22.1;85.6;5&l=temperature-2m


