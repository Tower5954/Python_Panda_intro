# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])

import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

temp_list = data["temp"].to_list()


print(data["temp"].mean())
print(data["temp"].max())

#Get data in coloumns
print(data["condition"])
print(data.condition)

#Get data in row
print(data[data.day == "Monday"])
#Get the row with the max temp
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

#Create a DataFrame from scratch

data_dict2 = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 54, 59]
}

new_data = pandas.DataFrame(data_dict2)
data.to_csv("new_data.csv")