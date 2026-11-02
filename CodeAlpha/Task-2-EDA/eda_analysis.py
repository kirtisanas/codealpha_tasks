
import pandas as pd
import numpy as np

# 1. Load dataset
df = pd.read_csv("Task-2-EDA/data/Data Set- Inc5000 Company List_2014.csv")

print("========== DATASET OVERVIEW ==========")

# 2. Dataset information
print("\nDataset Shape:", df.shape)
print("\nColumn Names:", df.columns.tolist())

print("\nDataset Information:")
df.info()

# 3. Missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# 4. Duplicate records
print("\n========== DUPLICATES ==========")
print("Duplicate Rows:", df.duplicated().sum())

# 5. Remove unnecessary columns
unwanted = [
    "_input", "_num", "_widgetName",
    "_source", "_resultNumber", "_pageUrl",
    "id", "url", "state_l", "metro"
]

df.drop(columns=unwanted, inplace=True, errors="ignore")

# 6. Statistical analysis
print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# 7. Industry analysis
print("\n========== TOP INDUSTRIES ==========")
print(df["industry"].value_counts().head(10))

# 8. State analysis
print("\n========== TOP 10 STATES ==========")
print(df["state_s"].value_counts().head(10))

# 9. Growth analysis
print("\n========== COMPANY GROWTH ==========")
print("Average Growth:", df["growth"].mean())
print("Highest Growth:", df["growth"].max())
print("Lowest Growth:", df["growth"].min())

# 10. Revenue analysis
print("\n========== REVENUE ANALYSIS ==========")
print("Average Revenue:", df["revenue"].mean())
print("Total Revenue:", df["revenue"].sum())

# 11. Top 10 companies
print("\n========== TOP 10 COMPANIES ==========")
print(
    df.nlargest(10, "growth")[["company", "growth", "revenue", "industry"]]
)

# 12. Save cleaned dataset
df.to_csv("Task-2-EDA/cleaned_inc5000.csv", index=False)

print("\n========== EDA COMPLETED ==========")
print("Cleaned dataset saved successfully!")

import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Create charts folder
chart_folder = Path("Task-2-EDA/charts")
chart_folder.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")

# Chart 1: Top 10 Industries
plt.figure(figsize=(10, 6))

industry_data = df["industry"].value_counts().head(10)

sns.barplot(x=industry_data.values, y=industry_data.index)

plt.title("Top 10 Industries by Company Count")
plt.xlabel("Number of Companies")
plt.ylabel("Industry")
plt.tight_layout()
plt.savefig(chart_folder / "top_industries.png")
plt.close()

# Chart 2: Top 10 States
plt.figure(figsize=(10, 6))

state_data = df["state_s"].value_counts().head(10)

sns.barplot(x=state_data.values, y=state_data.index)

plt.title("Top 10 States by Company Count")
plt.xlabel("Number of Companies")
plt.ylabel("State")
plt.tight_layout()
plt.savefig(chart_folder / "top_states.png")
plt.close()

# Chart 3: Company Growth Distribution
plt.figure(figsize=(10, 6))

sns.histplot(df["growth"], bins=40, kde=True)

plt.title("Distribution of Company Growth")
plt.xlabel("Growth Percentage")
plt.ylabel("Number of Companies")
plt.tight_layout()
plt.savefig(chart_folder / "growth_distribution.png")
plt.close()

# Chart 4: Revenue Distribution
plt.figure(figsize=(10, 6))

sns.histplot(df["revenue"], bins=40, kde=True)

plt.title("Distribution of Company Revenue")
plt.xlabel("Revenue (USD)")
plt.ylabel("Number of Companies")
plt.tight_layout()
plt.savefig(chart_folder / "revenue_distribution.png")
plt.close()

print("\nAll 4 charts saved successfully!")

