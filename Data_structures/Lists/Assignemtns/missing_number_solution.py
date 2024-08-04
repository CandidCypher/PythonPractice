"""
Provided solution

Using arithmetic progression
"""

def find_missing_value(arr:list, n:int)->int:
    n = len(arr) + 1
    expected_sum = n * (arr[0] + arr[-1])//2 
    act_sum = sum(arr)
    missing_value = expected_sum - act_sum
    return missing_value


if __name__ == "__main__":
    print(find_missing_value([1,2,3,4,6],6))
