import pandas as pd

FUR_COLOR_01 = 'Primary Fur Color'

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(data[FUR_COLOR_01].unique())
fur_gray = len(data[data['Primary Fur Color'] == 'Gray'])
color_total = data['Primary Fur Color'].value_counts()
print(color_total)

gray = len(data[data['Primary Fur Color'] == 'Gray'])
black = len(data[data['Primary Fur Color'] == 'Black'])
cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])

color_dict = {
    "Fur color": ['Gray', 'Black', 'Cinnamon'],
    "Count": [gray, black, cinnamon]
}

df_color = pd.DataFrame(color_dict)
df_color.to_csv("color_fur.csv")