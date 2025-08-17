import pandas as pd

# Load the dataset
df = pd.read_csv("kaggle_final_products.csv")

# Drop rows with missing values in critical columns
df.dropna(subset=['UserID', 'ItemID', 'Rating'], inplace=True)

# Save cleaned dataset
df.to_csv("kaggle_products_cleaned_no_nulls.csv", index=False, encoding="utf-8")

print("✅ Null values removed. Clean file saved as kaggle_final_products.csv")
