"""
Interview Question: 

Write a function that finds all pairs whos sum is equal to a 
specified amount.

Questions to ask:
1) What is the range of numbers in the list/array? Do we need
    consider negatives in additionf to positives? 

2) Do we need to be concerned about repeating numbers?

3) Can we use values only once? IE: Looking for pairs that
    sum to 6 and we have 3 in the list; can we use it twice? 

4) Am I safe to assume that we don't care about order of pairs?
    IE: (4,1) is the same as (1,4)

5) Question: Do you want the pairs themselves or the indicies of
    the nummbers? 
"""

def find_sum_pairs(arr:list, desired_sum:int)->list:
    """
    Helper function to find all pairs that sum to the desired sum

    Input: (List) numbers
    Output: (List) list of tuples thhat have the correct sum
    """
    results = []
    # You have to itterate over the whole array because identified+2 pair
    # could be next to each other at the end. 
    # for x in range(len(arr)):
    #     # Itterate over the whole array
    #     for y in range(x+1, len(arr)):
    #         # Itterate over the remainder of the array
    #         if desired_sum == arr[x]+arr[y]:
    #             results.append([[x,y], [arr[x],arr[y]]])
    # return results

    for idx, val in enumerate(arr):
        for ydx, val2 in enumerate(arr[idx+1:]):
            if idx == ydx:
                # Assumption is that we don't want to repeat
                continue
            if desired_sum == val + val2:
                results.append([[val,val2], [idx,ydx+idx+1]])
    return results


if __name__ == "__main__":
    values = [2,6,3,9,11]
    pairs = find_sum_pairs(values, 9)
    print(pairs)
