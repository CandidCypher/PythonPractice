from function_examples import most_basic_function
from function_examples import hello_print, greet
from function_examples import multi_args_required, multi_args_unknown
import utility


if __name__ == "__main__":
    print(utility)
    most_basic_function()
    hello_print()
    greet("Daniel")
    multi_args_required(x=1, y=1.2, z="Thomas")
