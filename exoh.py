#! /usr/bin/python

'''Using the Python language, have the function ExOh(str)
take the str parameter being passed and return the string
true if there is an equal number of x's and o's, otherwise
return the string false. Only these two letters will be
entered in the string, no punctuation or numbers. For
example: if str is "xooxxxxooxo" then the output should
return false because there are 6 x's and 5 o's.'''

def ExOh(string):
    x = string.count('x')
    y = string.count('o')
    if x == y:
        return 'true' # Challenge asks to return string.
    else:
        return 'false'

print ExOh('xooxxxxooxo') # False
print ExOh('xxoo') # True
print ExOh('') # True, equal num of x and y (0)
        
