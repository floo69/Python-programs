# Write a program to convert a dictionary to dataframe and display its info 

import pandas as pd

data = {
    'Name':['Floyd', 'Mark', 'Luke'],
    'Age':[10,20,30]
}

df = pd.DataFrame(data)

print("Data Frame: ")
print(df)

print("\n DataFrame Info:")
df.info()

