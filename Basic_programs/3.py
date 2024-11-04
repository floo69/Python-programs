# Write a menu driven program to implement basic calculator using functions

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        return "error"
    return x/y

def calci():
    while True:
        print("\n This is a calci")
        print("1.Addition")
        print("2.Substract")
        print("3.Multiply")
        print("4.Division")
        print("5.Exit")

        choice = input("Enter your choice (1-5)")

        if choice=='5':
            break
        
        num1 = float(input("Enter first number"))
        num2 = float(input("Enter second number"))

        if choice == '1':
            result = add(num1, num2)
            print(f"{result}")

        elif choice == '2':
            result = sub(num1, num2)
            print(f"{result}")  

        elif choice == '3':
            result = mul(num1, num2)
            print(f"{result}")

        elif choice == '4':
            result = div(num1, num2)
            print(f"{result}")

        else:
            print("Invalid choice")    

calci()    

             
            

             


             



