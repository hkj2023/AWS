import pandas as pd
import random
from datetime import datetime

# Load the original CSV
file_path = "C:/Users/dasal/Desktop/Third Semister/Adaptive Web System/AWS/mobile_phones_data.csv"
df = pd.read_csv(file_path)

# Assign UserId
df["UserId"] = ["U{:03d}".format(i+1) for i in range(len(df))]

# Extract ItemId from URL
df["ItemId"] = df["URL"].apply(lambda x: x.split("/")[-1] if pd.notnull(x) else f"item_{random.randint(1000,9999)}")

# Assign InteractionType with weighted probabilities
interaction_types = ["View", "Click", "Purchase", "AddToCart"]
weights = [0.10, 0.15, 0.50, 0.25]
df["InteractionType"] = random.choices(interaction_types, weights, k=len(df))

# Assign Timestamp
df["TimeStamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Assign ProductCategory
df["ProductCategory"] = "Mobile Phones"

# Assign Rating (simulate positive feedback)
df["Rating"] = [round(random.uniform(3.0, 5.0), 1) for _ in range(len(df))]

# Select and reorder columns
final_df = df[["UserId", "ItemId", "InteractionType", "TimeStamp", "ProductCategory", "Rating"]]

# Save to new CSV
output_path = "C:/Users/dasal/Desktop/Third Semister/Adaptive Web System/AWS/mobile_transformed.csv"
final_df.to_csv(output_path, index=False)

print("Transformed file saved to:", output_path)