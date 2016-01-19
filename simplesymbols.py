#! /usr/bin/python
import re

def SimpleSymbols(str):

    '''(str) -> bool

    Return True or False based on whether str is an acceptable
    sequence according to these rules:

    str parameter must be composed of + and = symbols with
    several letters between them (e.g., ++d+===+c++==a).

    For str to be True, each letter (not num) must be
    surrounded by a + symbol. Example above is False.

    Precondition: str not empty and have at least one letter.
    '''

    # Test if str is empty
    if str == '':
        return False
    # Regexp to check if any alphabet characters.
    if not re.search('[a-zA-Z]+',str):
        return False
    # Str not empty, has alpha chars and '+' symbols
    else:
        # Set up state tracker.
        flag = False
        
        for char in range(len(str)):
            if str[char].isalpha():
                if char == 0: # If it is the first index. Can't be surrounded.
                    flag = False
                    return flag
                elif char == len(str)-1:
                    flag = False
                    return flag # It was the last index. Can't be surrounded.
                else:
                    if str[char-1] == '+' and str[char+1] == '+':
                        flag = True # Surrounded by '+'.
                        # Don't return here, continue to next char.
                    else:
                        flag = False
                        return flag # Not surrounded by '+'
        return flag # Char has run through str and is never alpha, return default False.
                    # Should never reach this point because of prior gotchas before this for loop.
                               
print(SimpleSymbols('+a+')) # True
print(SimpleSymbols('++a++')) # True
print(SimpleSymbols('+a+b+')) # True
print(SimpleSymbols('+a')) # False
print(SimpleSymbols('=a+b+')) # False

