"""
Introduction to Python Arrays and Numpy Arrays
"""

import array
# Python standard library array object. Downside is that it only
# supports python primitive types so you can't store custom types.

import numpy as np
# Non STL array object but is incredibly efficient. Thanks @TravisOliphant!

if __name__=="__main__":
    my_array = array.array("i") # Declares an empty array of integers
    # Notes: Creation of an empty array is (O(1)) time complexity
    print(my_array)

    my_array2 = array.array("i", [1,2,3,4,5])
    # Notes: Crreation of a non empty array is (O(n)) time due to the assignment
    # of the elements.
    print(my_array2)
    
    np_array = np.array([], dtype=int) # Declares numpy array of ints
    # Same O(1) time for empty array. 
    np_array2 = np.array([x for x in range(1,100) if x%2 ==0])
    # Same O(n) time for non empty arrays
    np_array2.__sizeof__()