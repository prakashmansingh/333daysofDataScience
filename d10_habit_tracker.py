import pandas as pd

# Create a dataset tracking daily habits
data = {
    'Date': pd.date_range(start='2025-02-16', periods=7, freq='D'),
    'Reading (mins)': [30, 45, 20, 60, 40, 50, 35],
    'Coding (mins)': [120, 90, 150, 100, 80, 110, 90],
    'Exercise (mins)': [45, 30, 50, 40, 35, 25, 60],
    'meditation (mins)':[10, 12, 14, 10, 15 ,16, 18],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the first few rows
print("Daily Habit Tracker:\n", df)

# Calculate total time spent on all activities per day
df['Total Time (mins)'] = df[['Reading (mins)', 'Coding (mins)', 'Exercise (mins)', 'meditation (mins)']].sum(axis=1)

# Find the day with the highest total activity
best_day = df.loc[df['Total Time (mins)'].idxmax()]

print("\n Best Day for Productivity:\n", best_day)

# Calculate the average time spent on each activity
average_times = df[['Reading (mins)', 'Coding (mins)', 'Exercise (mins)','meditation (mins)']].mean()

print("\n Average Time Spent on Activities:\n", average_times)

# Save the data for further analysis
df.to_csv("daily_habits.csv", index=False)
