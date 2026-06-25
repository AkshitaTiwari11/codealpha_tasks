import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset from Task 1
csv_path = "CodeAlpha_Scraped_Books.csv"

if not os.path.exists(csv_path):
    print(f"Error: '{csv_path}' not found! Make sure it is in this folder.")
else:
    # Read the data and clean the price column
    df = pd.read_csv(csv_path)
    df['Price'] = df['Price'].astype(str).str.replace('$', '', regex=False).astype(float)

    # 2. Setup the layout (1 row, 2 columns of charts)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Task 2: Books Dataset Analysis Dashboard", fontsize=16, fontweight='bold')

    # Chart 1: Price Distribution (Histogram)
    sns.histplot(df['Price'], bins=8, kde=True, color='skyblue', ax=axes[0])
    axes[0].set_title("How Book Prices are Distributed")
    axes[0].set_xlabel("Price ($)")
    axes[0].set_ylabel("Count")

    # Chart 2: Top 5 Most Expensive Books (Bar Chart)
    top_5 = df.nlargest(5, 'Price')

    # Fixed Warning: Explicitly assigned hue and set legend=False
    sns.barplot(x='Price', y='Book Title', data=top_5, palette="Reds_r", hue='Book Title', legend=False, ax=axes[1])
    axes[1].set_title("Top 5 Most Expensive Books")
    axes[1].set_ylabel("")  # Hide the vertical label to keep it clean

    # Fixed Warning: Setting tick locations explicitly before changing labels
    axes[1].set_yticks(range(len(top_5)))
    axes[1].set_yticklabels([title[:20] + '...' if len(title) > 20 else title for title in top_5['Book Title']])

    # Keep layout neat and show the charts
    plt.tight_layout()
    plt.show()