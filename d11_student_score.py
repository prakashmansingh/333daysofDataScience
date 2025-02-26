import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(0)
num_students = 30
student_names = [f'Student {i+1}' for i in range(num_students)]
student_scores = np.random.randint(50, 100, size=num_students)

# Create a DataFrame with student names and scores
df = pd.DataFrame({
    'Student Names': student_names,
    'Scores': student_scores
})

average_score = df['Scores'].mean()
highest_score = df['Scores'].max()
lowest_score = df['Scores'].min()

print(df)
print(f"\nAverage Score: {average_score:.2f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")

plt.figure(figsize=(10, 6))
plt.hist(df['Scores'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Student Scores')
plt.xlabel('Scores')
plt.ylabel('Number of Students')
plt.grid(axis='y', alpha=0.75)
plt.show()