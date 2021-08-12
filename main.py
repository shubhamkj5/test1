import pandas as pd

data=pd.read_csv("netflix_titles.csv")

cleaned_data=data.drop_duplicates(subset=["director","cast","country"])

print(data.shape,cleaned_data.shape)