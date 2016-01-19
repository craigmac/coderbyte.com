#! /usr/bin/python

'''
Using the Python language, have the function MeanMode(arr) take the array of numbers
stored in arr and return 1 if the mode equals the mean, 0 if they don't equal each other
(ie. [5, 3, 3, 3, 1] should return 1 because the mode (3) equals the mean (3)).
The array will not be empty, will only contain positive integers, and will not
contain more than one mode.
'''

# Mean is the middle value: to find, list in numerical order

# Mode is the value that occurs the most often

def MeanMode(arr):

    # Calculate the mean.
    arr.sort()
    # Length of list + 1 / 2 to find halfway
    # Use - 1 on halfway number so when use value as index
    # we consider 0-index start.
    mean_index = ((len(arr) + 1) / 2) - 1
    
    # print arr[mean_index] # Test

    # Calculate the mode.
    mode = arr[0] # Set first value as the highest
    high_count = 1 
    curr_count = 1

    for i in range(len(arr) - 1):
        if arr[i] in arr[i + 1:]: # Check if in rest.
            curr_count += 1 # Add to count
            if curr_count > high_count: # Only if higher.
                high_count = curr_count
                mode = arr[i] # Current num is the most repeated.
            
    # Compare the mean and mode.
    if mode == arr[mean_index]:
        return 1
    else:
        return 0

print MeanMode([5, 3, 3, 3, 1]) # -> 1
print MeanMode([5, 3, 3, 3, 1, 10, 6, 7, 8, 4]) # Mode = 3, Mean = 4, -> 0
