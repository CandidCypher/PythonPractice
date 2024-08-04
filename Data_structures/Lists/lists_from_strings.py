"""
List and string operations practice

"""
def sort_list(lst:list)->list:
    """
    Info: sorting function that returns a list in descending order
    ## Flaw is that it empties the input list because the list
    is passed by value not by reference. 
    """
    sorted = []
    while(len(lst) >0):
        sorted.append(max(lst))
        lst.remove(max(lst))
    return sorted

if __name__ == "__main__":
    foods = "spam"
    print(list(foods))
    numbers = 1234556
    print(list(str(numbers)))

    sentence = "This is Sam. Sam I am."
    words = sentence.split()
    type(words)
    numbers = [1,2,3,4,5,6,7,8,9]
    sorted_nums = sort_list(numbers)
    print(numbers) 
    print(sorted_nums)