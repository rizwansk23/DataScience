import pandas as pd
df = pd.read_csv('Employees.csv')
print('----- Original Data -----')
print(df)

# 1. handling missing values
df_filled = df.copy()
df_filled[&#39;Designation&#39;] = df_filled[&#39;Designation&#39;].fillna(&quot;Not Assigned&quot;)
print(df_filled)
df_dropped = df.dropna(subset=[&#39;Designation&#39;])
print(df_dropped)

# 2. Filter Salary column to show employees with salary higher than 40K
high_salary = df[df[&#39;Salary&#39;] &gt; 40000]
print(high_salary)

# 3. Filter Designation to show only Marketing Employees
marketing_emp = df[df[&#39;Department&#39;] == &#39;Marketing&#39;]
print(marketing_emp)

# 4. Sort the employee names in forward and reverse order
sorted_forward = sorted(df[&#39;Emp_Name&#39;])
print(sorted_forward)
sorted_reverse = sorted(df[&#39;Emp_Name&#39;], reverse=True)
print(sorted_reverse)

# 5. Display only Tech employees
tech_emp = df[df[&#39;Department&#39;] == &#39;Tech&#39;]
print(tech_emp)

# 6. Find the Average salary of all departments
dept_avg_salary = df.groupby(&#39;Department&#39;)[&#39;Salary&#39;].mean()
print(dept_avg_salary)

# 7. Find the count of HR employees
hr_count = df[df[&#39;Department&#39;] == &#39;HR&#39;][&#39;Emp_Name&#39;].count()
print(hr_count)

# 8. Find the designation wise highest and lowest salary
designation_max_salary = df.groupby(&#39;Designation&#39;)[&#39;Salary&#39;].max()
print(designation_max_salary)
designation_min_salary = df.groupby(&#39;Designation&#39;)[&#39;Salary&#39;].min()
print(designation_min_salary)