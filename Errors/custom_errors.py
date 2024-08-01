"""
Demonstrati(on raising custom errors
"""

if __name__ == "__main__":
    authenticated = False
    while not authenticated:
        try:
            age = int(input("What is your age? "))
            10/age #<- Throw ZeroDivisionError
            if age < 0:
                # Raise our own value error with custom error text.
                raise ValueError("Plase provide positive values")
            if age >= 18:
                # Appropriate age
                authenticated = True
                print(f"Age of {age} is approved")
        except ZeroDivisionError as err:
            print("Invalid age of zero: {err}")
        else:
            print("Thanks!")
