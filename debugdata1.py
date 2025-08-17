import csv

if gogebeya_dataset.csv:  # Check if list is not empty
    with open("gogebeya_dataset.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Category", "Title", "Price"])  # Header
        writer.writerows(gogebeya_dataset.csv)
else:
    print("gogebeya_dataset.csv. CSV not written.")