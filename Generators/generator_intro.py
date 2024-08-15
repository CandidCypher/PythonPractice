"""
Introduction to Generators
"""

# A very common generator is 'range' which yeilds numbers upon request.
# ie: 
range(100)
list(range(100))


#Demonstration of why generators are valuable
def make_list(nums:int)->list:
    """
    Info: Function that takes a len value and reteurns
    a list of numbers of that len with values * 2
    """
    result = []
    # Range is a generator which keeps track of where it is
    # and can return new numbers each time it is called.
    for i in range(nums):
        result.append(i*2)
    return result

def genrator_function(nums:int)->int:
    """
    Info: Generator function that will return a value * 2 
    based upon the calling of the function
    """
    for i in range(nums):
        # Yield pauses function and returns when next() is
        # is called on generator objects.
        yield i*2

if __name__ == "__main__":
    # We create a list object that exists in memory
    # this is bad for really large objects
    #my_list = make_list(100)
    #print(my_list)

    # Example of more efficient method of doing this
    # for item in genrator_function(100):
    #     print(item)

    # Using a generator object
    gen = genrator_function(100)
    print(gen) # <- shows the address of the object

    print(next(gen))
    print(next(gen))