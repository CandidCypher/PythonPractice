"""
Demonstration of a real world application of the power of decorators

Given a series of functions that are used elsewhere in code:
 - imported locally.
"""
from time import time
from functions import long_itteration, long_zip


def performance(func, *args, **kwargs):
    """
    Info: timing decorator funcction that reports the time that it takes for a funciton to run
    """
    def wrap_func(*args, **kwargs):
        t_start = time()
        func(*args, **kwargs)
        t_end = time()
        delta_t = t_end - t_start
        print("*********")

        if "function_name" in kwargs.keys():
            print(f"Function name: {kwargs['function_name']}")

        print(f" Testing time: {delta_t}s")
        
        print("*********")
    return wrap_func


@performance
def test_function_execution(func, *args, **kwargs):
    """
    Test method that tests the execution of a provided method"""
    func(*args)


if __name__ == "__main__":
    test_function_execution(long_itteration, 100000, function_name = long_itteration.__name__)
    test_function_execution(long_zip, 1000000)
    
