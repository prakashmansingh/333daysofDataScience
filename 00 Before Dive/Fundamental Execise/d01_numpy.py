import numpy as np

# Temperature readings for a week (Morning, Afternoon, Evening, Night)
temperature_data = np.array([
    [15, 20, 18, 16],  # Day 1
    [17, 22, 20, 18],  # Day 2
    [16, 21, 19, 17],  # Day 3
    [14, 19, 17, 15],  # Day 4
    [18, 24, 22, 20],  # Day 5
    [20, 25, 23, 21],  # Day 6
    [19, 23, 21, 19]   # Day 7
])


# Average temperature for each day
avg_temp_per_day = np.mean(temperature_data, axis=1)

# Maximum and minimum temperature for the week
max_temp = np.max(temperature_data)
min_temp = np.min(temperature_data)

# Identify the hottest and coldest days
hottest_day = np.argmax(avg_temp_per_day) + 1
coldest_day = np.argmin(avg_temp_per_day) + 1

print("Average temperature per day:", avg_temp_per_day)
print("Maximum temperature of the week:", max_temp)
print("Minimum temperature of the week:", min_temp)
print(f"Hottest day: Day {hottest_day}")
print(f"Coldest day: Day {coldest_day}")

