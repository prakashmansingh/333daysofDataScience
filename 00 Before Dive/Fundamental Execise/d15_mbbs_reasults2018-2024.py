import pandas as pd
import matplotlib.pyplot as plt

#just read csv file of mbbs entrance result of 2018 to 2024
df = pd.read_csv('mbbs_results.csv')
print(df.head())
print(df.info()) 

# Count number of students who passed each year
passed_per_year = df[df['Passed'] == 'Yes'].groupby('Year').size()
print("Students Passed Each Year:")
print(passed_per_year)

# lets Plot students who passed per year
plt.figure(figsize=(8, 5))
passed_per_year.plot(kind='bar', color='brown')
plt.xlabel('Year')
plt.ylabel('Number of Students Passed')
plt.title('Number of Students Passed Each Year')
plt.xticks(rotation=45)
plt.show()

#  subjects with highest and lowest average scores
subject_scores = df[['Biology', 'Chemistry', 'Physics', 'English']].mean()
lowest_score_subject = subject_scores.idxmin()
highest_score_subject = subject_scores.idxmax()

print(f"Lowest Scoring Subject: {lowest_score_subject} ({subject_scores.min():.2f})")
print(f"Highest Scoring Subject: {highest_score_subject} ({subject_scores.max():.2f})")

#lets Plot subject scores
plt.figure(figsize=(8, 5))
subject_scores.plot(kind='bar', color=['red' if subj == lowest_score_subject else 'green' for subj in subject_scores.index])
plt.xlabel('Subjects')
plt.ylabel('Average Score')
plt.title('Average Scores by Subject')
plt.xticks(rotation=45)in 
plt.show()
