import array
import numpy as np

def arrayIndexTraversal(arr):
    """
    Info: Helper method access elements of an array based upon the index
    """
    for x in range(len(arr)):
        print(arr[x])


def arrayElementTransversal(arr:array.array):
    """
    Info: Helper method to print out elements of an array
    """
    for element in arr:
        print(element)


if __name__ == "__main__":
    my_stl_array = array.array("i", [1,2,3,4,5])
    arrayIndexTraversal(my_stl_array)
    arrayElementTransversal(my_stl_array)