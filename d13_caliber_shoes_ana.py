import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
df = pd.read_csv("caliber_shoes_sales.csv", parse_dates=['Date']) # Load sales dataset
# Data Preprocessing
df.dropna(inplace=True)  # Remove missing values
df['Month'] = df['Date'].dt.to_period('M')  # Extract month-year for trend analysis

# Monthly Sales Trend Analysis
monthly_sales = df.groupby('Month')['Sales'].sum()
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o', linestyle='-', color='b')
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend of Caliber Shoes")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Best-Selling Products Analysis
best_sellers = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
best_sellers.plot(kind='bar', color='g')
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Top 10 Best-Selling Caliber Shoes")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Seasonal Demand Analysis
seasonal_sales = df.groupby(df['Date'].dt.month)['Sales'].sum()
plt.figure(figsize=(10, 5))
plt.bar(seasonal_sales.index, seasonal_sales.values, color='orange')
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Seasonal Demand Pattern of Caliber Shoes")
plt.xticks(np.arange(1, 13, 1), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
plt.grid(axis='y')
plt.show()

print("Analysis Complete: Sales trends, best-selling products, and seasonal demand analyzed.")
