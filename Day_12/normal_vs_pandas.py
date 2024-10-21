# with open("weather_data.csv") as weather_data:
#     lines = weather_data.readlines()
#     print( lines)

import csv

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    # print( data)
    temperature = []
    for row in data:
        # print(row)
        if row[1] != 'temp':
            temperature.append(int(row[1]))
    print(temperature)


# Using such method for a larger dataset is quite painful

# So we use PANDAS


import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print("\n")
print(data["temp"])