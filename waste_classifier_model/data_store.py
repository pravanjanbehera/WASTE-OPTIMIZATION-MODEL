import csv
import os
from datetime import datetime

FILE_NAME = "waste_data.csv"

def save_waste_data(area, waste_type, impact):
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["date", "area", "waste_type", "impact"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d"),
            area,
            waste_type,
            impact
        ])
