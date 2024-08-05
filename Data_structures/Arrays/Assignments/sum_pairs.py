"""
Write a function that returns a list of pairs who's sum is
equal to a specified value.

Write a function to find all pairs of an integer array whose 
sum is equal to a given number. Do not consider commutative pairs. 
"""

def find_sum_pairs(arr:list, value)->list:
    """

    """
    sum_pairs = []
    for x in range(len(arr)):
        for y in range(x+1, len(arr)):
            if arr[x] + arr[y] == value:
                sum_pairs.append([str(f"{arr[x]}+{arr[y]}")])

    return sum_pairs


if __name__ == "__main__":
    print(find_sum_pairs([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))

        