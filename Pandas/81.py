#Write a Pandas program to fill missing values (NaN) in a DataFrame and drop rows with missing data

import pandas as pd
import numpy as np

data = {
    'A':[10, np.nan, 20],
    'B':[30, np.nan, 40]    
}

df = pd.DataFrame(data)

print("Dataframe")
print(df)

modified = df.fillna(0)
print("DataFrame after filling")
print(modified)

