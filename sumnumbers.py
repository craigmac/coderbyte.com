def sumNum(num):

    '''(num) -> num

    Add up all the numbers from 1 to num and return the result.

    >>> sumNum(5)
    15
    >>> sumNum(0)
    0
    >>> sumNum(3)
    6
    '''

    # Set up iterator.
    i = 0

    # Start the loop.
    for i in range(num):
        num = num + i
        

    # Return the value.
    return num

# Have to use int() here because input creates a string
sum = (sumNum(int(input('Enter a number: '))))
print('From 0 to your number, the sum total is: ' + str(sum))
