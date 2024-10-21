import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print("\n")
# print(data["temp"])
print(type(data))           # <class 'pandas.core.frame.DataFrame'>
print(type(data["temp"]))   # <class 'pandas.core.series.Series'>

# Therer are 2 primary data structures of Pandas: Series(1D) and DataFrame (2D)
# Every single sheet or table is a DataFrame
# Every single columns in sheet or table is a Series


# Read the "API Reference" section in the pandas documentation

data_dict = data.to_dict()      # Convert data to dictionary
print(data_dict)

temperature_list = data["temp"].to_list()  # Convert data to list
print(temperature_list)

# Let's calculate the average temperature

average_temperature = sum(temperature_list) / len(temperature_list)
print(f"Average temperature: {average_temperature}")

# Let's calculate the average temperature using PANDAS

print(data["temp"].mean())

print(data["temp"].max())

# print(data.condition) # instead of writing print(data["condition"])

# Now how to  print a row ?

print(data[data.day == 'Monday'])

# Now let's print the day having max temperature

print(data[data.temp == data.temp.max()])

# Now let's print a particular day's conditon

monday = data[data.day == "Monday"]
print(monday.condition)


# HOW TO CREATE A DataFrame FROM SCRATCH (Previously we did from a CSV file)

data_dict_1 = {
    "Name" : ["Paul", "Abhijeet", "Deny" , "Morris"],
    "Age" : [25, 30, 28, 35]
}

data_frame_1 = pandas.DataFrame(data_dict_1)

print(data_frame_1)

data_frame_1.to_csv("new_csv_file.csv")