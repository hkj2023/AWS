import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("C:/Users/dasal/Desktop/Third Semister/Adaptive Web System/AWS/user_behavior_ratings.csv")

# Count interaction types
counts = df["InteractionType"].value_counts()
plt.bar(counts.index, counts.values, color="skyblue", edgecolor="black")
plt.xlabel("Interaction Type")
plt.ylabel("Frequency")
plt.title("Distribution of Interaction Types")
plt.show()
