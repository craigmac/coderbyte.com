#! /usr/bin/python

'''Using the Python language, have the function ArithGeo(arr) take the array
of numbers stored in arr and return the string "Arithmetic" if the sequence
follows an arithmetic pattern or return "Geometric" if it follows a geometric
pattern. If the sequence doesn't follow either pattern return -1. An
arithmetic sequence is one where the difference between each of the numbers
is consistent, where as in a geometric sequence, each term after the first
is multiplied by some constant or common ratio.

Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54].

Negative numbers may be entered as parameters, 0 will not be entered,
and no array will contain all the same elements.'''

def ArithGeo(arr):
    '''(list of int) -> str'''

    diff_arith = arr[1] - arr[0]
    geo_seq = arr[1]/arr[0] # Gives the multiplier. 

    if arr[2] - (arr[1]) == diff_arith: # Seem to meet arith seq. Check rest.
        for num in range(len(arr)- 1):
            if arr[num + 1] - (arr[num]) != diff_arith:
                return '-1' # Does not fit the pattern.
        return 'Arithmetic'
    elif arr[2] / arr[1] == geo_seq: # Seems to meet geo seq. Check rest.
        for num in range(len(arr) - 1):
            if arr[num + 1] / arr[num] != geo_seq:
                return '-1'
        return 'Geometric'
    else: # Doesn't meet either sequence beginning.
        return '-1'

        
print ArithGeo([2, 4, 6, 8]) # Arithmetic
print ArithGeo([2, 6, 18, 54]) # Geometric
print ArithGeo([9, 4, 15, 3, 7])



