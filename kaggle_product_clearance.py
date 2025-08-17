import os
import pandas as pd
import uuid
import random
from datetime import datetime
from kaggle.api.kaggle_api_extended import KaggleApi
import glob

# Optional: point to your custom config directory if needed
# os.environ["KAGGLE_CONFIG_DIR"] = r"C:\Users\dasal\Desktop\Third Semister\Adaptive Web System\AWS"

api = KaggleApi()
api.authenticate()

DATASETS = {
    "electronics": "datafiniti/electronic-products-prices",        
    "fashion": "ahmedgaitani/comprehensive-clothes-price-dataset", 
    "catalog": "supratimnag06/shop-product-catalog"                
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

    # Load first CSV
    files = glob.glob(f"./data/{category}/*.csv")
    if not files:
        print(f"No CSV files found for {slug} in ./data/{category}")
        continue

    df = pd.read_csv(files[0], low_memory=False)
    print(f"Loaded CSV for {category}, rows: {len(df)}")

    for idx, row in df.iterrows():
        all_data.append({
            "UserID": str(uuid.uuid4()),
            "ItemID": row.get("id", idx + 1),
            "ProductCategory": category,
            # If missing, inject random rating and price
            "Rating": row.get("rating") if pd.notna(row.get("rating")) else random.randint(1, 10),
            "Price": row.get("price") if pd.notna(row.get("price")) else round(random.uniform(50, 5000), 2),
            "InteractionType": random.choice(INTERACTIONS),
            "Timestamp": datetime.now().isoformat()
        })

final_df = pd.DataFrame(all_data)
final_df.to_csv("kaggle_products_cleaned.csv", index=False, encoding="utf-8")

print("✅ Clean dataset saved as kaggle_products_cleaned.csv")
