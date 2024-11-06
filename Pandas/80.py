#Write a Pandas program to replacing missing data with mean value

import pandas as pd

data = {'A': [1, 2, None, 4, 5],
        'B': [10, None, 30, 40, 50],
        'C': [100, 200, 300, None, 500]}

df = pd.DataFrame(data)

print("Original:")
print(df)

df_filled = df.fillna(df.mean())

print("\nDataFrame:")
print(df_filled)