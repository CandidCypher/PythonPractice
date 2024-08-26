def max_min_diff(numbers):
    """
    Calculates the difference between the maximum and minimum number
    in the given list.

    :param numbers: A list of numbers.
    :return: The difference between the maximum and minimum number
    in the list.
    :raises ValueError: If the list is empty.
    """
    assert len(numbers) > 1
    return max(numbers) - min(numbers)
    

if __name__ == "__main__":
    values = [2]
    print(max_min_diff(values))