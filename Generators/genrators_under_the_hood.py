def special_for(iterable):
    """
    Info: A custom implementation of the for keyword.
    """
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break


class MyGen():
    """
    Info: Special Class for a range object
    """
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration
    

if __name__ == "__main__":
    gen = MyGen(0,100)
    for i in gen:
        print(i)