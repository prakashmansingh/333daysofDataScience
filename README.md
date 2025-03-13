# 🌡️ Weekly Temperature Analysis with NumPy

This project utilizes **NumPy** to analyze daily temperature readings (morning, afternoon, evening, and night) for a week. It covers fundamental numerical operations such as calculating averages and identifying the hottest and coldest days.

## 📝 Project Overview

Using **NumPy**, this project processes and analyzes temperature data for a week to derive key insights, including:

- 📊 **Average temperature** for each day
- 🌡️ **Hottest and coldest days** based on average temperatures
- 🔥 **Maximum and minimum temperatures** recorded during the week

## 📊 Dataset

The dataset consists of temperature readings at four different times of the day:

- **Morning**
- **Afternoon**
- **Evening**
- **Night**

### Sample Temperature Data (°C)

```python
import numpy as np  

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
```

## 🛠️ Tools & Libraries

- **Python 3**  
- **NumPy**  

## 📈 Analysis & Results

- **Average temperature for each day:**
  ```python
  daily_avg = np.mean(temperature_data, axis=1)
  print(daily_avg)  # Example output
  ```
- **Hottest day:** Day 6  
- **Coldest day:** Day 4  
- **Maximum temperature recorded:** 25°C  
- **Minimum temperature recorded:** 14°C  

## 🔍 Key Insights

| Metric                | Value |
|-----------------------|------|
| 🔥 **Hottest Day**   | Day 6 |
| ❄️ **Coldest Day**  | Day 4 |
| 🌡️ **Max Temp**   | 25°C |
| 🌡️ **Min Temp**   | 14°C |

## 📸 Visualization (Optional)

To further enhance this analysis, you can visualize the data using **Matplotlib**:

```python
import matplotlib.pyplot as plt  

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
plt.plot(days, daily_avg, marker="o", linestyle="-", color="b", label="Avg Temp")  
plt.xlabel("Days of the Week")  
plt.ylabel("Temperature (°C)")  
plt.title("Weekly Temperature Trend")  
plt.legend()  
plt.grid()  
plt.show()
```

## 🚀 Conclusion

This simple project demonstrates how **NumPy** can be used for numerical computations and basic data analysis. As I continue my Data Science journey, I look forward to exploring more complex datasets and techniques!  

---

[![Project Image](https://www.openai.com)](https://www.openai.com)
