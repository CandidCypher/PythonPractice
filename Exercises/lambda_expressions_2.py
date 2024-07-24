"""
Exercise 1:
Given a list, [5,4,3], return the squares of those numbers
using a lambda expression.

Exercise 2:
Sort a list of tuples based upon the 2nd index using a lambda function
"""


if __name__ == "__main__":
    squares = [5,4,3]
    print(f"Using lambda function on {squares} to output {list(map(lambda item:item**2, squares))}")

    a = [(0,2), (4,3), (9,9), (10,-1)]
    print("Sorting Demo:")
    print(f"Input: {a}")
    a.sort(key=lambda x:x[1])
    print(f"Output: {a}")