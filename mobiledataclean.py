import pandas as pd

# Load dataset
df = pd.read_csv("mobile_phones_data.csv")

# Drop duplicates
df.drop_duplicates(subset=["ItemID", "UserID"], inplace=True)

# Handle missing titles or prices
df["Title"].fillna("Unknown", inplace=True)
df["Price"].replace(["", "No price"], pd.NA, inplace=True)
df.dropna(subset=["Price"], inplace=True)

# Convert price to numeric (remove currency symbols, commas)
df["Price"] = df["Price"].str.replace("[^0-9.]", "", regex=True).astype(float)