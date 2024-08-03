"""
Pracitce using lists
"""


my_list = [1,2,2,3,4,54, 1, 9, 22, 5, 5]

# Exercises
# 1: Given a list, find duplicates within a given list
def find_duplicates(lst:list)->list:
    """
    Info: Function that finds duplicates within a provided list by
    using the count function to build up a return list
    """
    duplicates = []
    for element in lst:
        if lst.count(element) >= 2 and element not in duplicates:
            duplicates.append(element)
    if len(duplicates) >= 1:
        return duplicates
    else:
        return -1
    
def find_duplicates_dict(lst:list)->list:
    """
    Info: Find duplicates in a list using a dictionary to store a counter value:
    """
    list_count = dict()
    for element in lst:
        if element not in list_count.keys():
            list_count[element] = 1
        else:
            list_count[element] += 1
    dups = [x for x in list_count.keys() if list_count[x] >= 2]
    if len(dups) == 0:
        return -1
    return dups
        
        
def find_duplicates_set(lst:list)->list:
    """
    Info: Function that finds duplicates within a provided list by
    using type conversions and returns a list of duplicates
    """
    singles = set(lst)
    dups = lst - list(singles)
    return dups


dups = find_duplicates(my_list)
print(dups)
# dups = find_duplicates_set(my_list)
# print(dups)

dups = find_duplicates_dict(my_list)
print(dups)

