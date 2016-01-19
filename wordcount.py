#! /usr/bin/python

'''Using the Python language, have the function
WordCount(str) take the str string parameter being
passed and return the number of words the string contains
(ie. "Never eat shredded wheat" would return 4). Words
will be separated by single spaces.'''

def WordCount(string):
    '''(str) -> int'''

    words = string.split()

    return len(words)

print WordCount('Never eat shredded wheat') # 4
print WordCount('') # 0
print WordCount('Thiswill be three') # 3
