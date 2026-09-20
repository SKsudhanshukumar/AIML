import sqlite3
import pandas as pd
from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# File paths
CSV_PATH = BASE_DIR / "data" / "processed" / "retail_cleaned.csv"
DB_PATH = BASE_DIR / "data" / "retail_sales.db"


# Check whether CSV exists
if not CSV_PATH.exists():
    print("CSV file not found!")
    print("Expected location:")
    print(CSV_PATH)
    exit()


# Load cleaned data
df = pd.read_csv(CSV_PATH)

print("Dataset loaded successfully!")
print("Shape:", df.shape)


# Connect to SQLite database
connection = sqlite3.connect(DB_PATH)


# Load dataframe into SQLite
df.to_sql(
    "sales",
    connection,
    if_exists="replace",
    index=False
)


connection.close()

print("SQLite database created successfully!")
print("Database location:")
print(DB_PATH)