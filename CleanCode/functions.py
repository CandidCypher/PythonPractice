def my_sum_fuction(single_arg, *args, kwarg=10, **kwargs):
    """
    Info: Template of function naming. 
    'single_arg' denotes a single positional argument.
    '*args' denots a list or itterable object of positional arguments
    'kwarg' denots a single named argument
    '**kwargs' denotes an unknown number of named (keyword) arguments
    """
    sum = single_arg
    for variable in args:
        sum += variable
    sum += kwarg
    for item in kwargs.values():
        sum += item
    return sum

if __name__ == "__main__":
    print(my_sum_fuction(10, 1,2,3,4,5, kwarg=5, x=1, y=2, z=200))