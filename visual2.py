import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("kaggle_final_products.csv")  # or your dataset file

# Plot histogram of ratings
sns.histplot(df['Rating'], bins=10, kde=False, color='skyblue')
plt.title("Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()
