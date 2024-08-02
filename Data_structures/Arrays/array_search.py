import array


def linear_array_search(arr:array.array, value)->int:
    """
    Info: Linear (O(n)) search function for searching 
    Input: array obj and value to search
    Output(int): Error code of -1 or index of found element. 
    """
    for idx, val in enumerate(arr):
        if arr[idx] == value:
            # Eastern european method of swapping lvars and rvars
            # protects from missing "=" by preventing an assigment
            # operation conditional check
            # Remove thhe second "=" and find out
            return idx
    return -1


if __name__ == "__main__":
    my_array = array.array("i", [1,2,3,4,5,10,11])
    search_element = 6
    found_idx = linear_array_search(my_array, search_element)
    if -1 == found_idx:
        print(f"Unable to find the search element {search_element}")
    else:
        print(f"Found the element at index: {found_idx}")