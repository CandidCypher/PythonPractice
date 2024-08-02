"""
Simple demo of using the 'remove' method of an array object
"""
import array

if __name__ == "__main__":
    my_array = array.array("i", [1,2,3,4,5,6,7,8,9])
    print(my_array)

    my_array.remove(3)

    print(my_array)