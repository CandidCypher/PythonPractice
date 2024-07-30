"""
Demonstration of a real world application of the power of decorators

Given a series of functions that are used elsewhere in code:
 - imported locally.
"""
from time import time
from functions import long_itteration, long_zip


def performance(func, func_name):
    """
    Info: timing decorator funcction that reports the time that it takes for a funciton to run
    """
    def wrap_func(*args, **kwargs):
        t_start = time()
        func(*args, **kwargs)
        t_end = time()
        delta_t = t_end - t_start
        print("*********")
        print(f"{func.__name__}  Testing time: {delta_t}s")
        print("*********")
    return wrap_func


@performance
def test_function_execution(func, *args, **kwargs):
    """
    Test method that tests the execution of a provided method"""
    func(*args, **kwargs)


if __name__ == "__main__":
    test_function_execution(long_itteration, 10000000)
    test_function_execution(long_zip, 1000000)
    
