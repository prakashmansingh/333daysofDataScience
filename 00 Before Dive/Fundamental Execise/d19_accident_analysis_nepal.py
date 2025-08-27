import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Creating a sample dataset
data = {
    "Date": pd.date_range(start="2024-01-01", periods=100, freq="D"),
    "Location": np.random.choice(["Kathmandu", "Pokhara", "Chitwan", "Biratnagar", "Dharan"], 100),
    "Severity": np.random.choice(["Fatal", "Serious", "Minor"], 100, p=[0.2, 0.3, 0.5]),
    "Weather": np.random.choice(["Clear", "Rainy", "Foggy"], 100, p=[0.6, 0.3, 0.1]),
    "Vehicle_Type": np.random.choice(["Car", "Bike", "Bus", "Truck"], 100),
    "Time_of_Day": np.random.choice(["Morning", "Afternoon", "Evening", "Night"], 100),
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Display the first few rows
print("Sample Dataset:")
print(df.head())

# Data Cleaning: Checking for missing values
df.isnull().sum()

# Accident Severity Count
severity_count = df["Severity"].value_counts()
plt.figure(figsize=(6,4))
sns.barplot(x=severity_count.index, y=severity_count.values, palette="coolwarm")
plt.title("Accident Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.show()

# Accidents by Location
plt.figure(figsize=(8,5))
sns.countplot(y=df["Location"], order=df["Location"].value_counts().index, palette="viridis")
plt.title("Accidents by Location")
plt.xlabel("Count")
plt.ylabel("Location")
plt.show()

# Accidents by Time of Day
plt.figure(figsize=(6,4))
sns.countplot(x=df["Time_of_Day"], order=["Morning", "Afternoon", "Evening", "Night"], palette="muted")
plt.title("Accidents by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Count")
plt.show()

# Weather Impact on Accidents
plt.figure(figsize=(6,4))
sns.countplot(x=df["Weather"], hue=df["Severity"], palette="pastel")
plt.title("Impact of Weather on Accidents")
plt.xlabel("Weather Condition")
plt.ylabel("Count")
plt.legend(title="Severity")
plt.show()

# Conclusion
print("Key Findings:")
print("- Most accidents occur in", df["Location"].value_counts().idxmax())
print("- The most common accident severity is", severity_count.idxmax())
print("- Weather conditions play a role in accident severity")
