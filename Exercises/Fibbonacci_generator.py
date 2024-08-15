"""
Function for generating fibbonacci numbers
"""

def fibbonacci_genrator(number):
    a = 0
    b = 1

    for i in range(number):
        yield a
        tmp_a = a
        a = b
        b = tmp_a + b


if __name__ == "__main__":
    for x in fibbonacci_genrator(100):
        print(x)
        