#! /usr/bin/python

''' Using python, have the function VowelCount(str) take
the str string parameter and return the number of vowels
the string contains. e.g. 'all cows eat grass' -> 5
Do not count 'y' as a vowel for this challenge. '''

# List comprehension way, most concise and easy
def VowelCount(string):
    count = [c for c in string if c in 'aeiou']
    return len(count)

# Counter way, bit more elaborate.
##def VowelCount(string):
##    count = 0
##    for c in string:
##        if c in 'aeiou':
##            count += 1
##    return count

print VowelCount('all cows eat grass')
print VowelCount('zzyz')
print VowelCount('aeiouy')
