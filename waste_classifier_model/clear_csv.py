import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "waste_data.csv")

if os.path.exists(CSV_PATH):
    os.remove(CSV_PATH)
    print("waste_data.csv cleared successfully")
else:
    print("waste_data.csv not found")
