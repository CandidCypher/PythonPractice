"""

"""

def remove_duplicates(arr:list)->list:
    """
    Function that removes the duplicates from a list
    """
    # To fix you could copy
    simplified = arr.copy()

    return list(set(simplified)) # Destructive


def remove_duplicates_no_set(arr:list)->list:
    """
    Function that retuns list with duplicates removed
    """
    simplified = []
    for element in arr:
        if element not in simplified:
            simplified.append(element)
    return simplified


if __name__ == "__main__":
    test_values = [1, 1, 2, 2, 3, 4, 5]
    print(remove_duplicates(test_values))
    print(remove_duplicates_no_set(test_values))
