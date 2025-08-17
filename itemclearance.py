import pandas as pd
import numpy as np

# Load your dataset
df = pd.read_csv("kaggle_products_cleaned1.csv")

# Replace 'UserID' with random integers
# For example, random numbers between 1 and 1000
np.random.seed(42)  # for reproducibility
df['ItemID'] = np.random.randint(1, 100001, size=len(df))

# Save the updated dataset
df.to_csv("kaggle_products_final.csv", index=False)

print("UserID column replaced with random numbers and saved to 'kaggle_products_final.csv'")
