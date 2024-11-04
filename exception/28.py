# Write a program for user Input Validation with Exceptions

def validate():
    while True:
        try:
            age = int(input("Enter your age"))
            if age<0 or age > 120:
              raise ValueError("Invalid value")   
            
            return age

        except ValueError as a:
            print(f"{a}")

agee = validate()
print(agee)
            

    

