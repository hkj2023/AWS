import pandas as pd
from sklearn.model_selection import train_test_split

# Load encoded dataset
df = pd.read_csv("kaggle_encoded_final_products.csv")   # 👈 make sure file exists in your folder

# Split into train and test
train, test = train_test_split(df, test_size=0.2, random_state=42)

print("✅ Dataset split complete")
print("Training set size:", len(train))
print("Test set size:", len(test))

# Save for later use
train.to_csv("train.csv", index=False)
test.to_csv("test.csv", index=False)
