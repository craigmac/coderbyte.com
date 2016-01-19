#! /usr/bin/python

from itertools import combinations


def ArrayAdditionI(arr):

    target = max(arr)

    arr.remove(target)

    for i in range(len(arr)):
        for combo in combinations(arr, i + 1):
            # Use i + 1, because i will start at 0.
            if sum(combo)== target:
                return True
    return False



print ArrayAdditionI([1, 2, 3]) # True
print ArrayAdditionI([1, 2, 4]) # False
print ArrayAdditionI([2, 2, 2, 5, 1]) # True
print ArrayAdditionI([5, 2, 2, 5, 1])
# Last one True because 0 index alone is target.
