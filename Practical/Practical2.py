import pandas as pd


df = pd.read_csv("Data/Employees.csv")
# print("----- Original Data -----")
# print(df)

# 1. handling missing values
df_filled = df.copy()
df_filled['Designation'] = df_filled['Designation'].fillna("Not Assigned")
print(df_filled)
df_dropped = df.dropna(subset=["Designation"])
print(df_dropped)

# 2. Filter Salary column to show employees with salary higher than 40K
high_salary = df[df['Salary'] > 40000]
print(high_salary)

# 3. Filter Designation to show only Marketing Employees
marketing_emp = df[df['Department'] == 'Marketing']
print(marketing_emp)

# 4. Sort the employee names in forward and reverse order
sorted_forward = sorted(df['Emp_Name'])
print(sorted_forward)
sorted_reverse = sorted(df['Emp_Name'], reverse=True)
print(sorted_reverse)

# 5. Display only Tech employees
tech_emp = df[df['Department'] == 'Tech']
print(tech_emp)

# 6. Find the Average salary of all departments
dept_avg_salary = df.groupby('Department')['Salary'].mean()
print(dept_avg_salary)

# # 7. Find the count of HR employees
hr_count = df[df['Department'] == 'HR']['Emp_Name'].count()
print(hr_count)

# 8. Find the designation wise highest and lowest salary
designation_max_salary = df.groupby('Designation')['Salary'].max()
print(designation_max_salary)
designation_min_salary = df.groupby('Designation')['Salary'].min()
print(designation_min_salary)
