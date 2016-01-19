#! /usr/bin/python

'''
Using the Python language, have the function SecondGreatLow(arr)
take the array of numbers stored in arr and return the second lowest
and second greatest numbers, respectively, separated by a space. For
example: if arr contains [7, 7, 12, 98, 106] the output should be 12
98. The array will not be empty and will contain at least 2 numbers.
It can get tricky if there's just two numbers!
'''

def SecondGreatLow(arr):

    if len(arr) == 2:
        return arr
    
    arr.sort() # Make sure in order.
    arr.remove(max(arr)) # Removes largest, leaves second largest

    while len(arr) > 2: # Want to have 2 answers remaining
        arr.remove(min(arr))

    return arr
        

    


print SecondGreatLow([7, 7, 12, 98, 106]) # 7 98
print SecondGreatLow([1, 2, 3, 4]) # 2 3
print SecondGreatLow([1, 1]) # 1 1
