"""
Example of the use of the keyword 'finally'
"""

if __name__=="__main__":
    authenticated = False
    while not authenticated:
        try:
            age = int(input("What is your age?\nAge: "))
            if age >= 18:
                print(f"Age of {age} is authenticated")
                authenticated = True
            1/age #make sure that the value is greater than zero
        except (ValueError) as err:
            print(f"Please input numbers. Error: {err}")
        except (ZeroDivisionError) as err:
            print(f"Please provide values greater than 0. Error: {err}")
        else:
            # Called when no exception occurs
            print("Thank you!")
        finally:
            print(f"Logging call")