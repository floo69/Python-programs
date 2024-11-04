# Write a python program to create 2 threads where in one displays salary of 10 employees and another displays name of 10 employees
import threading

def displayname(names):
    for name in names:
        print(f"Employee names are{name} ")

def displaysalary(salaries):
    for salary in salaries:
        print(f" \n Salaries are {salary}")

emp = []
salary_emp = []

print("Enter details of 10 employees")

for i in range(10):
    name=input("Enter your name")
    salary=input("Enter your salary")
    emp.append(name)
    salary_emp.append(salary)

name_t = threading.Thread(target=displayname, args=(emp,))
salary_t = threading.Thread(target=displaysalary, args=(salary_emp,))

name_t.start()
salary_t.start()

name_t.join()
salary_t.join

