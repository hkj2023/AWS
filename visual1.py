import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/dasal/Desktop/Third Semister/Adaptive Web System/AWS/user_behavior_ratings.csv")

# Drop missing ratings
df = df.dropna(subset=["DerivedRating"])

# Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(df["DerivedRating"], bins=10, color="skyblue", edgecolor="black")
plt.title("Distribution of Derived Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()