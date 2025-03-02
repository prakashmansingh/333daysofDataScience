import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (Replace with actual file path)
df = pd.read_csv('fuel_prices_nepal_2015_2024.csv', parse_dates=['Date'])
df = df.sort_values(by='Date')
df.info()
print(df.head())

# Handling missing values 
df.fillna(method='ffill', inplace=True)

# Calculate moving averages for trend analysis
df['Petrol_MA'] = df['Petrol Price (NPR)'].rolling(window=6).mean()
df['Diesel_MA'] = df['Diesel Price (NPR)'].rolling(window=6).mean()

# Calculate percentage change in prices
df['Petrol_Change'] = df['Petrol Price (NPR)'].pct_change() * 100
df['Diesel_Change'] = df['Diesel Price (NPR)'].pct_change() * 100

# Identify periods of high inflation (sharp price increases)
df['High Petrol Inflation'] = df['Petrol_Change'] > df['Petrol_Change'].quantile(0.90)
df['High Diesel Inflation'] = df['Diesel_Change'] > df['Diesel_Change'].quantile(0.90)

# Summary statistics
print(df.describe())

# Visualization
plt.figure(figsize=(14,6))
plt.plot(df['Date'], df['Petrol Price (NPR)'], label='Petrol Price', marker='o', color='blue', alpha=0.6)
plt.plot(df['Date'], df['Diesel Price (NPR)'], label='Diesel Price', marker='s', color='green', alpha=0.6)
plt.plot(df['Date'], df['Petrol_MA'], label='Petrol 6-Month MA', linestyle='dashed', color='red')
plt.plot(df['Date'], df['Diesel_MA'], label='Diesel 6-Month MA', linestyle='dashed', color='orange')
plt.xlabel('Date')
plt.ylabel('Price (NPR)')
plt.title('Fuel Price Trends in Nepal (2015-2024)')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Histogram to see price distribution
plt.figure(figsize=(10,5))
plt.hist(df['Petrol Price (NPR)'], bins=20, alpha=0.5, label='Petrol', color='blue')
plt.hist(df['Diesel Price (NPR)'], bins=20, alpha=0.5, label='Diesel', color='green')
plt.xlabel('Price (NPR)')
plt.ylabel('Frequency')
plt.title('Fuel Price Distribution in Nepal (2015-2024)')
plt.legend()
plt.grid()
plt.show()

# Correlation between petrol and diesel prices
correlation = df[['Petrol Price (NPR)', 'Diesel Price (NPR)']].corr()
print("Correlation between petrol and diesel prices:")
print(correlation)

# Visualizing correlation using heatmap
plt.figure(figsize=(6,5))
sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap: Petrol vs Diesel Prices")
plt.show()

# Scatter plot to visualize correlation
plt.figure(figsize=(8,6))
plt.scatter(df['Petrol Price (NPR)'], df['Diesel Price (NPR)'], alpha=0.5, color='purple')
plt.xlabel('Petrol Price (NPR)')
plt.ylabel('Diesel Price (NPR)')
plt.title('Scatter Plot of Petrol vs Diesel Prices in Nepal')
plt.grid()
plt.show()

# Detecting periods of high inflation
high_inflation_periods = df[df['High Petrol Inflation'] | df['High Diesel Inflation']]
print("High Inflation Periods:")
print(high_inflation_periods[['Date', 'Petrol Price (NPR)', 'Diesel Price (NPR)', 'Petrol_Change', 'Diesel_Change']])

# Save the processed data
df.to_csv('processed_fuel_prices_nepal_2015_2024.csv', index=False)
