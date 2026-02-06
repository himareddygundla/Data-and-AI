# Students missing analysis 
# Name Age Marks 

import pandas as pd
df = pd.read_csv("students_missing.csv")
print(df,"\n")

print(df.isnull(),"\n")

df["age"]=df["age"].fillna(df["age"].mean(),inplace=True) # inplace = true means changes will be made to original dataframe
df["marks"]=df["marks"].fillna(df["marks"].mean(),inplace=True)


# or we can simply clean as well 
# df = df.dropna()
print(df)