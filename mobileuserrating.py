import pandas as pd

# Load transformed dataset
file_path = "C:/Users/dasal/Desktop/Third Semister/Adaptive Web System/AWS/mobile_phones_transformed.csv"
df = pd.read_csv(file_path)

# Define interaction weights
interaction_weights = {
    "View": 1.0,
    "Click": 2.0,
    "AddToCart": 3.5,
    "Purchase": 5.0
}

# Map weights to interaction types
df["InteractionScore"] = df["InteractionType"].map(interaction_weights)

# Optional: Normalize timestamp (recent = higher score)
# For simplicity, we skip timestamp weighting here — can be added later

# Compute user-product rating by averaging interaction scores
user_rating_df = df.groupby(["UserId", "ItemId", "ProductCategory"]).agg({
    "InteractionScore": "mean"
}).reset_index()

# Rename for clarity
user_rating_df.rename(columns={"InteractionScore": "DerivedRating"}, inplace=True)

# Save to CSV
output_path = "C:/Users/dasal/Desktop/Third Semister/Adaptive Web System/AWS/user_behavior_ratings.csv"
user_rating_df.to_csv(output_path, index=False)

print("✅ User behavior-based rating file saved to:", output_path)