"""
Average script: but using list operations
"""

if __name__ == "__main__":
    values = []
    while True:
        inp = input("Enter a Number: ")
        if inp == 'done':
            break
        values.append(float(inp))
    average = sum(values)/len(values)
    print(f"Average is {average}")
