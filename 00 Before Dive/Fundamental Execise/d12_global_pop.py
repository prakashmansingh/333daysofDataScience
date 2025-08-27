import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic dataset
np.random.seed(42)
years = np.arange(1960, 2025)  # Years from 1960 to 2024
countries = ["USA", "China", "India", "Brazil", "Indonesia", "Germany", "UK", "Japan", "Russia", "Nigeria"]

data = []
# Generate random population data for each country
for country in countries:
    population = np.round(np.linspace(np.random.randint(50, 300), np.random.randint(500, 1500), len(years)), 2)
    data.extend(zip([country] * len(years), years, population))

df = pd.DataFrame(data, columns=["Country", "Year", "Population"]) # Create DataFrame

df["Growth"] = df.groupby("Country")["Population"].diff().fillna(0) # Calculate yearly population growth

# Get the top 10 fastest-growing countries in the most recent year
latest_year = df["Year"].max()
top_countries = df[df["Year"] == latest_year].nlargest(5, "Growth")[["Country", "Growth"]]

# Visualizing Population Growth Over Time
plt.figure(figsize=(10, 5))
for country in ["China", "India", "USA", "Brazil", "Nigeria"]:  
    country_data = df[df["Country"] == country]
    plt.plot(country_data["Year"], country_data["Population"], label=country)

plt.xlabel("Year")
plt.ylabel("Population (millions)")
plt.title("Synthetic Population Growth Over Time")
plt.legend()
plt.show()

# Visualizing Top 5 Fastest Growing Countries
plt.figure(figsize=(8, 5))
plt.barh(top_countries["Country"], top_countries["Growth"], color="green")
plt.xlabel("Population Growth (millions)")
plt.ylabel("Country")
plt.title("Top 5 Fastest Growing Countries in 2024")
plt.show()
