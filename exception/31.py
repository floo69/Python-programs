# Write a python program to create a method that takes an integer as a parameter and throws an exception if the number is odd

class check:
    def check_even(self, num):
        if num % 2 == 0:
            raise ValueError("The number is even")
        else:
            print("The number is odd")

try:
    a = check()
    a.check_even(2)
except ValueError as v:
    print(v)    