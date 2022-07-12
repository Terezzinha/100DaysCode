import pandas as pd 

data = pd.read_csv("weather_data.csv")

# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)

# media = data["temp"].mean()
# print(media)

# mediana = data["temp"].median()
#print(mediana)

#print(data[data.day == "Monday"])

#print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
#print(monday.temp)
monday_temp = int(monday.temp)*(9/5) + 32

#print(monday_temp)

data_dict = {
    "student": ["Any", "jessy"],
    "score": [48, 12]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")