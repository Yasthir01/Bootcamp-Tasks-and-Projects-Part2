import pandas as pd 


df = pd.read_csv('C:/Users/yasth/Downloads/credit.csv', sep=' ')
print(df)

# first 10 rows 
print(df.head(10))

# age coloumn
print(df['Age'])

# education column
print(df['Education'])

# Select users who are above the age of 30
print(df[df['Age'] > 30])