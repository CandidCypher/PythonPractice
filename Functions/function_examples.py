def most_basic_function():
    """
    Info: The most basic Python function
    """
    pass


def hello_print():
    """
    Info: Funcction that prints "Hello"
    """
    print("Hello world")


def greet(name:str)->None:
    """
    Info: Function that takes a str(Name) and prints a greeting
    """
    import random
    greeting = random.choice(["Hello", "Greetings", "Nice to meet you"])
    print(f"{greeting}, {name}")


def multi_args_unknown(*args, **kwargs):
    """
    Info: Example of a function that takes an unknown number of args, and kwargs
    """
    for arg in args:
        print(arg)
    for kwarg in kwargs.items():
        print(kwarg)


def multi_args_required(x:int, y:float, *args, z:str="name", **kwargs):
    """
    Info: Example of a function that takes both required and unknown number of args
    """
    print(f"Required args: x-{x}, y-{y}, z-{z}")
    if args:
        for arg in args:
            print(f"Args: {arg}")

    if kwargs:
        for kwarg in kwargs.items():
            print(kwarg)

if __name__ == "__main__":
    multi_args_required(1, 2.051, "a", 1, "c", "d", apple=123, phone='Samsung')
    multi_args_unknown(1,2,3,4, name="Simon", space=1000, definition="Banggers")