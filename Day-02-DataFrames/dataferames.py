import pandas as pd
import numpy as np

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}

df2= pd.DataFrame(data)




# add or remove Designation

df2["Designation"] = ["Doctor", "Eng.", "Doctor", "Eng."]

print(df2.drop('Designation',axis =1,inplace = True))
print(df2)


print(df2.loc[[0,1]])
print(df2.loc[[0,1]][["City","Salary"]])



# using list 


data_list = [
     ['John', 'Anna', 'Peter', 'Linda'],
     [28, 34, 29, 42],
     ['New York', 'Paris', 'Berlin', 'London'],
     [65000, 70000, 62000, 85000]
]
columns = ["Name", "Age", "City", "Salary"]

print(pd.DataFrame(data_list, columns=columns))

print(pd.DataFrame(data_list))





# conditionals selection

#I only want to see those people whose age is above 30

print(df2[df2["Age"] > 30])


#I only want people whose age is above 30 and their city must be Paris

print(df2[(df2["Age"] > 30 )& (df2["City"] == 'Paris')])