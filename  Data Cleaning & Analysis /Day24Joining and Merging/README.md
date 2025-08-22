# Day 24/333 – Merging & Joining Datasets

##  Overview
Today’s focus was on **merging and joining datasets**  a critical part of **Data Cleaning & Preprocessing**. In real-world scenarios, data often comes from multiple sources or files, and combining them properly is essential for accurate analysis.

---

##  Datasets Used
1. **students.csv** – Contains student details (ID, Name, Class, Marks in Math, Science, English).  
2. **attendance.csv** – Contains attendance records for students (ID, Attendance %).  
3. **student_performance.csv** – Merged dataset with average marks and attendance for reference.


---

##  Key Concepts Learned
- **Merging Datasets:** Combining two datasets based on a common key using `pd.merge()`.  
- **Join Types:**
  - **Inner Join:** Only matching records from both datasets.  
  - **Left Join:** All records from the left dataset + matching records from the right.  
  - **Right Join:** All records from the right dataset + matching records from the left.  
  - **Outer Join:** All records from both datasets, missing values filled with NaN.  
- **Concatenation:** Stacking datasets row-wise or column-wise using `pd.concat()`.  
- **Handling Missing Values:** Filling NaNs after merging to ensure clean analysis.

---

## 🔍 Analysis Performed
- Merged student details with attendance data.  
- Calculated **average marks** for each student.  
- Checked for missing attendance data and filled missing values.  
- Analyzed relationships between attendance and academic performance.

---

## 📊 Visualizations Created
1. **Scatterplot:** Attendance vs Average Marks  
2. **Barplot:** Top-performing students by average marks  
3. **Histogram:** Attendance distribution  
4. **Correlation Heatmap:** Relationships among subjects, attendance, and average marks  

---

## 💡 Key Takeaways
- Proper merging and joining ensures accurate and complete datasets for analysis.  
- Choice of join type affects the results and insights.  
- Visualizations help identify patterns and correlations quickly.  
- This step is essential before moving to **feature engineering and machine learning models**.

---



