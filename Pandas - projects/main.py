#import csv
import pandas



# with open("weather_data.csv") as weather_data:
#     data=weather_data.readlines()
#     for data in data:
#         stripped_data=data.strip()
#         print(data)

# with open("weather_data.csv") as weather_data:
#     reader = csv.reader(weather_data)
#     temperatures = []
#     for row in reader:
#         new=row[1]
#         if new=="temp":
#             continue
#         new_int=int(new)
#         temperatures.append(new_int)
#
#     print(temperatures)


#data = pandas.read_csv("weather_data.csv")
# temp_list=data["temp"].tolist()
# print(temp_list)
# avg_temp=sum(temp_list)/len(temp_list)
# print(round(avg_temp,2))
# print(data["temp"].max())

#print(data[data.temp == max(data.temp)])

# monday = data[data.day=='Monday']
# temp_in_celsius=monday.temp[0]
# fahrenheit = temp_in_celsius * 9/5 + 32
# print(temp_in_celsius)
# print(fahrenheit)

data= pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count=len(data[data["Primary Fur Color"]=="Gray"])

Cinnamon=len(data[data["Primary Fur Color"]=="Cinnamon"])

Black=len(data[data["Primary Fur Color"]=="Black"])


dict_data = {'Fur_color': ['Gray','Cinnamon','Black'],
             'count':[gray_count,Cinnamon,Black]
}
table=pandas.DataFrame(dict_data)
table.to_csv("squirrel_count.csv")

#print(len(fur.groupby(level=0).count()))
#print(c1)