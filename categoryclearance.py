import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("kaggle_products_final.csv")

# Define your 10 fixed categories
categories = [
    'Mobile-phone', 'Tablet', 'Laptop', 'Desktop',
    'Women-fashion', 'Men-fashion', 'Kids',
    'Home-furniture', 'Smart-TV', 'Smart-watch'
]

# Randomly assign each product to one of these categories
np.random.seed(42)  # optional, for reproducibility
df['ProductCategory'] = np.random.choice(categories, size=len(df))

# Save updated dataset
df.to_csv("kaggle_final_products.csv", index=False)

print("✅ Random ProductCategory assigned and saved to 'kaggle_final_products.csv'")
