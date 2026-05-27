import pandas as pd
import numpy as np

employees = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['John', 'Anna', 'Peter', 'Linda', 'Bob'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR']
})

# DataFrame 2: Salary information
salaries = pd.DataFrame({
    'employee_id': [1, 2, 3, 6, 7],
    'salary': [60000, 80000, 65000, 70000, 90000],
    'bonus': [5000, 10000, 7000, 8000, 12000]
})

print(employees)
print(salaries)
 
print(pd.merge(employees,salaries, on='employee_id',how='inner'))
print(pd.merge(employees,salaries, on='employee_id',how='outer'))
print(pd.merge(employees,salaries, on='employee_id',how='left'))
print(pd.merge(employees,salaries, on='employee_id',how='right'))




# concatination

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2'],
    'C': ['C0', 'C1', 'C2']
})

df2 = pd.DataFrame({
    'A': ['A3', 'A4', 'A5'],
    'B': ['B3', 'B4', 'B5'],
    'C': ['C3', 'C4', 'C5']
})

print(df1)
print(df2)

print(pd.concat([df1,df2]))
print(pd.concat([df1,df2],axis=1))




df1 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie']
}, index=[1, 2, 3])

# Second DataFrame
df2 = pd.DataFrame({
    'score': [85, 90, 75]
}, index=[2, 3, 4])


print(df1.join(df2))