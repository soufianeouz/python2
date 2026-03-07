def garden_operations():
    print("Testing ValueError...")
    try:
        tmp = int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    
    print()  
    print("Testing ZeroDivisionError...")
    try :
        tmp = 1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    
    print()   
    print("Testing FileNotFoundError...")
    try :
        file = open("missing.txt", "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    
    print()
    print("Testing KeyError...")
    try :
        dic = {"name":"soufiane"}
        bad_key = dic["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    
    print()
    print("Testing multiple errors together...")
    try :
        # we can use any error from the last 4 ones
        a = 1 / 0
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!") 
    
    print()
def test_error_types():
    print("=== Garden Error Types Demo ===")
    print()
    garden_operations()
    print("All error types tested successfully!")
test_error_types()