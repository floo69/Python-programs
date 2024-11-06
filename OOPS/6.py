#Write a program to create a class called Employee with methods called work() and getSalary(). Create a subclass called HRManager that overrides the work () method and adds a new method called addEmployee(). 

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is working")

    def getSalary(self):
       return self.salary

class HRManager(Employee):
    def __init__(self,name,salary):
        super().__init__(name, salary)

    #override
    def work(self):
        print(f"{self.name} is managing hr tasks")

    def addEmployee(self, employee_name):
        print(f"{self.name} added a new employee: {employee_name}")

emp1 = Employee("Floyd carlo", 5000)
emp1.work()            
print(f"salary: ${emp1.getSalary()}")

hr = HRManager("John", 1000)
hr.work()
print(f"salary: ${hr.getSalary()}")
hr.addEmployee("new")