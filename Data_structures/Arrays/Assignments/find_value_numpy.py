"""
Search of numpy array to find a specified value
"""
import numpy as np

def find_value(arr:np.array, target:int)->int:
    """
    INFO: Function to do linear search for as value in an array
    
    Input:(np.array) input array, (int)target value to find
    Output:(int) -1 if no value is found or the index of the found value
    """
    for idx in range(len(arr)):
        if arr[idx] == target:
            return idx
    return -1


if __name__ == "__main__":
    search_values = np.array([1,2,3,4,5,6,7,8,9,54,12,14,16,19])
    ret = find_value(search_values, 54)
    if ret == -1:
        print("Oh no, not in array")
    else:
        print(f"Found value at index: {ret}")