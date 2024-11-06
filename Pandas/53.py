# Write a program to fix bad data using pandas 

import pandas as pd

data = {
    'Name': ['Floyd', 'Mark', None, 'David', 'Eve'],
    'City': ['New york', None, 'Chicago', 'Sans', '']
}

df = pd.DataFrame(data)

print("Original dataframe:")
print(df)

df['Name']= df['Name'].fillna('Unknown')

df['City'] = df['City'].replace('', 'Unknown').fillna('Unknown')

print("\nCleaned dataframe:")
print(df)
