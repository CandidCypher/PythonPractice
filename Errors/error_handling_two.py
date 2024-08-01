"""
Error handling within functions

"""


def sum(num1:int, num2:int)->int:
    """
    Info: Summation methods that takes two ints and returns an int of their sum
    """
    try:
        return num1 + num2
    except (TypeError) as err:
        print(f"Sum function recieved incorrect arguments: {err}")


if __name__ == "__main__":
    print(sum("1", 1))