# Write a program to calculate gross salary of 10 employees using map function
# map(function, iterable)   

basic = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 1100]

def gross(basic):
    ha = 0.20 * basic
    ta = 0.30 * basic
    gross = ha+ta+basic
    return gross

gross_salary = list(map(gross, basic))

count = 1
for i in gross_salary:
    print(f"Gross salary of emp {count} is {i}")
    count+=1


