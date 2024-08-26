"""
Simple addition and subtraction funtions.
"""

def add_numbers(num1:int, num2:int)->int:
    """
    Info: Demonstrative function that adds two numbers
    """
    # try:
    #     return int(num1) + int(num2)
    # except ValueError as err:
    #     return err
    try:
        if not isinstance(num1, int) or not isinstance(num2, int):
            raise TypeError
        else:
            return num1 + num2
    except TypeError as err:
        return err

    # if not isinstance(num1, int) or not isinstance(num2, int):
    #     return TypeError
    # return num1 + num2


def subtract_numbers(num1:int, num2:int)->int:
    """
    Info: Demonstrative function that subtracts two numbers
    """
    return num1 - num2




