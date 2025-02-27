"""
    pip install pandas
    Use the above command to install pandas in a virtual environment.

    
    To figure out how many gray squirrels there are in total, how many cinnamon ones and how many black ones 
    based on that primary fur color column. And then you're gonna take that data and build a new data frame from it,
    and using that, create this final CSV using pandas.

"""

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240813.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
