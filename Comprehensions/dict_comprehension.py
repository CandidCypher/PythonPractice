"""
Dictionary comprehension is sort of similar to list comprehension

dict = {key:value for key,value in itterable}
"""
import names
import random

# Example 1: Converting a list of tuples to a dict
data = [("gary", 0), ("jane", 123), ("john", 723)]
phone_book = {key:value for key,value in data}
print(phone_book)

# Example 2: Using it to reduce an existing dictionary
first_names = [names.get_first_name() for x in range(100)]
numbers = [random.randint(1,9) for x in range(100)]
# Combining the data into a list of tuples
phone_data = [(name,number) for name,number in zip(first_names, numbers)]
reduced_data = {key:value for key,value in phone_data if value%2==0}
