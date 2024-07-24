
def hello():
    print("Hello!")

def first_level(func):
    # Higher level function is a function that takes
    # a function as a parameter.  
    func()


def first_level2():
    def layer2():
        return 5
    return layer2


if __name__ == "__main__":
    print(first_level(hello))

    print(first_level2())