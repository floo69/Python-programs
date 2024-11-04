# Demonstrate assert, raise try except and finally

def div(a,b):
    assert b!=0, "The demonator cannot be zero"

    if type(a) not in [int]:
        raise TypeError("Not a integer")
    if type(b) not in [int]:
        raise TypeError("Not a integer")
    
    try:
        res=a/b
        return res
    except ZeroDivisionError:
        print("zero division error")
    except:
        print("invaid")    
    finally:
        print("Execution completed")    
    
print(div(10,0))
