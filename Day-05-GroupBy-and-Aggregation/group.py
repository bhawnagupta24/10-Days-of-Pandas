import pandas as pd
import numpy as np

data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Store': ['S1', 'S1', 'S2', 'S2', 'S1', 'S1', 'S2', 'S1'],
    'Sales': [100, 200, 150, 250, 120, 180, 200, 300],
    'Quantity': [10, 15, 12, 18, 8, 20, 15, 25],
    'Date': pd.date_range('2023-01-01', periods=8)
}

df = pd.DataFrame(data)


# Group by Category and calculate the sum of Sales

cat = df.groupby('Category')

for i, v in cat:
    print(i)
    print(v)


cat = df.groupby('Category')['Sales'].sum()
print(cat)
# Group by story and calculate the sum of Sales

cat = df.groupby('Store')['Sales'].sum()
print(cat)


cat = df.groupby(['Category','Store'])['Sales'].sum()
print(cat)



# Agrregation

print(df['Sales'].mean())

print(df['Sales'].agg(['sum', 'mean', 'min', 'max', 'count', 'std', 'median']))