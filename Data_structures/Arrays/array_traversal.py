import array


def array_index_traversal(arr):
    """
    Info: Helper method access elements of an array based upon the index
    """
    for x in range(len(arr)):
        print(arr[x])


def array_element_traversal(arr:array.array):
    """
    Info: Helper method to print out elements of an array
    """
    for element in arr:
        print(element)


def array_element_access(arr:array.array, idx:int):
    """
    Info: Silly wrapper function to return an element of an array given
    an index

    Input(array.array, int): STL Array object and the requested index
    Output: The requested element at specified index
    """
    # Ensure that the specified idx is within the len of the array
    if idx >= len(arr):
        print(f"Error: Unable to access element {idx} of array size {len(arr)}")
        return
    elif idx < 0:
        print("Error: Unable to access negative space indicies. You have broken the space time continuum")
        return
    else:
        return arr[idx]

if __name__ == "__main__":
    my_stl_array = array.array("i", [1,2,3,4,5])
    array_index_traversal(my_stl_array)
    array_element_traversal(my_stl_array)
    res = array_element_access(my_stl_array, 100)
    res2 = array_element_access(my_stl_array, -100)
    res3 = array_element_access(my_stl_array, 4)
    print(res, res2, res3)

