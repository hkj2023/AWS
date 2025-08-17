# Jiji Ethiopia Scraper using Edge
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pandas as pd
import time
import uuid
from datetime import datetime

# === Configuration ===
BASE_URL = "https://jiji.com.et"

CATEGORIES = {
    "electronics": "electronics",
    "smartphones": "mobile-phones-tablets",
    "vehicles": "vehicles",
    "fashion": "fashion-and-beauty",
    "furniture": "home-garden",
    "beauty": "health-and-beauty",
    "hobbies": "hobbies-art-sport",
    "agriculture": "agriculture-and-foodstuff",
    "kids": "babies-and-kids"
}

# === Setup Edge with webdriver_manager ===
driver_path = r"C:\Users\dasal\Desktop\Third Semister\Adaptive Web System\AWS\edgedriver_win64\msedgedriver.exe"
service = Service(driver_path)

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

driver = webdriver.Edge(service=service, options=options)
driver.get("https://jiji.com.et")

# === Data storage ===
data = []

# === Scraping loop ===
for category_name, category_slug in CATEGORIES.items():
    page = 1
    while True:
        url = f"{BASE_URL}/{category_slug}?page={page}"
        print(f"Scraping category: {category_name}, page {page}: {url}")
        driver.get(url)
        
        try:
            # Wait for products to load
            products = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "b-advert-listing js-advert-listing qa-advert-listing"))
                
            )
        except:
            print(f"No products found on page {page} for {category_name}. Moving to next category.")
            break
        
        if not products:
            break

        for product in products:
            try:
                title_elem = product.find_element(By.CSS_SELECTOR, "a.list-ad-title")
                price_elem = product.find_element(By.CSS_SELECTOR, "span.list-ad-price")
                link = title_elem.get_attribute("href")
                item_id = link.split("/")[-1].split("-")[0]  # numeric ID

                data.append({
                    "UserID": str(uuid.uuid4()),       # simulated user
                    "ItemID": item_id,
                    "InteractionType": "view",         # default interaction
                    "Timestamp": datetime.now().isoformat(),
                    "ProductCategory": category_name,
                    "Rating": None,
                    "Title": title_elem.text.strip(),
                    "Price": price_elem.text.strip(),
                    "ProductURL": link
                })
            except Exception as e:
                print("Error parsing product:", e)

        page += 1
        time.sleep(2)  # small delay

# === Finish ===
driver.quit()

# Save to CSV
if data:
    df = pd.DataFrame(data)
    df.to_csv("jiji_dataset.csv", index=False, encoding="utf-8")
    print("Scraping complete. Data saved to jiji_dataset.csv")
else:
    print("No data scraped.")
