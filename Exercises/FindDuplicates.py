#! /env/usr/bin python3

data = [1,2,4,9,5,1,7,8,9,4,6]

def findDuplicates_with_dict(inputList:list)->set:
    """
    Method that returns a list of duplicates found
    Uses a dictionary to form a table and then uses the
    table to return the duplicates

    Input: list
    Output: list
    """
    table_dict = dict()
    for element in inputList:
        if element not in table_dict.keys():
            table_dict[element] = 1
        else:
            # Previously added to the dict so increment the counter
            table_dict[element] += 1
    #for item in table_dict.items():
    duplicates = set()
    for number, count in table_dict.items():
        if count >= 2:
            duplicates.add(number)
    return duplicates

def findDuplicates_list_count(inputList:list)->set:
    """
    Method that returns duplicates using built-in methods
    """
    duplicates = set()
    for element in inputList:
        if inputList.count(element) >=2:
            duplicates.add(element)
    return duplicates

if __name__ == "__main__":
    data = [1,2,4,9,5,1,7,8,9,4,6]
    # Duplicates return should be [1,4,9]
    print(findDuplicates_with_dict(data))
    print(findDuplicates_list_count(data))
    