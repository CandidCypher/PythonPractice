# Requirements. Given a list of integers, find the highest even number

def highest_even(li:list)->int:
    """
    Info: Method to return the highest even in a list
    Input:(list) List of integers
    Output: (int) Highest even number of the input
    """
    high_even = 0
    for element in li:
        if element % 2 == 0 and element >= high_even:
            high_even = element
    return high_even

def highest_even_2(*args:int)->int:
    """
    INFO: Wrapper for highest_even to allow for passing arguments in place vs
          using a list
    """
    values = []
    for value in args:
        values.append(value)
    return highest_even(values)


if __name__ == "__main__":
    # Function call should return 8
    print(highest_even([1,2,3,4,5,6,8]))
    print(highest_even_2(1,2,3,4,5,6,7,8))