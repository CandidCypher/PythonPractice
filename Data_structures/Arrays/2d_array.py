"""
2-Dimensional array practice
"""

#import array - standard library array does not support multi-dimension arrays
import numpy as np


"""
Given the 2D array, create this as both as an STL array and numpy array

[1,2,3,4,5]
[6,6,7,8,9]
[10, 20, 30, 40, 50]

"""

if __name__ == "__main__":
    two_d_array = np.array([[1,2,3,4,5], [6,6,7,8,9], [10, 20, 30, 40, 50]], dtype=int)
    # print(two_d_array)

    # # accessing rows
    # print("Priting row elements")
    # for row in two_d_array:
    #     print(f"Row: {row}")

    # # accessing elements
    # for row in two_d_array:
    #     for element in row:
    #         print(element)

    # Inserts a new column(axis=1) at index 0
    new_array = np.insert(two_d_array, 0, [[1,2,3]], axis=1)
    # Inserts a new row(axis=0) at index 1
    new_array2 = np.insert(two_d_array, 1, [[8,8,8,8,8]], axis=0)
    print(new_array)
    print(new_array2)