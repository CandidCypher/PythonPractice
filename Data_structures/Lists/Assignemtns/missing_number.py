"""
Assignment: Find the missing number in a given array of integers

Write a function to find the missing number in a given integer 
array of 1 to 100. The function takes to parameter the array and 
the number of elements that needs to be in array.  For example if 
we want to find missing number from 1 to 6 the second parameter will be 6. 
"""

def find_missing_value(arr:list, number_vals:int)->int:
    """
    Info: Function to provide a list of the missing values given
    a list of numbers
    """
    low = min(arr)
    high = max(arr)
    num_missing = number_vals - len(arr)
    # The missing value should be somewhere between high and low
    # and the length of the list indicates how many values may be missing
    missing = []
    for i in range(low, low+num_missing):
        if i not in arr:
            missing.append(i)
    return missing

def find_missing_value2(arr:list, n:int)->int:
    n = len(arr) + 1
    expected_sum = n * (arr[0] + arr[-1])//2 
    act_sum = sum(arr)
    missing_value = expected_sum - act_sum
    return missing_value

if __name__ == "__main__":
    values = [1,2,3,3,4,6]
    missing_numbers = find_missing_value(values,6)
    print(f"In the list of values: {values} these are the values missing: {missing_numbers}")
