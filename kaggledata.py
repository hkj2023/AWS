import os
import pandas as pd
import uuid
import random
from datetime import datetime
from kaggle.api.kaggle_api_extended import KaggleApi

# Optional: point to your custom config directory if needed
# os.environ["KAGGLE_CONFIG_DIR"] = r"C:\Users\dasal\Desktop\Third Semister\Adaptive Web System\AWS"

api = KaggleApi()
api.authenticate()

DATASETS = {
    "electronics": "datafiniti/electronic-products-prices",        # API-compatible
    "fashion": "ahmedgaitani/comprehensive-clothes-price-dataset", # API-compatible
    "catalog": "supratimnag06/shop-product-catalog"                # API-compatible
}

INTERACTIONS = ["view", "click", "purchase"]
all_data = []

for category, slug in DATASETS.items():
    print(f"Downloading {category} dataset from Kaggle: {slug}")
    try:
        api.dataset_download_files(slug, path=f"./data/{category}", unzip=True)
    except Exception as e:
        print(f"Failed to download {slug}: {e}")
        continue

    # Try loading the first CSV found in the directory
    import glob
    files = glob.glob(f"./data/{category}/*.csv")
    if not files:
        print(f"No CSV files found for {slug} in ./data/{category}")
        continue

    df = pd.read_csv(files[0])
    print(f"Loaded CSV for {category}, rows: {len(df)}")

    for idx, row in df.iterrows():
        all_data.append({
            "UserID": str(uuid.uuid4()),
            "ItemID": row.get("id", idx + 1),
            "ProductCategory": category,
            "Rating": row.get("rating", None),
            "Price": row.get("price", row.get("Price", None)),
            "InteractionType": random.choice(INTERACTIONS),
            "Timestamp": datetime.now().isoformat()
        })

final_df = pd.DataFrame(all_data)
final_df.to_csv("kaggle_products.csv", index=False, encoding="utf-8")

print("✅ Combined dataset saved as kaggle_products.csv")
