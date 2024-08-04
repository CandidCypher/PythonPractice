"""
Write a function that returns the middle slice of a list

Middle Function

Write a function called middle that takes a list and returns a new 
list that contains all but the first and last elements.
"""

def middle_return(arr:list)->list:
    """
    Info: Function that takes a list and returns a new list containing all but
    the first and last elements
    """
    return arr[1:-1]


if __name__ == "__main__":
    test_values = [1,2,3,4,5,6,7,8,9]
    print(middle_return(test_values))