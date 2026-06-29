import os
import pandas as pd

csv_path = "CodeAlpha_Scraped_Books.csv"

if not os.path.exists(csv_path):
    print(f"Error: '{csv_path}' not found! Make sure to run your scraper first.")
else:
    # Load the data
    df = pd.read_csv(csv_path)

    # Clean price column for calculations
    df['Price'] = df['Price'].astype(str).str.replace('$', '', regex=False).astype(float)

    print("\n--- TASK 2: EXPLORATORY DATA ANALYSIS (EDA) ---")

    # 1. Dataset Basic Info
    print("\n💡 1. Structure of the Dataset:")
    print(f"Total Books Scraped: {df.shape[0]}")
    print(f"Total Columns: {df.shape[1]} ({', '.join(df.columns)})")

    # 2. Check for missing values
    print("\n🔍 2. Missing Values Check:")
    print(df.isnull().sum())

    # 3. Statistical Summary of Prices
    print("\n📊 3. Statistical Summary of Book Prices:")
    print(df['Price'].describe())

    # 4. Show the first few rows
    print("\n📋 4. First 3 Rows of Data:")
    print(df.head(3))
