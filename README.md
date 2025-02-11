Starting my data science journey, I explored NumPy, a key library for numerical computing. This project analyzes a week of temperature data, focusing on basic operations like averages and identifying the hottest and coldest days. It’s a small start, but I’m excited to dive deeper and take on bigger challenges ahead! 

🌡️ Weekly Temperature Analysis with NumPy:
 A simple data analysis project using NumPy to analyze and extract insights from a week of temperature data.

📝 Project Overview
This project uses NumPy to analyze daily temperature readings (morning, afternoon, evening, and night) for a week.
The analysis includes:

Calculating the average temperature for each day
Finding the maximum and minimum temperatures for the week
Identifying the hottest and coldest days based on the average temperature

📊 Data
The dataset consists of temperature readings for each day of the week at four different times:

Morning
Afternoon
Evening
Night

🛠️ Tools and Libraries
Python 3
NumPy

📈 Analysis and Results
Average temperature for each day
Maximum and minimum temperatures for the week
Hottest day
Coldest day


# Temperature readings for a week (Morning, Afternoon, Evening, Night)
temperature_data = np.array([
    [15, 20, 18, 16],
    [17, 22, 20, 18],
    [16, 21, 19, 17],
    [14, 19, 17, 15],
    [18, 24, 22, 20],
    [20, 25, 23, 21],
    [19, 23, 21, 19]
])


🔍 Key Findings
Hottest day: Day 6
Coldest day: Day 4
Maximum temperature: 25°C
Minimum temperature: 14°C
