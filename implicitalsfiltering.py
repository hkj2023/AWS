import pandas as pd
from scipy.sparse import coo_matrix
from implicit.als import AlternatingLeastSquares

# Load the train dataset
train = pd.read_csv("train.csv")  # make sure this file exists

# Build the sparse user-item matrix
sparse_train = coo_matrix((train['Rating'], (train['user_idx'], train['item_idx'])))

# Initialize ALS model
model = AlternatingLeastSquares(factors=50, regularization=0.1, iterations=20)

# Train ALS (implicit expects item-user matrix)
model.fit(sparse_train.T)

print("✅ ALS model training complete")
