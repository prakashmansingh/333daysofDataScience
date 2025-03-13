
import numpy as np
import matplotlib.pyplot as plt


days = np.arange(1, 211) # Simulating NEPSE stock market data for the last 7 months 
np.random.seed(42)  

prices = 2000 + np.cumsum(np.random.normal(0, 10, 210))  # Generate stock prices  (starting price NPR 2000)

daily_returns = np.diff(prices) / prices[:-1] * 100 # Calculate daily returns (percentage change)

def moving_average(prices, window): # Calculate moving averages (7-day, 30-day, 90-day)
    return np.convolve(prices, np.ones(window)/window, mode='valid')

mavg_7 = moving_average(prices, 7)
mavg_30 = moving_average(prices, 30)
mavg_90 = moving_average(prices, 90)


def rolling_volatility(returns, window): # Calculate rolling volatility (standard deviation of returns over 30 days)
    return np.array([np.std(returns[i-window:i]) for i in range(window, len(returns))])
vol_30 = rolling_volatility(daily_returns, 30)

day_max = days[np.argmax(prices)] # Find max and min stock prices
price_max = np.max(prices)
day_min = days[np.argmin(prices)]
price_min = np.min(prices)


# Plot stock prices and moving averages
plt.figure(figsize=(12, 6))
plt.plot(days, prices, label='NEPSE Stock Price', alpha=0.7)
plt.plot(days[6:], mavg_7, label='7-day Moving Average', color='red')
plt.plot(days[29:], mavg_30, label='30-day Moving Average', color='green')
plt.plot(days[89:], mavg_90, label='90-day Moving Average', color='blue')
plt.scatter(day_max, price_max, color='gold', label=f'Highest: NPR {price_max:.2f}', marker='^')
plt.scatter(day_min, price_min, color='black', label=f'Lowest: NPR {price_min:.2f}', marker='v')
plt.xlabel('Days')
plt.ylabel('Stock Price (NPR)')
plt.title('NEPSE Stock Price Analysis (Last 7 Months)')
plt.legend()
plt.grid()
plt.show()


# Plot volatility
days_vol = days[30:-1]
plt.figure(figsize=(12, 4))
plt.plot(days_vol, vol_30, label='30-day Volatility', color='purple')
plt.xlabel('Days')
plt.ylabel('Volatility (%)')
plt.title('NEPSE Stock Market Volatility Analysis (Last 7 Months)')
plt.legend()
plt.grid()
plt.show()
