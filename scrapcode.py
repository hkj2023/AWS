# Jiji Ethiopia Scraper using Edge + BeautifulSoup (offline-safe)

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
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
MAX_PAGES = 5  # Adjust as needed

# === Setup Edge WebDriver (offline-safe) ===
def init_driver():
    driver_path = r"C:\Users\dasal\Desktop\Third Semister\Adaptive Web System\AWS\edgedriver_win64\msedgedriver.exe"
    service = Service(driver_path)

    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

    return webdriver.Edge(service=service, options=options)

# === Parse product block using BeautifulSoup ===
def parse_product_html(html, category_name):
    soup = BeautifulSoup(html, "html.parser")
    products = soup.select("div.list-item")
    parsed = []

    for product in products:
        try:
            title_tag = product.select_one("a.list-ad-title")
            price_tag = product.select_one("span.list-ad-price")
            link = BASE_URL + title_tag["href"]
            item_id = link.split("/")[-1].split("-")[0]

            parsed.append({
                "UserID": str(uuid.uuid4()),
                "ItemID": item_id,
                "InteractionType": "view",
                "Timestamp": datetime.now().isoformat(),
                "ProductCategory": category_name,
                "Rating": None,
                "Title": title_tag.get_text(strip=True),
                "Price": price_tag.get_text(strip=True),
                "ProductURL": link
            })
        except Exception as e:
            print("Error parsing product:", e)
    return parsed

# === Main scraping function ===
def scrape_jiji():
    driver = init_driver()
    all_data = []

    for category_name, category_slug in CATEGORIES.items():
        for page in range(1, MAX_PAGES + 1):
            url = f"{BASE_URL}/{category_slug}?page={page}"
            print(f"Scraping category: {category_name}, page {page}: {url}")
            driver.get(url)

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.list-item"))
                )
                html = driver.page_source
                products = parse_product_html(html, category_name)
                if not products:
                    print(f"No products found on page {page} for {category_name}.")
                    break
                all_data.extend(products)
            except Exception as e:
                print(f"Failed to load page {page} for {category_name}: {e}")
                break

            time.sleep(2)

    driver.quit()
    return all_data

# === Save to CSV ===
def save_to_csv(data, filename="jiji_dataset.csv"):
    if data:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding="utf-8")
        print(f"✅ Scraping complete. Data saved to {filename}")
    else:
        print("⚠️ No data scraped.")

# === Run ===
if __name__ == "__main__":
    scraped_data = scrape_jiji()
    save_to_csv(scraped_data)