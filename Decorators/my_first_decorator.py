

def my_decorator(func):
    """
    Info: Decorator function to add additional formatting to a function
    that prints strings.
    """
    def wrap_func(*args, **kwargs):
        print("*******")
        func(*args, **kwargs)
        print("*******")
    return wrap_func

@my_decorator
def hello(*args, **kwargs):
    """
    Info: Function to print a string "Heellleewww" for the purpose of
          demonstration.  
    """
    ending = "," if len(args) > 0 else ""
    print("helllleeeeewwww", end=ending)
    if len(args) > 0:
        for arg in args:
            print(f" {arg}", end = "")
        print("")

@my_decorator
def see_ya():
    """
    Info: Funcciton that prints 'See ya!!!' """
    print("See ya!!!")


hello("simon", "dave", "rubin")
see_ya()
