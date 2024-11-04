# Write a program to implement Catch exception in a function

def divide_num(a,b):
    try:
        ans=a/b
        print(f"The ans is {ans}")
    except ZeroDivisionError:
        return "Invalid! cant divide"
    except TypeError:
        return "Invaid input type"
    except ValueError:
        return "Invalid , no value"
    except Exception:
        return "invalid"
    finally:
        print("Execution completed")

print(divide_num(10, 2))    
print(divide_num(10, 0))    
print(divide_num(10, 'a'))  