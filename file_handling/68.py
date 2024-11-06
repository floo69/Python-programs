# Write a Python program to read a file line by line and store it into a list.

fname = 'source.txt'

elist = []

with open(fname, 'r') as file:
    for line in file:
        elist.append(line.strip())

print(elist)        