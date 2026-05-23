import pandas as pd
import numpy as np

labels = ['a','b','c']
my_list = [10,20,30]
arr= np.array([10,20,30])
d= {1:10,2:20,3:30}

print(pd.Series(my_list))
print(pd.Series(my_list,index= labels))
print(pd.Series(my_list,index= d))
