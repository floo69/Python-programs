#Write a program to demonstrate series using pandas and perform removing of duplicate rows. 

import pandas as pd

data = ["apple", "banana", "cherry", "apple"]

s = pd.Series(data)

print("Original:")
print(s)

new_s = s.drop_duplicates()
print(new_s)



