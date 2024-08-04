"""
Find the maximum product of the values within an array
"""

def find_max_product(arr:list)->tuple:
    """
    Info: Function that does a linear search to find the maximum product of values
        within a specified array/list
    Input: Input array/list of values
    Output: (tuple) Values that yeild the greatest product
    """
    max_prod = 0
    for idx in range(len(arr)):
        for ydx in range(idx+1, len(arr)):
            if max_prod < arr[idx]*arr[ydx]:
                max_prod = arr[idx]*arr[ydx]
                max_values = (arr[idx], arr[ydx])
    return max_values


def find_max_pair(arr:list)->tuple:
    """
    Info: Alternative to the above but more efficient as it requires
        only 1 itteration

    """
    max1, max2 = 0, 0
    for x in arr:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x
    return (max1, max2)


if __name__ == "__main__":
    test_values = [1,9,2,8,3,7,4,6,5]
    print(find_max_product(test_values))
    print(find_max_pair(test_values))