# Write a menu driven program to demonstrate value error,type error and name error. 

def value():
    try:
        num=int(input("Enter a integer"))
        test=int(num)
        print(f"you have entered {test}")
    except ValueError:
        print("Invalid input")    

def typee():
    try:
        value="100" + 50
        print(value)
    except TypeError:
        print("Invalid! Type error")    

def name():
    try:
        print(a)
    except NameError:
        print("Invaid name error")   

def div():
    try:
        result = 10/0
    except ZeroDivisionError:
        print("Cant divide by zero")

def main():
    while True:
        print("\n 1.Value error")
        print("2.Type error")
        print("3.Name error")
        print("4.Zerodivision error")
        print("5.EXIT")

        choice = input("Enter from 1 to 5: ")
        if choice == '5':
            break

        if choice == '1':
            value()
        if choice == '2':
            typee()
        if choice == '3':
            name()
        if choice == '4':
            div()       

main()

         

