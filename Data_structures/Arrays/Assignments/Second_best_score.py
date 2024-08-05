"""
Given a list of scores, find the 2nd best score. 
"""

def find_second_best(arr:list)->tuple:
    """
    Info: FUnction that returns the second highest element in a list
    
    Input: List of values
    Output: 2nd Highest element. 
    """
    second_highest = 0
    highest = max(arr)
    for element in arr:
        if element >= second_highest and element < highest:
            second_highest = element
    return highest, second_highest


#If the max function is not available
def find_second_best_no_max(arr:list)->tuple:
    """
    Info: Funcion that finds the first and second highest
    """
    highest, second_best = 0, 0
    for score in arr:
        if score > highest:
            second_best = highest
            highest = score
        elif ((score > second_best) and score != highest):
            second_best = score
    return highest, second_best



if __name__ == "__main__":
    myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
    print(find_second_best(myList))
    print(find_second_best_no_max(myList))
