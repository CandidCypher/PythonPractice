"""
Write a function that reports if a list has duplicates
"""

def has_duplicates_count(arr:list)->bool:
    """
    Implementation of a function that reports if a list contains duplicate items.
    Input: itterable (list/array)
    Output: bool False - no duplicates / True - Duplicates found
    """
    for element in arr:
        if arr.count(element) >= 2:
            return True
    return False


def has_duplicates_set(arr:list)->bool:
    """
    Implementation of a function that reports if a list contains duplicates
    using a set for tracking unique values. This is more efficient
    """
    seen_vals = set()
    for element in arr:
        if element not in seen_vals:
            seen_vals.add(element)
        else:
            return True
    return False


if __name__ == "__main__":
    test_set = [1,2,3,4,5,6,7,8,9,5]
    print(has_duplicates_count(test_set))
    print(has_duplicates_set(test_set))