"""
Example of searching a 2D array. This is of O(m*n) complexity and O(1) space complexity
"""

import numpy as np

def search_2d_array(arr:np.array, value)->tuple:
    """
    Info: Helper function that returns the index of the first instance of a specified
        search value

    Inputs
    - arr (numpy.array): array to search over
    - value: search value

    Output : index of the first instance of the search value or -1
    """

    for rdx, row in enumerate(arr):
        for cdx, element in enumerate(row):
            if element == value:
                return (rdx, cdx)
    # Element was not found
    return -1


if __name__ == "__main__":
    size = range(5)
    two_d_array = np.array([[x for x in size],[x*2 for x in size],[x*10 for x in size]], dtype=int)
    ret = search_2d_array(two_d_array, 2)
    #ret should be (0,2)
    print(ret)

    ret = search_2d_array(two_d_array, 6)
    print(ret)