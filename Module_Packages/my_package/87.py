# Create a package with 3 files and import any one file in another package 

from package.module3 import mul

a = float(input("Enter a number"))
b = float(input("Enter second number"))

res = mul(a,b)

print(f"The result is {res}")

