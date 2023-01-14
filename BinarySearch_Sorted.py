# Joshua Gregory/Jan. 2023
# Algorithmic Functions for Searching
# Binary Searching through sorted and unsorted lists

import random, math

def bin_srtd(lst, n):
    ''' Binary Search sorted list; parameters include a list of nums 1-100
        in sorted order and an n value to find '''

    # iterate over indices and elements of sorted list
    for i, e in enumerate(lst):
        if n == e:
            print("...")

def binary_srtd(lst, n):
    ''' Binary Search sorted list; parameters include a list of nums 1-100
        in unsorted order and an n value to find '''

    # set bounds for search
    upper = len(lst) - 1
    middle = 0
    lower = 0

    while lower <= upper:

        middle = (upper + lower) // 2  # remove list in half

        if lst[middle] < n:            # remove lower half of list
            lower = middle + 1

        elif lst[middle] > n:          # remove upper half of list
            upper = middle - 1

        else:                          # else, n = middle value
            return middle

    return -1  # if no condition is met, n not present

def main():

    # best case, worst case, random case n values
    n1 = 1
    n2 = 100
    n3 = random.randrange(1, 101)

    # list to search
    lst = list(range(1, 101))

    # initialize variables using search function for each case n
    result1 = binary_srtd(lst, n1)
    result2 = binary_srtd(lst, n2)
    result3 = binary_srtd(lst, n3)

    if result1 != -1:
        print(f"{n1} found at index {result1}.")
    else:
        print(f"Element not present in list.")

    if result2 != -1:
        print(f"{n2} found at index {result2}.")
    else:
        print(f"Element not present in list.")

    if result3 != -1:
        print(f"{n3} found at index {result3}.")
    else:
        print(f"Element not present in list.")

if __name__ == "__main__":
    main()
