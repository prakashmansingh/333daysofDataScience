
import numpy as np  
import matplotlib.pyplot as plt  

# Simulate rolling two dice 10,000 times
num_rolls = 10000
die1 = np.random.randint(1, 7, num_rolls)  
die2 = np.random.randint(1, 7, num_rolls)  
sum_of_dice = die1 + die2  

# Count frequency of each outcome
values, counts = np.unique(sum_of_dice, return_counts=True)  

# Plot the probability distribution
plt.bar(values, counts / num_rolls, color='skyblue', edgecolor='black')  
plt.xlabel("Sum of Two Dice")  
plt.ylabel("Probability")  
plt.title("Probability Distribution of Two Dice Rolls")  
plt.xticks(range(2, 13))  
plt.show()  
