import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load your dataset
df = pd.read_csv("kaggle_final_products.csv")   # 👈 change file name if different

# Initialize encoders
user_enc = LabelEncoder()
item_enc = LabelEncoder()
interaction_enc = LabelEncoder()

# Encode categorical columns
df['user_idx'] = user_enc.fit_transform(df['UserID'])
df['item_idx'] = item_enc.fit_transform(df['ItemID'])
df['interaction_idx'] = interaction_enc.fit_transform(df['InteractionType'])

# Save the encoded dataset
df.to_csv("kaggle_encoded_final_products.csv", index=False)

print("✅ Encoding complete. Encoded dataset saved as kaggle_encoded_final_products.csv")
print(df.head())