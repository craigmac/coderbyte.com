#! /usr/bin/python

# factorial the hard way. Easy way is to import math and use math.factorial(# x)

def FirstFactorial(num):
    '''(num) -> num
    
    Take num and return factorial of it.
    
    >>> FirstFactorial(9)
    362280
    >>> FirstFactorial(4)
    4
    '''
    i = num -1 # counter
    ans = 0 # accumulator

    if num == 0 or num == 1:
        return ans # return passed in value
    else:
        while i > 0:
            ans = ans + (num * i)
            i = i - 1
    return ans

# if passed in number 4:
# pass 1: i = 3, ans = 12
# pass 2: i = 2, ans = 8, ans = 20
# pass 3: i = 1, ans = 4, ans = 24
# pass 4: i = 0, return ans = 24

# Using recursion to do factorial

def recursion_factorial(n):
    '''(num) -> num

    Returns a number which is the factorial of n.

    '''
    if n == 1:
        return n
    else:
        return n * recursion_factorial(n-1)

num = int(input('Enter a number for factorial: ')

# checks 
#if num < 0:
#   print('Sorry, numbers cannot be negative to do factorial')
#elif num == 0:
#    print('The factorial of 0 is 1')
#else:
#    print('The factorial of ',num, 'is ', recursion_factorial(num))
    
