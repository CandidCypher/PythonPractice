"""
Exercise showcasing the performance difference of generators
"""
from time import time

def performance(func, *args, **kwargs):
    """
    Info: Performance testing function decoractor

    Input: Function
    Output: Wrapped function with print statements
    """
    def wrapper(*args, **kwargs):
        t_start = time()
        func(*args, **kwargs)
        t_end = time()
        execution_time = t_end - t_start
        print("*"*10)
        if kwargs.get("function_name"):
            print(f"Function Name: {kwargs['function_name']}")
        print(f"Execution time: {execution_time}")
        print("*"*10)


    return wrapper


@performance
def test_function(func, *args, **kwargs):
    """
    Info: Helper function that tests supplied functions

    Inputs:
    - Func : Function to be tested
    - Kwargs [func name]
    """
    func(*args)


def long_time(nums:int):
    """
    Info: Function iterrates over a range of nums
    """
    for i in range(nums):
        i*5



def long_time_list(nums:int):
    """
    Info: Function that iterrates over a list created by a range of nums
    """
    for i in list(range(nums)):
        i*5


if __name__ == "__main__":
    test_itterations = 1000000000

    test_function(long_time, test_itterations, function_name=long_time.__name__)
    test_function(long_time_list, test_itterations, function_name=long_time_list.__name__)
    