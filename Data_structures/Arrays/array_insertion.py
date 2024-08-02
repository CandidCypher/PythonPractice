import array
import numpy as np


if __name__ == "__main__":
    my_stl_array = array.array("i", [1,2,3,4])

    my_stl_array.insert(0, 6)

    my_stl_array.insert(2, 11)
    
    my_stl_array.append(15)

    my_stl_array.insert(len(my_stl_array)-2, 100)
    # Question, where do you think this will be?
    # my_stl_array = [6,1,11,2,3,4,15]

    #Ans: [6,1,11,2,3,100,4,15]
    # Notes: inserts the value 6 at index 0
    my_np_array = np.array([1,2,3,4,5.123])
    # The declaration of the dtype is intelligent and
    # creates an array based upon the innformation that is passed into it. 

    np.insert(my_np_array,1,2) # insert the value 2 at index 1 (index zero based)
    print(my_np_array)
    # ?? What happened, it didn't insert it? the np.insert function returns a new array
    my_np_array = np.insert(my_np_array,0,6)
    my_np_array = np.insert(my_np_array, 2, 11)
    my_np_array = np.append(my_np_array, 15)
