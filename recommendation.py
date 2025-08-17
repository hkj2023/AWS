import pandas as pd
from scipy.sparse import csr_matrix
from implicit.als import AlternatingLeastSquares

# === 1. Load and Prepare Data ===
df = pd.read_csv("kaggle_final_products.csv")
df.columns = df.columns.str.strip()
df['UserID'] = df['UserID'].astype(int)  # Ensure UserID is integer

# === 2. Map User and Item IDs to Indices ===
user_mapping = {user_id: idx for idx, user_id in enumerate(df['UserID'].unique())}
item_mapping = {item_id: idx for idx, item_id in enumerate(df['ItemID'].unique())}

df['user_idx'] = df['UserID'].map(user_mapping)
df['item_idx'] = df['ItemID'].map(item_mapping)

# === 3. Create Sparse Matrix (User-Item) ===
sparse_train_csr = csr_matrix(
    (df['Rating'], (df['user_idx'], df['item_idx'])),
    shape=(len(user_mapping), len(item_mapping))
)

# === 4. Train ALS Model ===
model = AlternatingLeastSquares(factors=50, regularization=0.01, iterations=20)
model.fit(sparse_train_csr)  # ✅ Correct orientation: user-item matrix

# === 5. Recommendation Function ===
def recommend_for_user(user_id, N=5, debug=False):
    if user_id not in user_mapping:
        raise ValueError(f"User ID {user_id} not found in dataset.")
    
    user_idx = user_mapping[user_id]

    if debug:
        print("🔍 Debug Info:")
        print("Matrix shape:", sparse_train_csr.shape)
        print("User index:", user_idx)

    recommended = model.recommend(user_idx, sparse_train_csr, N=5)
    reverse_item_mapping = {idx: item_id for item_id, idx in item_mapping.items()}
    results = [(reverse_item_mapping[item_idx], score) for item_idx, score in recommended]
    
    return results

# === 6. Run Recommendation ===
user_id_input = "794"  # ✅ Integer input

if user_id_input not in df['UserID'].values:
    print(f"User ID {user_id_input} not found in dataset.")
    print("✅ Available user IDs:", df['UserID'].unique())
else:
    top_items = recommend_for_user(user_id_input, N=5, debug=True)

    print("\nTop recommended items:")
    for item_id, score in top_items:
        print(f"Item: {item_id}, Score: {score:.4f}")

    pd.DataFrame(top_items, columns=["item_id", "score"]).to_excel("recommendations.csv", index=False)