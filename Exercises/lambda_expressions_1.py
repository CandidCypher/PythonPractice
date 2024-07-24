"""
This is a brief demo of the use of lambda functions.
For declaring lambda functions the general syntax is:
lambda param: action

The importance of lambda functions is that they are functions defined
in place which is valueable when 
"""

def multiply_by2(value:int)->int:
    """
    Info: Wrapper method to multiply a value by two
    Input (int): value to be multiplied
    Output (int): The value mutliplied by 2
    """
    return value*2


if __name__ == "__main__":
    values = [1,2,3,4,5]
    print("Demo using our own function")
    print(f"The input: {values}\n The Output: {list(map(multiply_by2, values))}",end="\n\n")
    print("Demo using a lambda function instead of the defined function")
    print(f" The input: {values}\n The Output: {list(map(lambda item:item*2, values))}")
