import pandas as pd
import numpy as np

df = pd.read_csv('Dataset/Countries.csv')

# print(df)
print(df.shape)
print(df.info())


# which country has the highest population

print(df[df['population'] == df['population'].max()]['country'])



#what is the capital of the country with highest population

print(df[df['population'] == df['population'].max()][['capital_city']])



# which country has the least population

print(df[df['population'] == df['population'].min()]['country'])




#what is the capital of the country with  least population

print(df[df['population'] == df['population'].min()][['capital_city']])




#give me top 5 countries with highest democratic score

df.sort_values(by='democracy_score', ascending=False, inplace=True)

print(df['country'].head())




#how many total regions are there

print(df['region'].value_counts().count())




#how many countries lie in Eastern Europe region

print(df[df['region'] == 'Eastern Europe']['country'])




#who is the political leader of the 2nd highest populated country

print(df[df['population'] == df['population'].nlargest(2).iloc[1]]['political_leader'])



# how many countries are there whose political leaders are unknown

print(df[df['political_leader'].isna()]['country'].count())



#how many country have Republic in their full name

count = 0

def counting(txt):
    global count

    if 'republic' in txt.lower():
        count += 1

    return txt


df['country_long'] = df['country_long'].apply(counting)

print(count)




#which country in african region has highest population


africa_df = df[df['continent'] == 'Africa']

print(africa_df[africa_df['population'] == africa_df['population'].max()])