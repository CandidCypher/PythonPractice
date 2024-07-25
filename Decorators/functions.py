"""
Function modules that are used in the performance_decorator.py script. 

Dependencies: 


"""

import random
import string


def long_itteration(lst_len:int):
    """
    Info: Funcction that does itteration over a specified length and multiplies the index by 5"""
    for x in range(lst_len):
        x = x*100

def long_zip(lst_len:int):
    """
    Info: Function that generates two lists of
    """
    letters = string.ascii_lowercase
    len(letters)
    letters[25]

    numbers = [random.randint(0,1000) for x in range(lst_len)]
    letters = [string.ascii_lowercase[random.randint(0, 25)] for x in range(lst_len)]
    commbined = zip(numbers, letters)
    

