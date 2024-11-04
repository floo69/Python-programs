# Write a program to find maximum salary of an employee after calculating gross salary using map and reduce function

# from functools import reduce
# reduce(function, iterable[, initializer])

from functools import reduce

n = int(input("Enter the no of employees"))   
salaries =[]
for i in range(n):
    basic=int(input("Enter the salaries of employees"))
    salaries.append(basic)

def gross(basic):
    ha=0.10*basic
    ta=0.20*basic
    gross=ha+ta+basic
    return gross

def maxx(x,y):
    if x>y:
        return x
    else:
        return y

gross_salary = list(map(gross,salaries))
max = reduce(maxx, gross_salary)

print("Gross Salaries:", gross_salary)
print("Maximum Gross Salary:", max)
