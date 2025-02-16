
#Shoe Size Trend Prediction with NumPy

import numpy as np

#here generating random shoe sizes for 50 customers (sizes between 36-45)
np.random.seed(50)  # Ensures consistent results
shoe_sizes = np.random.randint(36, 46, size=50)

print("Customer Shoe Sizes:", shoe_sizes)#print the shoe size of each customer


# Counting occurrences of each shoe size
unique_sizes, counts = np.unique(shoe_sizes, return_counts=True)

# Finding the most common shoe size
most_common_size = unique_sizes[np.argmax(counts)]

print("Shoe Size Counts:", dict(zip(unique_sizes, counts)))
print("Most Common Shoe Size:", most_common_size)


# Predicting future shoe sizes based on current distribution
future_shoe_sizes = np.random.choice(unique_sizes, size=20, p=counts/np.sum(counts)) #for future customer

# Counting the future shoe sizes
future_unique_sizes, future_counts = np.unique(future_shoe_sizes, return_counts=True)

# Finding the most common predicted size
predicted_most_common_size = future_unique_sizes[np.argmax(future_counts)]

print("Predicted Most Common Shoe Size for Future Sales:", predicted_most_common_size)
