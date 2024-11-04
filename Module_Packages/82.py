# Write a module to calculate rate of interest and import it in another file and display the output 

from module2 import interest

p=float(input("Enter the principal amount"))
r=float(input("Enter the rate"))
t=float(input("Enter the time"))

ans = interest(p,r,t)

print(f"The interest rate for {p} principal, {r} rate and {t} time is {ans}")