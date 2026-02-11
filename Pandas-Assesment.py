import pandas as pd

marks = [78, 85, 90, 66, 72]

series = pd.Series(marks)

print(series.values)
print(series.index)
print(type(series))
print(series.head(1))
print(series.tail(1))
# ===========================================================
#MathsMatics
series=series+5
print(series)

series=series-2
print(series)

series=series*1.05
print(series)

series=series/1.05
print(series)
#====================================================================
print(series.max())
print(series.min())
print(series.sum())
print(series.mean())

print(list(filter(lambda x:print(x) if x>=70 else None, series)))

TotalStudent = sum(1 for i, x in enumerate(series) if x >= 70)
print(TotalStudent)

# ===========================================================================

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}


df =pd.DataFrame(students)

print(df.head(3))
print(df.tail(2))

print(df.shape)       # prints (rows, columns)
print(df.columns)     # prints column names

# =======================================================================================

print(df.info)
print(df.describe())
print(df.head())
print(df.tail())
print(df.sort_values(df.columns[1],ascending=False))
print(df.sort_values(df.columns[0],ascending=True))

#======================================================================================
# Filtering and Conditinal selection

print(df[df["Marks"]>75])
print(df[df["Subject"]=="Math"])
print(df[df["Marks"]>df["Marks"].mean()])
print(df[df["Marks"]<70])

avg_marks = df.groupby('Subject')['Marks'].mean()
print("Average marks per subject:", avg_marks)

count_students = df.groupby('Subject')['Name'].count()
print("\nNumber of students per subject:")
print(count_students)

max_marks = df.groupby('Subject')['Marks'].max()
print("\nMaximum marks per subject:")
print(max_marks)

#-----------------------------------------------------------------------
df.plot(kind='bar', x='Name', y='Marks', title='Student Marks - Bar Graph')
df['Marks'].plot(kind='line', title='Marks - Line Graph')
df['Marks'].plot(kind='hist', title='Marks - Histogram')

#======================================================================

sales = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
}

df_Sales = pd.DataFrame(sales)

print(df_Sales["Revenue"].sum())

print(df_Sales["Revenue"].mean())

print(df[df_Sales["Revenue"]> df_Sales["Revenue"].mean()])


import matplotlib.pyplot as plt


plt.figure(figsize=(8, 5))
plt.plot(df['Day'], df['Revenue'], marker='o', linewidth=2)
plt.title('Revenue vs Day')
plt.xlabel('Day')
plt.ylabel('Revenue')
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()



