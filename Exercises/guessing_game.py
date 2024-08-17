"""
Very basic guessing game to demonstrate command line args and use of other packages
"""

import sys
from random import randint

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        try:
            low = int(sys.argv[1])
            high = int(sys.argv[2])
        except ValueError:
            print("Kazzoo must be given integers for our game!\nI bid thee farwell mortal!")
            sys.exit()
    else:
        print("Kazoo must know a range of values for our game!")
        sys.exit()

    random_value = randint(low, high)
    
    print(f"I am Kazzuu the magnificent!\nYou shall have three tries to guess the magic number that is between {low} and {high}")
    for x in range(3):
        match x:
            case 0:
                guess_number = "first"
            case 1:
                guess_number = "second"
            case 2:
                guess_number = "third and FINAL"
        try:
            guess = int(input(f"What is your {guess_number} guess?: "))
            if guess < low or guess > high:
                print(f"The value {guess} is not between {low} and {high}, try again!")
                continue
        except ValueError:
            print("You must provide numbers mortal!")
        if guess == random_value:
            print(f"That is correct! The magic number is {random_value}!")
            sys.exit()
        else:
            print(f"The guess of {guess} is incorrect, try again!")
    print(f"You failed! The magic number was {random_value}")