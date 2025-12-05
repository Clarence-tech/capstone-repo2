import csv
from pathlib import Path

DATA_PATH = Path("data") / "sample_data.csv"

def analyze():
    if not DATA_PATH.exists():
        print(f"Data file not found: {DATA_PATH}")
        return

    total = 0
    failures = 0

    with DATA_PATH.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            if row.get("status", "").upper() == "FAIL":
                failures += 1

    print("=== Analysis Summary ===")
    print(f"Total events: {total}")
    print(f"Failed events: {failures}")
    if total > 0:
        rate = failures / total * 100
        print(f"Failure rate: {rate:.2f}%")

if __name__ == "__main__":
    analyze()

