#! /usr/bin/python

'''Using the Python language, have the function ArrayAdditionI(arr) take
the array of numbers stored in arr and return the string true if any
combination of numbers in the array can be added up to equal the largest
number in the array, otherwise return the string false.

For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return
true because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not
contain all the same elements, and may contain negative numbers. '''

def ArrayAdditionI(arr):
    '''(list of num) -> str'''

    lrg = max(arr)

    i = 0
    j = 1

    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[i] + arr[j] == lrg:
                return 'true'
            j += 1
        i += 1    
    return 'false'    
            
print ArrayAdditionI([4, 6, 23, 10, 1, 3])      
            
    
