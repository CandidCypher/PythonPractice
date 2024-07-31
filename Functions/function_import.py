from function_examples import most_basic_function
from function_examples import hello_print, greet
from function_examples import multi_args_required, multi_args_unknown


if __name__ == "__main__":
    most_basic_function()
    hello_print()
    greet("Daniel")
    multi_args_required(x=1, y=1.2, z="Thomas")
