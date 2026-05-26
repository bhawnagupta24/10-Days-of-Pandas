import pandas as pd
import numpy as np

data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan],
    'D': [1, np.nan, np.nan, np.nan, 5]
}

df = pd.DataFrame(data)

print(df)

# true false 
print(df.isna())

# how many values of NaN
print(df.isna().sum())

#empty or not
print(df.isna().any())



#removing NaN

print(df.dropna())
print(df.dropna(thresh =3))



#Filling the new data

print(df.fillna(0))

values = {'A':0, 'B':100, 'C':300, 'D':400}

print(df.fillna(value=values))