import pandas as pd

# Load your dataset
df = pd.read_csv('kaggle_final_products.csv')

# Quick inspection
print(df.head())
print(df.info())