# Given a list of numbers, provide the sum of all of the elements

def sumList(inputList:list) -> int:
    """
    Provides the sum of all elements in a list
    Input: list
    Output: int
    """
    sum = 0
    for element in inputList:
        sum += element
    return sum


if __name__ == "__main__":
    my_list = [1,2,3,4,5,6,7,8,9,10]
    sum_value = sumList(my_list)
    print(sum_value)
    # Silly as there is a built-in method for this
    print(sum(my_list))