# Write a menu driven program to demonstrate map,reduce and filter 
# filter(function, iterable) - relies on function that returns true or false

from functools import reduce

def square(n):
    return n ** 2

def prod(a,b):
    return a*b

def even(n): 
    return n %2 ==0 #returns true or false

def main():
    while True:
        print("This is menu driven program for map, reduce and filter")
        print("1.Map example")
        print("2.Reduce example")
        print("3.Filter example")
        print("4.EXIT")
        choice = input("Entet your choice")

        if choice == '4':
            break

        if choice == '1':
            num = [1,2,3,4,5]
            res = list(map(square, num))
            print(f"original num = {num}, map = {res}")

        elif choice == '2':
            num = [1,2,3,4,5]
            res = reduce(prod, num)
            print(f"original num = {num}, map = {res}")

        elif choice == '3':
             num = [1,2,3,4,5]
             res = filter(even,num)
             print(f"original num = {num}, map = {res}")

        else:
            print("invalid choice")

main()        



             

        