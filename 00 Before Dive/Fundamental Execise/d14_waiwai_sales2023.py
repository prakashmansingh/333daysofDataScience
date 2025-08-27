import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("wai_wai_sales_nepal.csv", parse_dates=["Date"])

print(df.head())
print("\nData Summary:")
print(df.describe())

# Time series analysis
plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Sales"], label="Daily Sales", color='blue')
plt.xlabel("Date")
plt.ylabel("Sales Volume")
plt.title("Wai Wai Daily Sales Trends in Nepal (2023)")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# Regional sales distribution
regions = df["Region"].unique()
region_sales = [df[df["Region"] == region]["Sales"].values for region in regions]

plt.figure(figsize=(8, 5))
plt.boxplot(region_sales, labels=regions )
plt.title("Sales Distribution by Region")
plt.xlabel("Region")
plt.ylabel("Sales Volume")
plt.xticks(rotation=45)
plt.show()

# Price impact on sales
prices = df["Price_Per_Pack"].unique()
total_sales = [df[df["Price_Per_Pack"] == price]["Sales"].sum() for price in prices]

plt.figure(figsize=(6, 4))
plt.bar(prices, total_sales, color='purple')
plt.title("Total Sales by Price Point")
plt.xlabel("Price Per Pack (NPR)")
plt.ylabel("Total Sales")
plt.show()
