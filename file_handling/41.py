#Write a program to check whether a file exist if it exists delete it otherwise create it

import os

fname = 'source.txt'

# checking
if os.path.exists(fname):
    os.remove(fname)
    print("removed")
else:
    with open(fname, 'w') as file:
        file.write("New file created")
    print("Created")    