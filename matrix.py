import pandas as pd

# Load the transformed dataset
file_path = "C:/Users/dasal/Desktop/Third Semister/Adaptive Web System/AWS/mobile_phones_transformed.csv"
df = pd.read_csv(file_path)

# Create User-Item Rating Matrix
rating_matrix = df.pivot_table(index="UserId", columns="ItemId", values="Rating", fill_value=0)

# Save to CSV
matrix_path = "C:/Users/dasal/Desktop/Third Semister/Adaptive Web System/AWS/user_item_rating_matrix.csv"
rating_matrix.to_csv(matrix_path)

print("✅ Rating matrix saved to:", matrix_path)