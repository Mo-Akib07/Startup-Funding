import pandas as pd
import numpy as np

df = pd.read_csv('startup_funding.csv')

df.drop(columns= ["Remarks"], inplace=True)
df.set_index("Sr No", inplace=True)
df.rename(columns= {
    "Date dd/mm/yyyy": "date",
    "Startup Name": "startup",
    "Industry Vertical": "vertical",
    "SubVertical": "sub_vertical",
    "City  Location" : "city",
    "Investors Name": "investors",
    "InvestmentnType": "round",
    "Amount in USD": "amount",
}, inplace=True)

df["amount"] = df["amount"].fillna("0")
df["amount"] = df["amount"].str.replace(",", "")
df["amount"] = df["amount"].replace('undisclosed', "0")
df["amount"] = df["amount"].replace('unknown', "0")
df["amount"] = df["amount"].replace('Undisclosed', "0")
df = df[df["amount"].str.isdigit()]
df["amount"] = df["amount"].astype("float")

df["date"] = df["date"].str.replace("05/072018", "05/07/2018")
df["date"] = pd.to_datetime(df["date"], errors= "coerce")

df = df.dropna(subset=["date", "startup", "vertical", "city", "investors", "round", "amount"])
print(df.info())

