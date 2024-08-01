"""
Introduction to error handling 
"""

if __name__ == "__main__":
    authenticated = False
    while not authenticated:
        try:
            age = int(input("What is your age?\nAge: "))
            if age >= 18:
                print("Age autheticated")
                authenticated = True
            else:
                print("Authentication not commplete, please input an age greater than or equal to 18")
        except ValueError:
            ## Input is not able to be converted to an int
            print("Please put in a number")
        