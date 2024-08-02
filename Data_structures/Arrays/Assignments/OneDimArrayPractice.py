"""
Practice assignment for one dimentional arrays
"""

import array

# 1: Create a (1-D) array and traverse it
my_array = array.array("f", [1.1, 1.2, 1.5, 2.8, 1.99])
for idx, val in enumerate(my_array):
# 2: Access individual elements through indexess
    print(my_array[idx])

# 3: Append any value to the array using the append() method
my_array.append(7.89)

# 4: Insert a value into the array at any specified index
my_array.insert(2, 3.3)

# 5: Extend the python array with the extend() method
# Note: the append method only adds one element however the 
# extend() method appends a list object
my_array.extend([7.8, 8.8, 9.9])

# 6: Add items from a list into an array using fromlist() method
list_to_add = [1.5, 1.9, 10.8]
my_array.fromlist(list_to_add)

# 7: Remove a specified element from an array using the remove() method
if 1.99 in my_array:
    # Demonstrates the issue with floating point in Python
    print("Found an element")
my_array.remove(my_array[2]) # Work around

# 8: Rmove the last element usinng pop()
my_array.pop()
my_array.pop(2)

# 9: Fetch any element through its index using index
value = my_array[5]
fetched_index = my_array.index(value)
print(fetched_index) # <- This value would be 5

# 10: Reverse an array byt calling reverse() * This is an inplace operation
my_array.reverse()
print(my_array)

# 11: Get array buffer information through buffer_info()
# This method returns the memory address and the length of an array
print(my_array.buffer_info())
addr, length = my_array.buffer_info()
print(f"my_array address: {hex(addr)} is of length: {length}")

# 12: Check the number of occurences of a value using count()
int_array = array.array("i", [1,2,3,4,4,5,5,5,5,5])
print(int_array.count(5))

# 13: Convert an arry to a string using tostring() method <- Must first be a list
# Note: As of Python 3.9 the tostring() method for arrays has been completely removed


# 14: convert an array to a list object using tolist()
listed_array = my_array.tolist()

#15 Append a string to the char array using fromstring() method
# Note: fromstring() has also been removed

# 16: Slice an array 
my_array_len = len(my_array)
print(my_array[int(my_array_len/2):])