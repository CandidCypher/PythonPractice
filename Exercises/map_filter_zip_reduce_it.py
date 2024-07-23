"""
Instructions: 
For each of the functional programming functions, write
something that highlights their utility. 
# 1: Given a list of names, use map to iteratively captialize them
# 2: Given a pair of lists, zip them together.
# 3: Given a set of numbers, find the numbers that are greater than a given threshold
# 4: Accumulate the sum of both the datasets used for both #2 and #4
"""


from functools import reduce
import string 
from random import randint

names = ["harry", "eugene", "sally", "thomas"]
letters = [letter for letter in string.ascii_lowercase]
numbers = [num for num in range(len(letters))]


def capitalize_names(name:str)->str:
    """
    Wrapper fo the string upper method for demonstrative
    purposes
    """
    return name.capitalize()


def generate_random_numbers(length:int, minimum:int=0, maximum:int=100)->list:
    """
    Helper method to generate a list of random numbers
    """
    random_numbers = []
    for x in range(length):
        random_numbers.append(randint(minimum, maximum))
    return random_numbers


def is_overtemp(temperature:int)->bool:
    """
    Info: Helper method to determine if temperature is overtemp
    """
    return temperature >=85


def accumulate(acc, item):
    """
    Accumulation helper method"""
    return acc + item


if __name__ == "__main__":
    print(f"Map Demo \n.The input: {names}\n The output:",end="")
    print(list(map(capitalize_names, names)), end="\n\n")
    print(f"Zip Demo \n The first input: {letters}\n The second input: {numbers}\n The Output: {list(zip(letters, numbers)), end }",
          end="\n\n")
    temperatures = generate_random_numbers(10,60,100)
    print(f"Filter Demo\n The input: {temperatures}\n The Output: {list(filter(is_overtemp, temperatures))}")
    print(f"Reduce Demo:\n The Output: {reduce(accumulate, (numbers + temperatures))} \n\n")