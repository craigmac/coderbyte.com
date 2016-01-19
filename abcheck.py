#! /usr/bin/python

''' (str) -> bool

Challenge:
have the function ABCheck(str) take the str parameter being passed
and return the string true if the characters a and b are separated by
exactly 3 places anywhere in the string at least once (ie. "lane borrowed"
would result in true because there is exactly three characters between
a and b). Otherwise return the string false.

Example usage:
>>> ABCheck('all your base')
True
>>> ABCheck('abba')
False
>>> ABCheck('allbum')
False
>>> ABCheck('albxaster bastion')
True
'''

def ABCheck(phrase):

    string = phrase.lower()

    if 'a' not in string:
        return False
    else:    
        current_a = string.find('a')
        for char in string:
            a_index = string.find('a', current_a)
            b_index = string.find('b', a_index + 1)
            # Search from a_index b/c 'b' must be found after the furthest 'a'

            if a_index == -1: # No more a's.
                return True
            elif b_index == -1: # No more b's.
                return False
            else: # Have both a's and b's left.
                if b_index - current_a >= 3: # If separated by 3+ characters.
                    return True 
                current_a = a_index + 1 
    
print ABCheck(raw_input('Enter string to check: '))

