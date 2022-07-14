import pandas as pd

FUR_COLOR_01 = 'Primary Fur Color'

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(data[FUR_COLOR_01].unique())
fur_gray = (data['Primary Fur Color'] == 'Gray')
print(data['Primary Fur Color'].value_counts())
print(data['Primary Fur Color'].size)