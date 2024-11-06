# Write a program to read a file and copy its contents to another file 

source = 'source.txt'
dest = 'destination.txt'

with open(source, 'r') as sourcef:
    content = sourcef.read()

with open(dest, 'w') as destination:
    destination.write(content)

print("success")