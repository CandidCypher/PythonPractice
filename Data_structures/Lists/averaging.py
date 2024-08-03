"""
Average script
"""

if __name__ == "__main__":
    total = 0
    count = 0
    while True:
        inp = input("Enter a Number: ")
        if inp == 'done': break
        value = float(inp)
        total += value
        count += 1
        average = total / count
    print(f"Average is {average}")