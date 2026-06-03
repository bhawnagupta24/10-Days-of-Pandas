import pandas as pd
import numpy as np



#episodes

df = pd.read_csv('Dataset/anime.csv')

# print(df.head())

# print(df.loc[4]['Title'])

def extract_episodes(txt):
    check = False
    data = ""

    for i in txt:
        if i == ")":
            check = False
            return data
    
        if i == "(":
            check = True
            continue

        if check == True:
            data = data + i

df['Episodes']=df["Title"].apply(extract_episodes)
df['Episodes']= df['Episodes'].str.replace(" eps", "")
df['Episodes'] = df['Episodes'].astype(int)
# print(df)






# timestamp

def extraction_time(txt):
    check = False
    data = ""

    for i in range(len(txt)):
        if txt[i] == ')':

            for j in range(i+1, i + 20):
                data += txt[j]
            
            return data

df['Total Time'] =df['Title'].apply(extraction_time)
# print(df.head())
        



from dateutil.relativedelta import relativedelta
from datetime import datetime

def calculate_total_months(period):

    try:
        start_str, end_str = period.split(' - ')

        start_date = datetime.strptime(start_str, '%b %Y')
        end_date = datetime.strptime(end_str, '%b %Y')

        r = relativedelta(end_date, start_date)

        return r.years * 12 + r.months + 1   # +1 to include the starting month

    except:
        return None

df['Months'] = df['Total Time'].apply(calculate_total_months)

# print(df)



#highest score
print(df[df['Score'] == df['Score'].max()])

# print(df['Score'].value_counts())

# print(df['Title'].head())


print(df[df['Episodes'] == df['Episodes'].max()])