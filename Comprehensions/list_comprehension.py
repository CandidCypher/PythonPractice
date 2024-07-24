"""
Demo of the utilization of list comprehension
"""

# Not doing it within a main conditional just running
# the code in the interpreter
# General form of list commprehension is the following
# list = [param for param in itterable]

list1 = [x for x in range(10)]
print(list1)
list2 = [x/2 for x in range(10)]
print(list2)
list3 = [x/2 for x in range(10) if x%2==0]
print(list3)


# Exercise 2:
"""
Given a list of characters that include duplicate characters, write a comprehension
that finds the duplicates and returns the characters that are duplicated in the original
list
"""

letters_list = ["a", "b", "c", "d", "b", "e", "c"]

# example of solving this with a for loop:
# duplicates = []
# for value in letters_list:
#     if letters_list.count(value) >=1:
#         if value not in duplicates:
#             duplicates.append(value)

duplicates_list = list({letter for letter in letters_list if letters_list.count(letter)>1})
