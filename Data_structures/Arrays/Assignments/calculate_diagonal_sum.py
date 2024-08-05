"""
Given a 2D array, find the sum of the diagonal elements

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Calculate the sum of 1 + 5 + 9 = 15
"""


def calculate_diagonal_sum(arr:list)->int:
    """
    INFO: Function that calculates the sum of diagonal elements
    Input: (list) 2d list
    Output: (int) the sum of the major diagonal
    """
    total = 0
    for i in range(len(arr)):
        total += arr[i][i]
    return total


def calculate_diagonal_prod(arr:list)->int:
    """
    Info: Function that calculates the product of the diagonal elements
    Input: (list) 2D Array/list object
    Output: (int) the product of the diagonal. 
    """
    prod = 1 # If initalized to zero then it results as zero. 
    for i in range(len(arr)):
        prod *= arr[i][i]
    return prod

if __name__ == "__main__":
    test_values =[[1,2,3], [4,5,6], [7,8,9]]
    summation = calculate_diagonal_sum(test_values)
    product = calculate_diagonal_prod(test_values)

    print(f"The diagonal sum of {test_values} is {summation}")
    print(f"The diagonal prod of {test_values} is {product}")
