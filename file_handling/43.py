#Write  a program to append contents in a file and read it 

filen = 'source.txt'

with open(filen, 'a') as file:
    file.write("\n This is new text")

with open(filen, 'r') as file:
    c = file.read()

print("After appending") 
print(c)   
