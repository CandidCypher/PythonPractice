"""
Write a sorting algorithm that does not utilize sort
"""

def bubble_sort(arr:list)->list:
    """
    Bubble sort itterates ovewr a list and swaps values until
    """
    for n in range(len(arr) -1, 0, -1):
        # Start at n-1 index. Starting at the end end results in out of bound
        swapped = False # <- Flag for indicating when done
        for x in range(n):
            # itterate over the working slice
            if arr[x] > arr[x+1]:
                swapped = True
                arr[x], arr[x+1] = arr[x+1], arr[x]            
            if not swapped:
                return


if __name__ == "__main__":
    test_vaules = [x for x in range(100, 0, -1)]
    bubble_sort(test_vaules)
    print(test_vaules)
